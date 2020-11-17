package com.github.lamba92.fds

import Common.*
import ComparisonGrpcKt.ComparisonCoroutineStub
import DetectionGrpcKt.DetectionCoroutineStub
import EmbeddingGrpcKt.EmbeddingCoroutineStub
import EmbeddingOuterClass.EmbeddingResponse
import ExtractionGrpcKt.ExtractionCoroutineStub
import ExtractionOuterClass.ExtractionResponse
import ExtractionOuterClass.ExtractionResponse.AnnotatedPortrait
import GatewayGrpcKt
import GatewayOuterClass.*
import GatewayOuterClass.ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding
import io.grpc.ManagedChannelBuilder
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import megabytes

class GatewayService : GatewayGrpcKt.GatewayCoroutineImplBase() {

    private fun channelFromEnv(name: String) = envOrThrow(name)
        .split(":").let { (host, port) ->
            ManagedChannelBuilder.forAddress(host, port.toInt())
                .usePlaintext()
                .maxInboundMessageSize(100.megabytes)
                .build()
        }

    private val detectionApp =
        DetectionCoroutineStub(channelFromEnv("DETECTOR_HOSTNAME"))

    private val extractionApp =
        ExtractionCoroutineStub(channelFromEnv("EXTRACTOR_HOSTNAME"))

    private val embeddingApp =
        EmbeddingCoroutineStub(channelFromEnv("EMBEDDER_HOSTNAME"))

    private val comparisonApp =
        ComparisonCoroutineStub(channelFromEnv("COMPARATOR_HOSTNAME"))

    override suspend fun elaborate(request: ElaborationRequest): ElaborationResponse =
        detectionApp.detect(request.imagesList)
            .itemsList
            .asFlow()
            .map { extractionApp.extract(it.image, it.annotationsList) }
            .map { it to embeddingApp.embed(it.extractedList.map { it.image }) }
            .map { (extractionResponse: ExtractionResponse, embeddingResponse: EmbeddingResponse) ->
                extractionResponse.originalImage to extractionResponse.extractedList
                    .zip(embeddingResponse.resultsList) { ext: AnnotatedPortrait, emb: EmbeddingContainer ->
                        PortraitWithEmbedding(emb.arrayList, ext.image, ext.annotation)
                    }
            }
            .map { (originalImage: String, data: List<PortraitWithEmbedding>) ->
                ImageWithExtractedData(originalImage, data)
            }
            .toList()
            .let { ElaborationResponse(it) }

    override suspend fun comparePortraits(request: ComparePortraitsRequest): ComparisonResult =
        listOf(request.portrait, request.otherPortrait)
            .let { detectionApp.detect(it).itemsList }
            .asFlow()
            .map { extractionApp.extract(it.image, it.annotationsList) }
            .map { it.extractedList[0].image }
            .toList()
            .let { embeddingApp.embed(it).resultsList }
            .let { (e1, e2) -> ComparisonRequest(listOf(e1), listOf(e2)) }
            .let { comparisonApp.compare(it).resultsList.first()!! }

}


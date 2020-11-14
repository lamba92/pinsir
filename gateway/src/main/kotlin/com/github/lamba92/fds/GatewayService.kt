package com.github.lamba92.fds

import DetectionGrpcKt.DetectionCoroutineStub
import EmbeddingGrpcKt.EmbeddingCoroutineStub
import EmbeddingOuterClass.EmbeddingResponse
import EmbeddingOuterClass.EmbeddingResponse.Embedding
import ExtractionGrpcKt.ExtractionCoroutineStub
import ExtractionOuterClass.ExtractionResponse
import ExtractionOuterClass.ExtractionResponse.AnnotatedPortrait
import GatewayGrpcKt
import GatewayOuterClass.GatewayResponse.ImageWithExtractedData.PortraitWithEmbedding
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

    override suspend fun elaborate(request: GatewayOuterClass.GatewayRequest) =
        detectionApp.detect(request.imagesList)
            .itemsList
            .asFlow()
            .map { extractionApp.extract(it.image, it.annotationsList) }
            .map { it to embeddingApp.embed(it.extractedList.map { it.image }) }
            .map { (extractionResponse: ExtractionResponse, embeddingResponse: EmbeddingResponse) ->
                extractionResponse.originalImage to extractionResponse.extractedList
                    .zip(embeddingResponse.resultsList) { ext: AnnotatedPortrait, emb: Embedding ->
                        PortraitWithEmbedding(emb.arrayList, ext.image, ext.annotation)
                    }
            }
            .map { (originalImage: String, data: List<PortraitWithEmbedding>) ->
                ImageWithExtractedData(originalImage, data)
            }
            .toList()
            .let { GatewayResponse(it) }

}


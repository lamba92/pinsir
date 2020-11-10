package com.github.lamba92.fds

import GatewayGrpcKt
import io.grpc.ManagedChannelBuilder
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import megabytes

class GatewayService : GatewayGrpcKt.GatewayCoroutineImplBase() {

    private fun channelFromEnv(name: String) = envOrThrow(name)
        .split(":").let { (host, port) ->
            ManagedChannelBuilder.forAddress(host, port.toInt())
        }

    private val detectionApp =
        channelFromEnv("DETECTOR_HOSTNAME")
            .usePlaintext()
            .maxInboundMessageSize(100.megabytes)
            .build()
            .let { DetectionGrpcKt.DetectionCoroutineStub(it) }

    private val extractionApp =
        channelFromEnv("EXTRACTOR_HOSTNAME")
            .usePlaintext()
            .maxInboundMessageSize(100.megabytes)
            .build()
            .let { ExtractionGrpcKt.ExtractionCoroutineStub(it) }

    private val embeddingApp =
        channelFromEnv("EMBEDDER_HOSTNAME")
            .usePlaintext()
            .maxInboundMessageSize(100.megabytes)
            .build()
            .let { EmbeddingGrpcKt.EmbeddingCoroutineStub(it) }

    override suspend fun elaborate(request: GatewayOuterClass.GatewayRequest) =
        detectionApp.detect(DetectionRequest(request.imagesList))
            .itemsList
            .asFlow()
            .map { ExtractionRequest(it.image, it.annotationsList) }
            .map { extractionApp.extract(it) }
            .map { it to EmbeddingRequest(it.extractedList.map { it.image }) }
            .map { (r, request) ->
                r to embeddingApp.embed(request)
            }
            .map { (extractionResponse, embeddingResponse) ->
                extractionResponse.originalImage to extractionResponse.extractedList
                    .zip(embeddingResponse.resultsList)
                    .map { (ext: ExtractionOuterClass.ExtractionResponse.AnnotatedPortrait, emb: EmbeddingOuterClass.EmbeddingResponse.Embedding) ->
                        PortraitWithEmbedding(emb.arrayList, ext.image, ext.annotation)
                    }
            }
            .map { (originalImage, data) ->
                ImageWithExtractedData(originalImage, data)
            }
            .toList()
            .let { GatewayResponse(it) }

}

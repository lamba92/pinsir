@file:Suppress("TestFunctionName")

import DetectionGrpcKt.DetectionCoroutineStub
import EmbeddingGrpcKt.EmbeddingCoroutineStub
import ExtractionGrpcKt.ExtractionCoroutineStub
import GatewayGrpcKt.GatewayCoroutineStub
import GatewayOuterClass.GatewayRequest
import com.github.lamba92.fds.detect
import com.github.lamba92.fds.embed
import com.github.lamba92.fds.envOrThrow
import com.github.lamba92.fds.extract
import io.grpc.ManagedChannelBuilder
import kotlinx.coroutines.runBlocking
import java.util.*
import kotlin.test.Test
import kotlin.test.assertEquals

class TestFlow {

    private fun channelFromEnv(name: String) =
        envOrThrow(name).split(":").let { (host, port) ->
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

    private fun getImage() = (Thread.currentThread().contextClassLoader
        .getResourceAsStream("test2.jpg") ?: throw IllegalArgumentException("test2.jpg not found in resources"))
        .let { Base64.getEncoder().encodeToString(it.readBytes()) }!!

    private fun getTestImage(number: Int) = (Thread.currentThread().contextClassLoader
        .getResourceAsStream(number.toString().padStart(6, '0') + ".jpg")
        ?: throw IllegalArgumentException("${number.toString().padStart(6, '0')}.jpg not found in resources"))
        .let { Base64.getEncoder().encodeToString(it.readBytes()) }!!

    private val gatewayApp =
        GatewayCoroutineStub(channelFromEnv("GATEWAY_HOSTNAME"))

    @Test
    fun `test single file with a single face`(): Unit = runBlocking {
        val image = listOf(getTestImage(1))
        val detectionResponse = detectionApp.detect(image).itemsList[0]!!
        val extractedFacePortrait =
            extractionApp.extract(detectionResponse.image, detectionResponse.annotationsList).extractedList[0].image!!
        val embedding: List<Double> =
            embeddingApp.embed(listOf(extractedFacePortrait)).resultsList[0].arrayList.toList()

        val embedding2: List<Double> = gatewayApp.elaborate(image).elementsList[0].dataList[0].arrayList.toList()

        assertEquals(embedding, embedding2)
    }

    @Test
    fun `test list of pairs of images`(): Unit = runBlocking {
        val images = listOf(getTestImage(1), getTestImage(2))
        val detectionResponse = detectionApp.detect(images)
        val extraction1 =
            extractionApp.extract(
                detectionResponse.itemsList[0].image,
                detectionResponse.itemsList[0].annotationsList
            ).extractedList[0].image!!
        val extraction2 =
            extractionApp.extract(
                detectionResponse.itemsList[1].image,
                detectionResponse.itemsList[1].annotationsList
            ).extractedList[0].image!!
        val embedding1: List<Double> =
            embeddingApp.embed(listOf(extraction1)).resultsList[0].arrayList.toList()
        val embedding2: List<Double> =
            embeddingApp.embed(listOf(extraction2)).resultsList[0].arrayList.toList()

        val (gatewayEmbedding1, gatewayEmbedding2) =
            gatewayApp.elaborate(images).elementsList.map { it.dataList[0].arrayList.toList() }

        assertEquals(embedding1, gatewayEmbedding1)
        assertEquals(embedding2, gatewayEmbedding2)
    }

    private fun GatewayRequest(images: List<String>) =
        GatewayRequest.newBuilder().addAllImages(images).build()!!

    private suspend fun GatewayCoroutineStub.elaborate(images: List<String>) =
        elaborate(GatewayRequest(images))
}

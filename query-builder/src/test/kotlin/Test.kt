@file:Suppress("TestFunctionName")

import GatewayGrpcKt.GatewayCoroutineStub
import GatewayOuterClass.GatewayRequest
import io.grpc.ManagedChannelBuilder
import kotlinx.coroutines.runBlocking
import java.util.*
import kotlin.test.Test

class TestFlow {

    private fun getImage() = (Thread.currentThread().contextClassLoader
        .getResourceAsStream("test2.jpg") ?: throw IllegalArgumentException("test2.jpg not found in resources"))
        .let { Base64.getEncoder().encodeToString(it.readBytes()) }

    private val gatewayApp = ManagedChannelBuilder.forAddress("localhost", 50051)
        .usePlaintext()
        .maxInboundMessageSize(100.megabytes)
        .build()
        .let { GatewayCoroutineStub(it) }

    @Test
    fun testFile(): Unit = runBlocking {
        gatewayApp.elaborate((0..15).map { getImage() })
    }

    private fun GatewayRequest(images: List<String>) =
        GatewayRequest.newBuilder().addAllImages(images).build()!!

    private suspend fun GatewayCoroutineStub.elaborate(images: List<String>) =
        elaborate(GatewayRequest(images))
}

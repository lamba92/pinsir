import io.ktor.application.*
import io.ktor.http.*
import io.ktor.server.testing.*
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.util.*
import kotlin.test.Test
import kotlin.test.assertNotNull

class Test {

    private val b64Encoder by lazy { Base64.getEncoder()!! }

    private val serializer = Json(from= Json.Default) {
        prettyPrint = true
    }

    private fun getImage() =
        Thread.currentThread().contextClassLoader
            .getResourceAsStream("test2.jpg")!!
            .readBytes()
            .let { b64Encoder.encodeToString(it)!! }

    private fun getAnnotations() = Thread.currentThread().contextClassLoader
        .getResourceAsStream("annotation.json")!!
        .readBytes()
        .toString()
        .let { serializer.decodeFromString(ListSerializer(FaceAnnotationRequest.serializer()), it) }

    @Test
    fun testImage(): Unit = withTestApplication(Application::extractionModule) {
        val call = handleRequest(HttpMethod.Post, "extract") {
            setBody(ExtractionRequest(getImage(), getAnnotations()).toJson())
            addHeader(HttpHeaders.ContentType, ContentType.Application.Json.toString())
        }
        assertNotNull(call.response.content)
        println(call.response.content)
    }

    private fun ExtractionRequest.toJson() =
        serializer.encodeToString(this)


}

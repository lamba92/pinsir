import io.ktor.application.*
import io.ktor.http.*
import io.ktor.server.testing.*
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import java.io.File
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
        .let { String(it) }
        .let { serializer.decodeFromString<List<FaceAnnotationRequest>>(it) }

    @Test
    fun testImage(): Unit = withTestApplication(Application::extractionModule) {
        val call = handleRequest(HttpMethod.Post, "extract") {
            setBody(listOf(ExtractionRequest(getImage(), getAnnotations())).toJson())
            addHeader(HttpHeaders.ContentType, ContentType.Application.Json.toString())
        }
        assertNotNull(call.response.content)
        File("out.json").writeText(call.response.content!!)
    }

    private fun ExtractionRequest.toJson() =
        serializer.encodeToString(this)

    private inline fun <reified E> List<E>.toJson() =
        serializer.encodeToString(this)

}



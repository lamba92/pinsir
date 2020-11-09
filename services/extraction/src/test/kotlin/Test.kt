import Test.Companion.getImage
import com.github.lamba92.fds.detection.DetectionResponseItem
import com.github.lamba92.fds.extraction.ExtractionRequest
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

    companion object {
        val b64Encoder = Base64.getEncoder()!!

        fun getImage() =
            (Thread.currentThread().contextClassLoader
                .getResourceAsStream("test2.jpg") ?: throw IllegalArgumentException("resource test2.jpg not found"))
                .readBytes()
                .let { b64Encoder.encodeToString(it)!! }

        fun getAnnotations() = Thread.currentThread().contextClassLoader
            .getResourceAsStream("annotation.json")!!
            .readBytes()
            .let { String(it) }
            .let { Json.decodeFromString<List<DetectionResponseItem.FaceAnnotation>>(it) }
    }


    @Test
    fun testImage(): Unit = withTestApplication(Application::extractionModule) {
        val call = handleRequest(HttpMethod.Post, "extract") {
            setBody(ExtractionRequest(getImage(), getAnnotations()).toJson())
            addHeader(HttpHeaders.ContentType, ContentType.Application.Json.toString())
        }
        assertNotNull(call.response.content)
        File("out.json").writeText(call.response.content!!)
    }

    private fun ExtractionRequest.toJson() =
        Json.encodeToString(this)

}

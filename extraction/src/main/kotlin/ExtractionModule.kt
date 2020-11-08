import io.ktor.application.*
import io.ktor.features.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.serialization.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import kotlinx.coroutines.withContext
import java.util.*
import javax.imageio.ImageIO
import kotlin.math.max
import kotlin.math.min

fun Application.extractionModule() {

    val b64Encoder by lazy { Base64.getEncoder()!! }
    val b64Decoder by lazy { Base64.getDecoder()!! }

    install(ContentNegotiation) {
        json()
    }

    install(CallLogging)

    routing {
        contentType(ContentType.Application.Json) {
            post("extract") {
                val response = call.receive<List<ExtractionRequest>>()
                    .asFlow()
                    .map { it.elaborate(b64Decoder, b64Encoder) }
                    .toList()
                call.respond(response)
            }
        }
    }
}

suspend fun ExtractionRequest.elaborate(b64Decoder: Base64.Decoder, b64Encoder: Base64.Encoder): ExtractionResponse {
    val (image, annotations) = this
    val decodedImage = withContext(Dispatchers.IO) {
        b64Decoder.decode(image).let { ImageIO.read(it.inputStream()) }!!
    }
    return annotations.asFlow()
        .mapWithContext(Dispatchers.IO) {
            it to with(it.box) {
                val newX = max(0, x - 20)
                val newY = max(0, y - 20)
                val newW = min(x + width + 20, decodedImage.width) - newX
                val newH = min(y + height + 20, decodedImage.height) - newY
                val edge = min(newH, newW)
                decodedImage.getSubimage(newX, newY, edge, edge)!!
            }
        }
        .mapWithContext(Dispatchers.IO) { (annotation, bufferedImage) ->
            annotation to bufferedImage.toBase64Jpg(b64Encoder)
        }
        .map { (annotation, encodedImage) ->
            ExtractionResponse.AnnotatedImage(encodedImage, annotation)
        }
        .toList()
        .let { ExtractionResponse(image, it) }
}

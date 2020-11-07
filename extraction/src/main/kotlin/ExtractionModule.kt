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
                val (image, annotations) = call.receive<ExtractionRequest>()
                val decodedImage = withContext(Dispatchers.IO) {
                    b64Decoder.decode(image).let { ImageIO.read(it.inputStream()) }!!
                }
                annotations.asFlow()
                    .mapWithContext(Dispatchers.IO) {
                        it to with(it.box) {
                            decodedImage.getSubimage(x, y, width, height)!!
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
                    .also { call.respond(it) }
            }
        }
    }
}

@file:Suppress("BlockingMethodInNonBlockingContext")

import ExtractionOuterClass.ExtractionRequest
import ExtractionOuterClass.ExtractionResponse
import ExtractionOuterClass.ExtractionResponse.AnnotatedPortrait
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import kotlinx.coroutines.withContext
import java.awt.image.BufferedImage
import java.io.ByteArrayOutputStream
import java.util.*
import javax.imageio.ImageIO
import kotlin.coroutines.CoroutineContext
import kotlin.math.max
import kotlin.math.min

class ExtractionApp : ExtractionGrpcKt.ExtractionCoroutineImplBase() {

    private val encoder: Base64.Encoder = Base64.getEncoder()
    private val decoder: Base64.Decoder = Base64.getDecoder()

    override suspend fun extract(request: ExtractionRequest) =
        request.elaborate()

    private inline fun <T, R> Flow<T>.mapWithContext(
        context: CoroutineContext,
        crossinline transform: suspend (value: T) -> R
    ) = map { withContext(context) { transform(it) } }

    private fun BufferedImage.toBase64Jpg() =
        ByteArrayOutputStream()
            .also { ImageIO.write(this, "jpg", it) }
            .apply { flush() }
            .run { toByteArray() }
            .let { encoder.encodeToString(it)!! }

    private suspend fun ExtractionRequest.elaborate(): ExtractionResponse {
        val decodedImage = withContext(IO) {
            decoder.decode(image).let { ImageIO.read(it.inputStream()) }!!
        }
        return annotationsList.asFlow()
            .mapWithContext(IO) {
                require(padding >= 0) { "Padding is not >= 0" }
                it to with(it.box) {
                    val newX = max(0, x - padding)
                    val newY = max(0, y - padding)
                    var newW = min(x + width + padding, decodedImage.width) - newX
                    var newH = min(y + height + padding, decodedImage.height) - newY
                    if (squared) {
                        val edge = min(newH, newW)
                        newW = edge
                        newH = edge
                    }
                    decodedImage.getSubimage(newX, newY, newW, newH)!!
                }
            }
            .mapWithContext(IO) { (annotation, bufferedImage) ->
                AnnotatedPortrait.newBuilder()
                    .setImage(bufferedImage.toBase64Jpg())
                    .setAnnotation(annotation)
                    .build()
            }
            .toList()
            .let {
                ExtractionResponse
                    .newBuilder()
                    .setOriginalImage(image)
                    .addAllExtracted(it)
                    .build()
            }
    }

}

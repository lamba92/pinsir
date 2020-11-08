import com.github.lamba92.fds.extraction.ExtractionRequest
import com.github.lamba92.fds.extraction.ExtractionResponse
import com.github.lamba92.fds.utils.toCustom
import kotlinx.coroutines.Dispatchers
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

inline fun <T, R> Flow<T>.mapWithContext(
    context: CoroutineContext,
    crossinline transform: suspend (value: T) -> R
) = map { withContext(context) { transform(it) } }

fun BufferedImage.toBase64Jpg(b64Encoder: Base64.Encoder) =
    ByteArrayOutputStream()
        .also { ImageIO.write(this, "jpg", it) }
        .apply { flush() }
        .run { toByteArray() }
        .let { b64Encoder.encodeToString(it)!! }

suspend fun ExtractionRequest.elaborate(b64Decoder: Base64.Decoder, b64Encoder: Base64.Encoder): ExtractionResponse {
    val annotations = annotations.map { it.toCustom() }
    val decodedImage = withContext(Dispatchers.IO) {
        b64Decoder.decode(image).let { ImageIO.read(it.inputStream()) }!!
    }
    return annotations.asFlow()
        .mapWithContext(Dispatchers.IO) {
            require(padding >= 0) { "Padding is not >= 0" }
            it to with(it.box) {
                val newX = max(0, x - padding)
                val newY = max(0, y - padding)
                var newW = min(x + width + padding, decodedImage.width) - newX
                var newH = min(y + height + padding, decodedImage.height) - newY
                if (squared){
                    val edge = min(newH, newW)
                    newW = edge
                    newH = edge
                }
                decodedImage.getSubimage(newX, newY, newW, newH)!!
            }
        }
        .mapWithContext(Dispatchers.IO) { (annotation, bufferedImage) ->
            ExtractionResponse.AnnotatedPortrait(bufferedImage.toBase64Jpg(b64Encoder), annotation)
        }
        .toList()
        .let { ExtractionResponse(image, it) }
}

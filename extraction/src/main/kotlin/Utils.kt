import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.withContext
import java.awt.image.BufferedImage
import java.io.ByteArrayOutputStream
import java.util.*
import javax.imageio.ImageIO
import kotlin.coroutines.CoroutineContext

inline fun <T, R> Flow<T>.mapWithContext(
    context: CoroutineContext,
    crossinline transform: suspend (value: T) -> R
) = map { withContext(context) { transform(it) } }

suspend inline fun <T, R> Iterable<T>.mapWithContext(
    context: CoroutineContext,
    crossinline transform: suspend (value: T) -> R
) = map { withContext(context) { transform(it) } }

fun BufferedImage.toBase64Jpg(b64Encoder: Base64.Encoder) =
    ByteArrayOutputStream()
        .also { ImageIO.write(this, "jpg", it) }
        .apply { flush() }
        .run { toByteArray() }
        .let { b64Encoder.encodeToString(it)!! }

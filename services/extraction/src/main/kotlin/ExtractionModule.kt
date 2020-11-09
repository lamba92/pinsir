import com.github.lamba92.fds.extraction.ExtractionRequest
import io.ktor.application.*
import io.ktor.features.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.serialization.*
import it.lamba.ktor.utils.AllHeaders
import it.lamba.ktor.utils.any
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import org.slf4j.event.Level
import java.util.*

fun Application.extractionModule() {

    val b64Encoder by lazy { Base64.getEncoder()!! }
    val b64Decoder by lazy { Base64.getDecoder()!! }

    install(ContentNegotiation) {
        json()
    }

    install(CallLogging) {
        level = Level.DEBUG
    }

    install(CORS) {
        any()
        allowSameOrigin = true
        allowCredentials = true
        allowNonSimpleContentTypes = true
        allowXHttpMethodOverride()
        HttpHeaders.AllHeaders.forEach {
            exposeHeader(it)
        }
    }

    install(StatusPages) {
        exception<Throwable> {
            call.respond(mapOf(
                "error" to it.message,
                "stack" to it.stackTrace.map { it.toString() }.let { Json.encodeToString(it) }
            ))
        }
    }

    routing {
        contentType(ContentType.Application.Json) {
            route("extract") {
                post {
                    call.receive<ExtractionRequest>()
                        .elaborate(b64Decoder, b64Encoder)
                        .let { call.respond(it) }
                }
                post("array") {
                    call.receive<List<ExtractionRequest>>()
                        .asFlow()
                        .map { it.elaborate(b64Decoder, b64Encoder) }
                        .toList()
                        .let { call.respond(it) }
                }
            }
        }
    }
}

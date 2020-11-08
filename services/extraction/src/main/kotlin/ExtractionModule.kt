import com.github.lamba92.fds.extraction.ExtractionRequest
import io.ktor.application.*
import io.ktor.features.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.serialization.*
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.toList
import java.util.*

fun Application.extractionModule() {

    val b64Encoder by lazy { Base64.getEncoder()!! }
    val b64Decoder by lazy { Base64.getDecoder()!! }

    install(ContentNegotiation) {
        json()
    }

    install(CallLogging)

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

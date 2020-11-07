import io.ktor.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.util.*

@KtorExperimentalAPI
fun main() {
    embeddedServer(CIO, port = 8081, module = Application::extractionModule).start(true)
}

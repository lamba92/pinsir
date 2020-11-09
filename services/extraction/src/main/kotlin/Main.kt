import io.ktor.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.util.*
import java.lang.System.getenv

@KtorExperimentalAPI
fun main() {
    embeddedServer(
        factory = CIO,
        port = getenv("SERVER_PORT")?.toInt() ?: 8081,
        module = Application::extractionModule
    ).start(true)
}

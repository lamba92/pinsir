import io.ktor.application.*
import io.ktor.features.*
import io.ktor.serialization.*

class FaceAnnotation(box: List<Int>,) {

}

fun Application.extractionModule() {
    install(ContentNegotiation) {
        json()
    }
}

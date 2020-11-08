import com.github.lamba92.fds.queryBuilderModule
import io.ktor.application.*
import io.ktor.http.*
import io.ktor.server.testing.*
import io.ktor.util.*
import io.ktor.utils.io.core.*
import io.ktor.utils.io.jvm.javaio.*
import java.io.File
import java.lang.IllegalArgumentException
import kotlin.test.Test

@ExperimentalIoApi
@KtorExperimentalAPI
class TestFlow {

    fun getImage() = Thread.currentThread().contextClassLoader
        .getResourceAsStream("test2.jpg") ?: throw IllegalArgumentException("test2.jpg not found in resources")

    @Test
    fun testFile(): Unit = withTestApplication(Application::queryBuilderModule) {
        val call = handleRequest(HttpMethod.Post, "elaborate/file") {
            bodyChannel = getImage().toByteReadChannel()
        }
        Thread.sleep(1000)
        File("out.json").writeText(call.response.content!!)
    }

}

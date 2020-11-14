import org.gradle.api.DefaultTask
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.InputDirectory
import org.gradle.api.tasks.InputFile
import org.gradle.api.tasks.TaskAction
import org.gradle.kotlin.dsl.*
import java.io.File

open class DockerBuildx : DefaultTask() {

    enum class Architectures(val platformIdentifier: String) {
        AMD64("amd64"),
        ARM("arm"),
        ARM64("arm64")
    }

    @get:Input
    val buildArguments = project.objects.mapProperty<String, String>()

    @get:Input
    val architectures = project.objects.listProperty<Architectures>()
        .apply { set(Architectures.values().toList()) }

    @get:Input
    var imageName by project.objects.property<String>()
        .apply { set("${project.rootProject.name}.${project.name}") }

    @get:Input
    var publish by project.objects.property<Boolean>()
        .apply { set(false) }

    @get:Input
    var imageVersion by project.objects.property<String>()
        .apply { set(project.version.toString()) }

    @get:InputDirectory
    var context by project.objects.property<File>()

    init {
        group = "docker"
    }

    @OptIn(ExperimentalStdlibApi::class)
    @TaskAction
    fun buildImage() {
        project.exec {
            executable = "docker"
            args = buildList {
                add("buildx")
                add("build")
                add("-t")
                add("$imageName:$imageVersion")
                buildArguments.get().forEach { (k: String, v: String) ->
                    add("--build-arg=$k=$v")
                }
                add("--platform=${architectures.get().joinToString(",") { "linux/${it.platformIdentifier}" }}")
                if (publish)
                    add("--push")
                add(context.absolutePath)
            }
        }
    }
}

open class DockerBuildxSetup : DefaultTask() {

    init {
        group = "docker"
    }

    @TaskAction
    fun setup(): Unit = with(project) {
        exec {
            executable = "docker"
            args = listOf("buildx create --use")
        }
    }

}

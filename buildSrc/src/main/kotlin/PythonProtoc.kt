import org.gradle.api.DefaultTask
import org.gradle.api.tasks.InputDirectory
import org.gradle.api.tasks.InputFiles
import org.gradle.api.tasks.OutputDirectory
import org.gradle.api.tasks.TaskAction
import org.gradle.kotlin.dsl.*
import java.io.File

open class PythonProtoc : DefaultTask() {

    @get:OutputDirectory
    var destinationDir by project.objects.property<File>()

    @get:InputDirectory
    var sourceDir by project.objects.property<File>()

    @get:InputFiles
    val sourceFiles = project.objects.listProperty<File>()

    init {
        with(project) {
            destinationDir = file("$buildDir/grpc/python")
            sourceDir = file("src/main/proto")
            sourceFiles.set(sourceDir.walkTopDown().filter { it.extension == "proto" }.toList())
        }
        group = "grpc"
    }
    @TaskAction
    fun generate() {
        sourceFiles.get().forEach {
            project.exec {
                executable = "python"
                args = listOf(
                    "-m", "grpc_tools.protoc",
                    "-I${sourceDir.absolutePath}",
                    "--python_out=${destinationDir.absolutePath}",
                    "--grpc_python_out=${destinationDir.absolutePath}",
                    it.absolutePath
                )
            }
        }
    }
}

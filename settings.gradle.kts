rootProject.name = "face-detector-stack"

val services = arrayOf(
    ":detection",
    ":extraction",
    ":embedding"
)

include(*services, ":data", ":query-builder", ":dataset-builder")

services.forEach {
    project(it).projectDir = file("./services/${it.removePrefix(":")}")
}
project(":dataset-builder").projectDir = file("preprocessing/dataset-builder")

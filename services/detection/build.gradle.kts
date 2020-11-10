plugins {
    id("com.palantir.docker")
}

docker {
    name = "${rootProject.name}/${project.name}:${project.version}"
    files("src")
}

tasks {
    register<DockerBuildx>("dockerBuildx") {
        dependsOn(dockerPrepare)
        group = "docker"
        context = file("$buildDir/docker")
        imageName = "lamba92/${rootProject.name}.${project.name}"
        publish = true
    }
    val generatePythonDefinitions by project(":data").tasks.getting(PythonProtoc::class)
    register<Copy>("getGrpcDefinitions") {
        group = "grpc"
        dependsOn(generatePythonDefinitions)
        from(generatePythonDefinitions.destinationDir)
        into("src")
    }
}

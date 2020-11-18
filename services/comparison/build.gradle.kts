plugins {
    id("com.palantir.docker")
}

docker {
    name = "lamba92/${project.rootProject.name}.${project.name}:${project.version}"
    files(".")
}
evaluationDependsOn(":data")

val dockerBuildxSetup by rootProject.tasks.getting(DockerBuildxSetup::class)

evaluationDependsOn(":data")

tasks {
    val generatePythonDefinitions by project(":data").tasks.getting(PythonProtoc::class)
    register<Copy>("getGrpcDefinitions") {
        group = "grpc"
        dependsOn(generatePythonDefinitions)
        from(generatePythonDefinitions.destinationDir)
        into(".")
    }
    register<DockerBuildx>("dockerBuildx") {
        group = "docker"
        dependsOn(dockerPrepare, dockerBuildxSetup)
        context = dockerPrepare.get().destinationDir
    }
    val dockerBuildxPublish by registering(DockerBuildx::class) {
        group = "docker"
        dependsOn(dockerPrepare, dockerBuildxSetup)
        imageName = "lamba92/$imageName"
        context = dockerPrepare.get().destinationDir
        publish = true
    }
    val dockerBuildxPublishLatest by registering(DockerBuildx::class) {
        group = "docker"
        dependsOn(dockerPrepare, dockerBuildxSetup)
        imageName = "lamba92/$imageName"
        context = dockerPrepare.get().destinationDir
        publish = true
        imageVersion = "latest"
    }
    register("publish") {
        group = "publishing"
        dependsOn(dockerBuildxPublish, dockerBuildxPublishLatest)
    }
}

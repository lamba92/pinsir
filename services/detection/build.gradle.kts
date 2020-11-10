plugins {
    id("com.palantir.docker")
}

docker {
    name = "${rootProject.name}/${project.name}:${project.version}"
    files("detector_app.py", "app.py")
}

tasks {
    register<DockerBuildx>("dockerBuildx") {
        dependsOn(dockerPrepare)
        group = "docker"
        context = file("$buildDir/docker")
        imageName = "lamba92/${rootProject.name}.${project.name}"
        publish = true
    }
}

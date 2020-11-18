import com.github.lamba92.gradle.utils.*

plugins {
    id("com.palantir.docker")
    kotlin("plugin.serialization")
    kotlin("jvm")
    application
    id("com.google.protobuf")
}

var mainClassName: String by application.mainClass
mainClassName = "com.github.lamba92.pinsir.MainKt"

kotlin {
    target {
        compilations.all {
            kotlinOptions {
                jvmTarget = "1.8"
            }
        }
    }
    sourceSets {

        val logbackVersion: String by project
        val jupyterVersion: String by project
        val grpcKotlinVersion: String by project
        val grpcJavaVersion: String by project

        main {
            dependencies {
                implementation(project(":data"))
                implementation("ch.qos.logback", "logback-classic", logbackVersion)


            }
        }
        test {
            dependencies {
                implementation(kotlin("test-junit5"))
                implementation("org.junit.jupiter", "junit-jupiter-api", jupyterVersion)
                implementation("org.junit.jupiter", "junit-jupiter-engine", jupyterVersion)
            }
        }
    }
}

docker {
    name = "lamba92/${project.rootProject.name}.${project.name}:${project.version}"
    files(tasks.installDist.get().outputs)
    buildArgs(mapOf("APP_NAME" to project.name))
}

val dockerBuildxSetup by rootProject.tasks.getting(DockerBuildxSetup::class)

tasks {
    withType<Test> {
        useJUnitPlatform()
    }
    dockerPrepare {
        dependsOn(installDist)
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
        buildArguments.set(mapOf("APP_NAME" to project.name))
    }
    val dockerBuildxPublishLatest by registering(DockerBuildx::class) {
        group = "docker"
        dependsOn(dockerPrepare, dockerBuildxSetup)
        imageName = "lamba92/$imageName"
        context = dockerPrepare.get().destinationDir
        publish = true
        buildArguments.set(mapOf("APP_NAME" to project.name))
        imageVersion = "latest"
    }
    register("publish") {
        group = "publishing"
        dependsOn(dockerBuildxPublish, dockerBuildxPublishLatest)
    }
}


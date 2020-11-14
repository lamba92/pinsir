import com.github.lamba92.gradle.utils.*
import com.google.protobuf.gradle.*

plugins {
    id("com.palantir.docker")
    kotlin("plugin.serialization")
    kotlin("jvm")
    application
    id("com.google.protobuf")
}

var mainClassName: String by application.mainClass
mainClassName = "MainKt"

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

tasks {
    withType<Test> {
        useJUnitPlatform()
    }
    dockerPrepare {
        dependsOn(installDist)
    }
    register<DockerBuildx>("dockerBuildx") {
        group = "docker"
        dependsOn(dockerPrepare)
        context = dockerPrepare.get().destinationDir
    }
    register<DockerBuildx>("dockerBuildxPublish") {
        group = "docker"
        dependsOn(dockerPrepare)
        imageName = "lamba92/$imageName"
        context = dockerPrepare.get().destinationDir
        publish = true
        buildArguments.set(mapOf("APP_NAME" to project.name))
    }
}


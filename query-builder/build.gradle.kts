import com.github.lamba92.gradle.utils.implementation
import com.github.lamba92.gradle.utils.ktor
import com.github.lamba92.gradle.utils.lamba

plugins {
    id("com.palantir.docker")
    kotlin("jvm")
    application
}

var mainClassName: String by application.mainClass
mainClassName = "com.github.lamba92.fds.MainKt"

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
    name = "${rootProject.name}/${project.name}:${project.version}"
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
        dependsOn(dockerPrepare)
        group = "docker"
        context = file("$buildDir/docker")
        imageName = "lamba92/${rootProject.name}.${project.name}"
        buildArguments.set(mapOf("APP_NAME" to project.name))
        publish = true
    }
}

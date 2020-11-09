import com.github.lamba92.gradle.utils.implementation
import com.github.lamba92.gradle.utils.ktor
import com.github.lamba92.gradle.utils.lamba

plugins {
    id("com.palantir.docker")
    kotlin("plugin.serialization")
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

        val ktorVersion: String by project
        val logbackVersion: String by project
        val jupyterVersion: String by project
        val ktorCorsAnyVersion: String by project

        main {
            dependencies {
                implementation(project(":data"))
                implementation(ktor("server-cio", ktorVersion))
                implementation(ktor("serialization", ktorVersion))
                implementation(ktor("client-serialization", ktorVersion))
                implementation(ktor("client-apache", ktorVersion))
                implementation("ch.qos.logback", "logback-classic", logbackVersion)
                implementation(lamba("ktor-cors-any", ktorCorsAnyVersion))
            }
        }

        test {
            dependencies {
                implementation(kotlin("test-junit5"))
                implementation(ktor("server-test-host", ktorVersion))
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
}

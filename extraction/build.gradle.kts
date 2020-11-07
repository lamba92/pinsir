import com.github.lamba92.gradle.utils.*

plugins {
    id("com.palantir.docker")
    kotlin("plugin.serialization")
    kotlin("jvm")
    application
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

        val ktorVersion: String by project
        val kotlinxSerializationVersion: String by project
        val logbackVersion: String by project
        val jupyterVersion: String by project

        main {
            dependencies {
                implementation(ktor("server-cio", ktorVersion))
                implementation(ktor("serialization", ktorVersion))
                implementation(kotlinx("serialization-json", kotlinxSerializationVersion))
                implementation("ch.qos.logback", "logback-classic", logbackVersion)
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

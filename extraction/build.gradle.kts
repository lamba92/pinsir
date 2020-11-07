import com.github.lamba92.gradle.utils.ktor

plugins {
    id("com.palantir.docker")
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
        main {
            dependencies {
                val ktorVersion: String by project
                implementation(ktor("server-cio", ktorVersion))
                implementation(ktor("serialization", ktorVersion))
            }
        }
    }
}

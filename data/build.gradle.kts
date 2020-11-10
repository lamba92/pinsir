import com.github.lamba92.gradle.utils.kotlinx
import com.google.protobuf.gradle.*

plugins {
    kotlin("jvm")
    `maven-publish`
    id("com.google.protobuf")
}

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
            kotlin.srcDir("$buildDir/generated")
        }
    }
}

protobuf {
    protoc {
        val protobufVersion: String by project
        artifact = "com.google.protobuf:protoc:$protobufVersion"
    }
    plugins {
        val grpcKotlinVersion: String by project
        val grpcJavaVersion: String by project
        id("grpc") {
            artifact = "io.grpc:protoc-gen-grpc-java:$grpcJavaVersion"
        }
        id("grpckt") {
            artifact = "io.grpc:protoc-gen-grpc-kotlin:$grpcKotlinVersion:jdk7@jar"
        }
    }
    generateProtoTasks {
        all().forEach {
            it.plugins {
                id("grpc")
                id("grpckt")
            }
        }
    }
}

dependencies {
    val kotlinxSerializationVersion: String by project
    val grpcKotlinVersion: String by project
    val coroutinesVersion: String by project
    val protobufVersion: String by project
    val grpcJavaVersion: String by project
    api(kotlinx("serialization-json", kotlinxSerializationVersion))
    api("com.google.protobuf", "protobuf-java-util", protobufVersion)
    api("io.grpc", "grpc-kotlin-stub", grpcKotlinVersion)
    api(kotlinx("coroutines-core", coroutinesVersion))
    api("io.grpc", "grpc-netty", grpcJavaVersion)

}

tasks {
    register<PythonProtoc>("generatePythonDefinitions")
}

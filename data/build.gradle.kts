import com.android.build.gradle.internal.tasks.factory.dependsOn
import com.github.lamba92.gradle.utils.kotlinx
import com.github.lamba92.gradle.utils.prepareForPublication
import com.google.protobuf.gradle.*
import com.jfrog.bintray.gradle.tasks.BintrayUploadTask
import org.gradle.jvm.tasks.Jar

plugins {
    kotlin("jvm")
    `maven-publish`
    id("com.google.protobuf")
    id("com.jfrog.bintray")
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
            tasks.create<Jar>("sourcesJar") {
                group = "publishing"
                archiveClassifier.set("sources")
                from(kotlin.sourceDirectories)
            }
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

publishing {
    publications {
        create<MavenPublication>(project.name) {
            from(components["kotlin"])
            artifact(tasks.named<Jar>("sourcesJar"))
            groupId = project.group as String
            artifactId = "${rootProject.name}-${project.name}"
            version = project.version as String
        }
    }
}

tasks {
    register<PythonProtoc>("generatePythonDefinitions")
    publish.dependsOn("bintrayUpload")
}

prepareForPublication()

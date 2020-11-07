plugins {
    `kotlin-dsl`
}

repositories {
    jcenter()
    mavenCentral()
    gradlePluginPortal()
    google()
    maven("https://dl.bintray.com/lamba92/com.github.lamba92/")
}

dependencies {
    val kotlinVersion: String by project
    val dokkaVersion: String by project
    val nodePluginVersion: String by project
    val sshPluginVersion: String by project
    val dockerPluginVersion: String by project
    val lambaGradleUtilsVersion: String by project

    api(kotlin("gradle-plugin", kotlinVersion))
    api(kotlin("serialization", kotlinVersion))
    api(kotlin("reflect", kotlinVersion))
    api("org.jetbrains.dokka", "dokka-gradle-plugin", dokkaVersion)

    api("com.github.node-gradle", "gradle-node-plugin", nodePluginVersion)
    api("org.hidetake", "gradle-ssh-plugin", sshPluginVersion)
    api("com.palantir.gradle.docker", "gradle-docker", dockerPluginVersion)
    api("com.github.lamba92", "lamba-gradle-utils", lambaGradleUtilsVersion)

}

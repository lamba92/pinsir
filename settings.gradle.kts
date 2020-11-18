@file:Suppress("UnstableApiUsage")

plugins {
    `gradle-enterprise`
}

rootProject.name = "pinsir"

val services = arrayOf(
    ":detection",
    ":extraction",
    ":embedding",
    ":comparison"
)

include(*services, ":data", ":gateway", ":preprocessing:dataset-builder", ":preprocessing:training", ":preprocessing")

services.forEach {
    project(it).projectDir = file("./services/${it.removePrefix(":")}")
}

gradleEnterprise.buildScan {
    termsOfServiceUrl = "https://gradle.com/terms-of-service"
    termsOfServiceAgree = "yes"
    publishAlwaysIf(System.getenv("CI")?.toBoolean() == true)
}

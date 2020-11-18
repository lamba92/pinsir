allprojects {
    group = "com.github.lamba92"
    version = System.getenv("GITHUB_REF")?.split("/")?.last() ?: "1.0-alpha"
}

subprojects {
    repositories {
        jcenter()
        mavenCentral()
        google()
        maven("https://dl.bintray.com/lamba92/com.github.lamba92")
    }
}

tasks {
    wrapper {
        gradleVersion = "6.7"
        distributionType = Wrapper.DistributionType.ALL
    }
}

val dockerBuildxSetup by tasks.registering(DockerBuildxSetup::class)


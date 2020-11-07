allprojects {
    group = "com.github.lamba92"
    version = "1.0-SNAPSHOT"
}

subprojects {
    repositories {
        jcenter()
        mavenCentral()
    }
}

tasks {
    wrapper {
        gradleVersion = "6.7"
        distributionType = Wrapper.DistributionType.ALL
    }
}


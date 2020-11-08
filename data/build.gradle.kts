import com.github.lamba92.gradle.utils.kotlinx

plugins {
    kotlin("multiplatform")
    kotlin("plugin.serialization")
    `maven-publish`
}

kotlin{
    jvm {
        compilations.all {
            kotlinOptions {
                jvmTarget = "1.8"
            }
        }
    }
    js {
        nodejs()
    }
//    ios()
//    tvos()
//    watchos()
//    ming

    sourceSets {
        commonMain {
            dependencies {
                val kotlinxSerializationVersion: String by project
                api(kotlinx("serialization-json", kotlinxSerializationVersion))
            }
        }
    }
}

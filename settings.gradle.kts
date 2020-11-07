rootProject.name = "face-detector-stack"

include(
    "detection",
    "extraction",
    "embedding"
)

//if (file("../mtcnn-java").run { isDirectory })
//    includeBuild("../mtcnn-java") {
//        dependencySubstitution {
//            substitute(module("net.tzolov.cv:mtcnn")).with(project(":"))
//        }
//    }

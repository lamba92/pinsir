plugins {
    id("com.palantir.docker")
}

docker {
    name = "${rootProject.name}/${project.name}:${project.version}"
    files("detector_app.py", "app.py")
}

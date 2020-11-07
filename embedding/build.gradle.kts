plugins {
    id("com.palantir.docker")
}

docker {
    name = "${rootProject.name}/${project.name}:${project.version}"
    files("embedder_app.py", "app.py", "build_vgg_cache.py")
}

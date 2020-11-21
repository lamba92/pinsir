<img src="https://raw.githubusercontent.com/lamba92/pinsir/master/.github/images/pinsir-logo.svg" width="100%">

PINSIR, or Person Identification Network Stack for Identity Recognition, is a scalable open source end to end solution for face detection and identity recognition.

It is divided into 4 main services Detection, Extraction, Embedding and Comparison with a 5th optional gateway service. 

# How does it work

<img src="https://raw.githubusercontent.com/lamba92/pinsir/master/.github/images/pinsir-simple-pipeline.svg" width="100%">

Identity recognition requires different steps that need to be framed independently of one another:

- Detection: given an image, for each face present in the image, a bounding box should be output;
- Extraction: each bounding box should be used to extract sub-images containing only the identified faces;
- Embedding: for each sub-image, an appropriate embedding of the face in the image.
- Comparison: given two embedding, a model should be able to say if the embeddings are from the same person or not.
- Gateway: given one or more image, can offer many high level recognition services, such as one to many identity discovery, embedding extraction and so on.

<img src="https://raw.githubusercontent.com/lamba92/pinsir/master/.github/images/pinsir-services-docker.svg" width="100%">

All containers communicate through gRPC generated from proto files available [here](/data/src/main/proto). While Kotlin/JVM and Java artifacts are available on my Maven repository (instructions below), the Python declarations are not wrapped as a library. To build them copy the proto files and run `protoc` on your own or clone the project and [run](/data/build.gradle.kts#L88) `./gradlew :data:generatePythonDefinitions` which will be available in `data/build/grpc/python`.

The training notebooks for the networks inside the Comparison service are available [here](https://drive.google.com/drive/folders/1Wp03oWdYvvwJXd8MGw58vewsGFpdglRM?usp=sharing)

# Docker images

Images are available for AMD64, ARM32 and ARM64. Working on AMD64 only! Need help to build opencv and pillow in dockerfile, PR are welcomes!

- Detection:  [`lamba92/pinsir.detection:latest`](https://hub.docker.com/repository/docker/lamba92/pinsir.detection)
- Extraction: [`lamba92/pinsir.extraction:latest`](https://hub.docker.com/repository/docker/lamba92/pinsir.extraction)
- Embedding:  [`lamba92/pinsir.embedding:latest`](https://hub.docker.com/repository/docker/lamba92/pinsir.embedding)
- Comparison: [`lamba92/pinsir.comparison:latest`](https://hub.docker.com/repository/docker/lamba92/pinsir.comparison)
- Gateway:    [`lamba92/pinsir.gateway:latest`](https://hub.docker.com/repository/docker/lamba92/pinsir.gateway)


# Example usage
This is an example compose file for Docker Composer or Docker Swarm:
```yaml
version: "3.8"
services:
  detection:
    image: lamba92/pinsir.detection:latest

  extraction:
    image: lamba92/pinsir.extraction:latest

  embedding:
    image: lamba92/pinsir.embedding:latest

  comparison:
    image: lamba92/pinsir.comparison:latest
    environment:
      - MODEL: SIMPLE+ #default
#     - MODEL: SIMPLE
#     - MODEL: COMPLEX

  gateway:
    image: lamba92/pinsir.gateway:latest
    ports:
    - 50051:50051
    environment:
      DETECTOR_HOSTNAME: "detection:50051"
      EXTRACTOR_HOSTNAME: "extraction:50051"
      EMBEDDER_HOSTNAME: "embedding:50051"
      COMPARATOR_HOSTNAME: "comparison:50051"

```

# Maven [ ![Download](https://api.bintray.com/packages/lamba92/com.github.lamba92/pinsir/images/download.svg) ](https://bintray.com/lamba92/com.github.lamba92/pinsir/_latestVersion)
JVM clients and Kotlin extension function utils available at Maven. Gradle Kotlin DSL:
```kotlin
repositories {
    maven("https://dl.bintray.com/lamba92/com.github.lamba92")
}

dependencies {
    implementation("com.github.lamba92:pinsir-data:LATEST_VERSION")
}
```
Maven:
```xml
<repositories>
    <repository>
      <id>lamba92</id>
      <name>lamba92 repo</name>
      <url>https://dl.bintray.com/lamba92/com.github.lamba92</url>
    </repository>
</repositories>

<dependency>
    <groupId>com.github.lamba92</groupId>
    <artifactId>pinsir-data</artifactId>
    <version>LATEST-VERSION</version>
    <type>pom</type>
</dependency>
```

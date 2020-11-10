@file:Suppress("FunctionName")

package com.github.lamba92.fds

import java.lang.IllegalArgumentException

fun GatewayResponse(elements: List<GatewayOuterClass.GatewayResponse.ImageWithExtractedData>) =
    GatewayOuterClass.GatewayResponse.newBuilder().addAllElements(elements).build()!!

fun ImageWithExtractedData(originalImage: String, data: List<GatewayOuterClass.GatewayResponse.ImageWithExtractedData.PortraitWithEmbedding>) =
    GatewayOuterClass.GatewayResponse.ImageWithExtractedData.newBuilder().setOriginalImage(originalImage).addAllData(data).build()!!

fun PortraitWithEmbedding(embedding: List<Double>, face: String, annotation: Common.FaceAnnotation) =
    GatewayOuterClass.GatewayResponse.ImageWithExtractedData.PortraitWithEmbedding.newBuilder().addAllArray(embedding).setFaceImage(face).setAnnotation(annotation).build()!!

fun EmbeddingRequest(images: List<String>) =
    EmbeddingOuterClass.EmbeddingRequest.newBuilder().addAllImages(images).build()!!

fun ExtractionRequest(image: String, annotations: List<Common.FaceAnnotation>) =
    ExtractionOuterClass.ExtractionRequest.newBuilder().setImage(image).addAllAnnotations(annotations).build()!!

fun DetectionRequest(images: List<String>) =
    DetectionOuterClass.DetectionRequest.newBuilder().addAllImages(images).build()!!

fun envOrThrow(name: String) =
    System.getenv(name) ?: throw IllegalArgumentException("$name not found in environment")

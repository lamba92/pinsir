@file:Suppress("FunctionName", "RemoveRedundantQualifierName")

package com.github.lamba92.pinsir

import Common.ComparisonResponse.*
import Common.ComparisonResult
import Common.EmbeddingContainer
import ComparisonOuterClass.ComparisonRequest
import GatewayOuterClass.ComparePortraitsRequest
import java.lang.IllegalArgumentException

fun ElaborationRequest(elements: List<String>) =
    GatewayOuterClass.ElaborationRequest.newBuilder().addAllImages(elements).build()!!

fun ElaborationResponse(elements: List<GatewayOuterClass.ElaborationResponse.ImageWithExtractedData>) =
    GatewayOuterClass.ElaborationResponse.newBuilder().addAllElements(elements).build()!!

fun ImageWithExtractedData(originalImage: String, data: List<GatewayOuterClass.ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding>) =
    GatewayOuterClass.ElaborationResponse.ImageWithExtractedData.newBuilder().setOriginalImage(originalImage).addAllData(data).build()!!

fun PortraitWithEmbedding(embedding: List<Double>, face: String, annotation: Common.FaceAnnotation) =
    GatewayOuterClass.ElaborationResponse.ImageWithExtractedData.PortraitWithEmbedding.newBuilder().addAllArray(embedding).setFaceImage(face).setAnnotation(annotation).build()!!

fun EmbeddingRequest(images: List<String>) =
    EmbeddingOuterClass.EmbeddingRequest.newBuilder().addAllImages(images).build()!!

fun ExtractionRequest(image: String, annotations: List<Common.FaceAnnotation>) =
    ExtractionOuterClass.ExtractionRequest.newBuilder().setImage(image).addAllAnnotations(annotations).build()!!

fun DetectionRequest(images: List<String>) =
    DetectionOuterClass.DetectionRequest.newBuilder().addAllImages(images).build()!!

fun EmbeddingContainer(array: List<Double>): EmbeddingContainer =
    EmbeddingContainer.newBuilder().addAllArray(array).build()!!

fun ComparisonRequest(embeddings: List<EmbeddingContainer>, otherEmbeddings: List<EmbeddingContainer>) =
    ComparisonRequest.newBuilder().addAllEmbeddings(embeddings).addAllOtherEmbeddings(otherEmbeddings).build()!!

fun ComparisonResponse(results: List<ComparisonResult>) =
    newBuilder().addAllResults(results).build()!!

fun ComparePortraitsRequest(portrait: String, otherPortrait: String) =
    ComparePortraitsRequest.newBuilder().setPortrait(portrait).setOtherPortrait(otherPortrait).build()!!

fun envOrThrow(name: String) =
    System.getenv(name) ?: throw IllegalArgumentException("$name not found in environment")

suspend fun EmbeddingGrpcKt.EmbeddingCoroutineStub.embed(images: List<String>) =
    embed(EmbeddingRequest(images))

suspend fun ExtractionGrpcKt.ExtractionCoroutineStub.extract(originalImage: String, annotations: List<Common.FaceAnnotation>) =
    extract(ExtractionRequest(originalImage, annotations))

suspend fun DetectionGrpcKt.DetectionCoroutineStub.detect(images: List<String>) =
    detect(DetectionRequest(images))

suspend fun GatewayGrpcKt.GatewayCoroutineStub.elaborate(images: List<String>) =
    elaborate(ElaborationRequest(images))

suspend fun GatewayGrpcKt.GatewayCoroutineStub.comparePortraits(portrait: String, otherPortrait: String) =
    comparePortraits(ComparePortraitsRequest(portrait, otherPortrait))

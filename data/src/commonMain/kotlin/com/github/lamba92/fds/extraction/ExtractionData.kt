package com.github.lamba92.fds.extraction

import com.github.lamba92.fds.detection.DetectionResponseItem
import kotlinx.serialization.Serializable

@Serializable
data class ExtractionRequest(
    val image: String,
    val annotations: List<DetectionResponseItem.FaceAnnotation>,
    val squared: Boolean = true,
    val padding: Int = 20
)

@Serializable
data class ExtractionResponse(
    val originalImage: String,
    val extracted: List<AnnotatedPortrait>
) {
    @Serializable
    data class AnnotatedPortrait(
        val image: String,
        val annotation: Annotation
    ) {
        @Serializable
        data class Annotation(
            val box: Box,
            val confidence: Double,
            val keypoints: Keypoints
        ) {
            @Serializable
            data class Box(val x: Int, val y: Int, val width: Int, val height: Int)

            @Serializable
            data class Keypoints(
                val leftEye: Point,
                val rightEye: Point,
                val nose: Point,
                val mouthLeft: Point,
                val mouthRight: Point,
            ) {
                @Serializable
                data class Point(val x: Int, val y: Int)
            }
        }
    }
}

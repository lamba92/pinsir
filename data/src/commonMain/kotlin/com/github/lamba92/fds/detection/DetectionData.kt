package com.github.lamba92.fds.detection

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

typealias DetectionRequest = List<String>

typealias DetectionResponse = List<DetectionResponseItem>

@Serializable
data class DetectionResponseItem(
    val image: String,
    val annotations: List<FaceAnnotation>
) {
    @Serializable
    data class FaceAnnotation(
        val box: List<Int>,
        val confidence: Double,
        val keypoints: Keypoints
    ) {
        @Serializable
        data class Keypoints(
            @SerialName("left_eye") val leftEye: List<Int>,
            @SerialName("right_eye") val rightEye: List<Int>,
            val nose: List<Int>,
            @SerialName("mouth_left") val mouthLeft: List<Int>,
            @SerialName("mouth_right") val mouthRight: List<Int>
        )
    }
}

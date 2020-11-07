import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class FaceAnnotationRequest(
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

@Serializable
data class FaceAnnotation(
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

fun FaceAnnotationRequest.toAnnotation() = FaceAnnotation(
    FaceAnnotation.Box(box[0], box[1], box[2], box[3]),
    confidence,
    FaceAnnotation.Keypoints(
        FaceAnnotation.Keypoints.Point(keypoints.leftEye[0], keypoints.leftEye[1]),
        FaceAnnotation.Keypoints.Point(keypoints.rightEye[0], keypoints.rightEye[1]),
        FaceAnnotation.Keypoints.Point(keypoints.nose[0], keypoints.nose[1]),
        FaceAnnotation.Keypoints.Point(keypoints.mouthLeft[0], keypoints.mouthLeft[1]),
        FaceAnnotation.Keypoints.Point(keypoints.mouthRight[0], keypoints.mouthRight[1]),
    )

)

import kotlinx.serialization.Serializable

@Serializable
class ExtractionRequest(
    val image: String,
    val annotations: List<FaceAnnotationRequest>
) {
    operator fun component1() =
        image

    operator fun component2() =
        annotations.map { it.toAnnotation() }
}

@Serializable
data class ExtractionResponse(
    val originalImage: String,
    val faces: List<AnnotatedImage>
) {
    @Serializable
    data class AnnotatedImage(val face: String, val annotation: FaceAnnotation)
}

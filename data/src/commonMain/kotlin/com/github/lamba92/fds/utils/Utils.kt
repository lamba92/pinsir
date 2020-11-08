package com.github.lamba92.fds.utils

import com.github.lamba92.fds.detection.DetectionResponseItem
import com.github.lamba92.fds.extraction.ExtractionResponse

fun DetectionResponseItem.FaceAnnotation.toCustom() = ExtractionResponse.AnnotatedPortrait.Annotation(
    ExtractionResponse.AnnotatedPortrait.Annotation.Box(box[0], box[1], box[2], box[3]),
    confidence,
    ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints(
        ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints.Point(keypoints.leftEye[0], keypoints.leftEye[1]),
        ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints.Point(keypoints.rightEye[0], keypoints.rightEye[1]),
        ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints.Point(keypoints.nose[0], keypoints.nose[1]),
        ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints.Point(keypoints.mouthLeft[0], keypoints.mouthLeft[1]),
        ExtractionResponse.AnnotatedPortrait.Annotation.Keypoints.Point(keypoints.mouthRight[0], keypoints.mouthRight[1]),
    )

)

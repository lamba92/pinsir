import base64
from io import BytesIO

import numpy as np
from PIL import Image
from mtcnn import MTCNN

from common_pb2 import FaceAnnotation, Point
from detection_pb2 import DetectionResponse, DetectionRequest
from detection_pb2_grpc import DetectionServicer


class DetectorApp(DetectionServicer):
    detector: MTCNN = MTCNN()

    def transform_annotation(self, old_annotation) -> FaceAnnotation:
        old_kp = old_annotation["keypoints"]
        return FaceAnnotation(
            box=FaceAnnotation.Box(
                x=old_annotation["box"][0],
                y=old_annotation["box"][1],
                width=old_annotation["box"][2],
                height=old_annotation["box"][3],
            ),
            confidence=old_annotation["confidence"],
            keypoints=FaceAnnotation.Keypoints(
                leftEye=Point(x=old_kp["left_eye"][0], y=old_kp["left_eye"][0]),
                rightEye=Point(x=old_kp["right_eye"][0], y=old_kp["right_eye"][0]),
                nose=Point(x=old_kp["nose"][0], y=old_kp["nose"][0]),
                mouthLeft=Point(x=old_kp["mouth_left"][0], y=old_kp["mouth_left"][0]),
                mouthRight=Point(x=old_kp["mouth_right"][0], y=old_kp["mouth_right"][0]),
            )
        )

    def process_image(self, b_64_image) -> DetectionResponse.Item:
        im = base64.b64decode(b_64_image)
        im = BytesIO(im)
        im = Image.open(im)
        im = np.asarray(im).astype(np.float32)
        ann = self.detector.detect_faces(im)
        ann = list(map(self.transform_annotation, ann))
        return DetectionResponse.Item(
            image=b_64_image,
            annotations=ann
        )

    def detect(self, request: DetectionRequest, context):
        b_64_images = list(request.images)
        items = list(map(self.process_image, b_64_images))
        return DetectionResponse(items=items)

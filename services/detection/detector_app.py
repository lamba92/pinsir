import json

import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, Response
from io import BytesIO
from mtcnn import MTCNN
import base64


class DetectorApp(Flask):
    detector: MTCNN

    def __init__(
            self,
            import_name,
            static_url_path=None,
            static_folder="static",
            static_host=None,
            host_matching=False,
            subdomain_matching=False,
            template_folder="templates",
            instance_path=None,
            instance_relative_config=False,
            root_path=None
    ):
        super().__init__(import_name, static_url_path, static_folder, static_host, host_matching, subdomain_matching,
                         template_folder, instance_path, instance_relative_config, root_path)
        self.detector = MTCNN()
        self.route('/detect', methods=['post', 'get'])(self.detect)

    def process_image(self, b_64_image):
        im = base64.b64decode(b_64_image)
        im = BytesIO(im)
        im = Image.open(im)
        im = np.asarray(im).astype(np.float32)
        return {
            "image": b_64_image,
            "annotations": self.detector.detect_faces(im)
        }

    def detect(self):
        b_64_images = request.get_json()
        annotations_list = map(self.process_image, b_64_images)
        re = Response(json.dumps(list(annotations_list)))
        re.headers["Content-Type"] = "application/json"
        return re

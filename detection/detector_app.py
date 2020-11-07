import json

import cv2
import numpy as np
from flask import Flask, request
from flask_cors import CORS
from mtcnn import MTCNN


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
        CORS(self)
        self.detector = MTCNN()
        self.route('/detect', methods=['post', 'get'])(self.detect)

    def detect(self):
        img_str = request.get_data()
        np_image = np.fromstring(img_str, np.uint8)
        decoded = cv2.imdecode(np_image, cv2.COLOR_BGR2RGB)
        image = cv2.cvtColor(decoded, cv2.COLOR_BGR2RGB)
        annotations = self.detector.detect_faces(image)
        return json.dumps(annotations)

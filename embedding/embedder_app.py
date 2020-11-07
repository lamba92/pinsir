import json

import cv2
import numpy as np
import base64

import tensorflow
from flask import Flask, request
from flask_cors import CORS
from keras_vggface import VGGFace
from keras_vggface.utils import preprocess_input


class EmbedderApp(Flask):
    model: VGGFace

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
        self.model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
        self.route('/embed', methods=['post'])(self.embed)

    # example: { "image": "base64EncodedImage" }
    def embed(self):
        b_64_image = request.get_json()["image"]
        image = tensorflow.io.decode_base64(b_64_image)
        image = tensorflow.io.decode_jpeg(image, channels=3)
        image = tensorflow.image.resize(
            image=image,
            size=(224, 224),
            method=tensorflow.image.ResizeMethod.BILINEAR,
            align_corners=False
        )
        image = preprocess_input(image, version=2)

        return json.dumps({
            "image": b_64_image,
            "vector": self.model.predict(image)[0]
        })

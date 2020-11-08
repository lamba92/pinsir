import base64
import json
from io import BytesIO

import numpy as np
from PIL import Image
from flask import Flask, request
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

    def elaborate_image(self, b_64_image):
        image = base64.b64decode(b_64_image)
        image = BytesIO(image)
        image = Image.open(image)
        image = image.resize((224, 224))
        image = np.asarray(image).astype(np.float32)
        image = np.expand_dims(image, axis=0)
        return {
            "image": b_64_image,
            "input": preprocess_input(image, version=2)
        }

    def embed(self):
        elaborated = list(map(self.elaborate_image, request.get_json()))
        inputs = np.concatenate(list(map(lambda i: i["input"], elaborated)), axis=0)
        predictions = self.model.predict(inputs)
        r = []
        images = list(map(lambda e: e["image"], elaborated))
        predictions_list = predictions.tolist()
        zipped = list(zip(images, predictions_list))
        for b_64_image, prediction in zipped:
            r.append({
                "image": b_64_image,
                "featureVector": prediction
            })
        return json.dumps(r)

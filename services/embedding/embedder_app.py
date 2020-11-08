import base64
import json
from io import BytesIO

import numpy as np
from PIL import Image
from flask import Flask, request, Response
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
        return preprocess_input(image, version=2)

    def embed(self):
        inputs = request.get_json()
        inputs = map(self.elaborate_image, inputs)
        inputs = list(inputs)
        inputs = np.concatenate(inputs, axis=0)
        predictions = self.model.predict(inputs).tolist()
        re = Response(json.dumps(predictions))
        re.headers["Content-Type"] = "application/json"
        return re

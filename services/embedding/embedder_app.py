import base64
from io import BytesIO

import numpy as np
from PIL import Image
from keras_vggface import VGGFace
from keras_vggface.utils import preprocess_input

from embedding_pb2 import EmbeddingRequest, EmbeddingResponse
from embedding_pb2_grpc import EmbeddingServicer
from common_pb2 import EmbeddingContainer


# noinspection PyMethodMayBeStatic
class EmbedderApp(EmbeddingServicer):

    model: VGGFace = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')

    def deserializer_image(self, b_64_image) -> np.array:
        image = base64.b64decode(b_64_image)
        image = BytesIO(image)
        image = Image.open(image)
        image = image.resize((224, 224))
        image = np.asarray(image).astype(np.float32)
        return np.expand_dims(image, axis=0)

    def elaborate_image(self, b_64_image):
        image = self.deserializer_image(b_64_image)
        return preprocess_input(image, version=2)

    def embed(self, request: EmbeddingRequest, context):
        inputs = list(request.images)
        inputs = map(self.elaborate_image, inputs)
        inputs = list(inputs)
        inputs = np.concatenate(inputs, axis=0)
        predictions = self.model.predict(inputs).tolist()
        return EmbeddingResponse(
            results=list(map(lambda p: EmbeddingContainer(
                array=p
            ), predictions))
        )

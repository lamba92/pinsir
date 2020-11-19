import numpy as np
import os

from comparison_pb2_grpc import ComparisonServicer
from comparison_pb2 import ComparisonRequest
from common_pb2 import ComparisonResponse, ComparisonResult
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Model


def select_model_name():
    model = os.environ.get("MODEL")
    if model == "SIMPLE":
        model = "simple_saved.h5"
    elif model == "COMPLEX":
        model = "complex_saved.h5"
    else:
        model = "simpler_saved.h5"
    return model


# noinspection PyMethodMayBeStatic
class ComparisonApp(ComparisonServicer):
    model_name = select_model_name()
    model: Model = load_model(model_name, compile=True)

    def prediction_to_result(self, prediction) -> ComparisonResult:
        return ComparisonResult(
            isSame=True if prediction[0] < prediction[1] else False,
            confidence=max(prediction[0], prediction[1])
        )

    def embeddings_to_numpy(self, embeddings):
        x = list(embeddings)
        x = list(map(lambda el: list(el.array), x))
        return np.asarray(x)

    def simple_input_transformation(self, x_a, x_b):
        x = map(lambda e: np.concatenate([e[0], e[1]]), zip(x_a, x_b))
        x = list(x)
        return np.asarray(x)

    def compare(self, request: ComparisonRequest, context) -> ComparisonResponse:
        x_a = self.embeddings_to_numpy(request.embeddings)
        x_b = self.embeddings_to_numpy(request.other_embeddings)
        x = [x_a, x_b] if self.model_name == "complex_saved.h5" else self.simple_input_transformation(x_a, x_b)
        predictions = list(map(
            self.prediction_to_result,
            self.model.predict(x)
        ))
        return ComparisonResponse(results=predictions)

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

    model: Model = load_model(select_model_name(), compile=False)

    def prediction_to_result(self, prediction) -> ComparisonResult:
        return ComparisonResult(
            isSame=True if prediction[0] < prediction[1] else False,
            confidence=max(prediction[0], prediction[1])
        )

    def embeddings_to_numpy(self, embeddings):
        x = list(embeddings)
        x = list(map(lambda el: list(el.array), x))
        return np.asarray(x)

    def compare(self, request: ComparisonRequest, context) -> ComparisonResponse:
        x_a = self.embeddings_to_numpy(request.embeddings)
        x_b = self.embeddings_to_numpy(request.other_embeddings)
        predictions = list(map(
            self.prediction_to_result,
            self.model.predict([x_a, x_b])
        ))
        return ComparisonResponse(results=predictions)

import base64
import math

import numpy as np
import orjson as json
import pandas as pd
from tensorflow.python.keras.utils.data_utils import Sequence
from urllib3 import PoolManager


class OnlineSequence(Sequence):

    url: str
    batch_size: int
    services_url: str
    class_columns_name: str
    image_columns_2_name: str
    image_columns_1_name: str
    images_path: str
    http_client: PoolManager
    df: pd.DataFrame

    def __init__(
            self,
            dataframe: pd.DataFrame,
            services_protocol: str = "http",
            services_hostname: str = "localhost",
            services_port: int = 8080,
            images_path: str = "./",
            image_columns_1_name: str = "0",
            image_columns_2_name: str = "1",
            class_columns_name: str = "2",
            batch_size: int = 8,
    ) -> None:
        super().__init__()
        if batch_size <= 0:
            raise ValueError("batch_size must be more than 0")
        self.batch_size = batch_size
        self.services_url = f"{services_protocol}://{services_hostname}:{services_port}"
        self.url = f"{self.services_url}/elaborate/embeddingOnly/flattened?facesPerImage=1"
        self.class_columns_name = class_columns_name
        self.image_columns_2_name = image_columns_2_name
        self.image_columns_1_name = image_columns_1_name
        self.images_path = images_path
        if self.images_path[len(self.images_path) - 1] != "/":
            self.images_path = self.images_path + "/"
        self.http_client = PoolManager()
        self.df = dataframe

    headers = {'Content-type': 'application/json'}

    def __len__(self):
        return math.ceil(len(self.df.index) / self.batch_size)

    def __getitem__(self, index):
        file_1_array: list = self.df[self.image_columns_1_name] \
            .iloc[index * self.batch_size:(index + 1) * self.batch_size].tolist()
        file_2_array: list = self.df[self.image_columns_2_name] \
            .iloc[index * self.batch_size:(index + 1) * self.batch_size].tolist()
        clazz = self.df[self.class_columns_name]\
            .iloc[index * self.batch_size:(index + 1) * self.batch_size].tolist()

        # (0, 1) means same, (1, 0) means different
        clazz = list(map(lambda c: (0, 1) if c == 1 else (1, 0), clazz))

        clazz = np.array(clazz)

        for i, file_name in enumerate(file_1_array):
            with open(f'{self.images_path}/{file_name}', "rb") as image_file:
                file_1_array[i] = base64.b64encode(image_file.read()).decode("utf-8")

        for i, file_name in enumerate(file_2_array):
            with open(f'{self.images_path}/{file_name}', "rb") as image_file:
                file_2_array[i] = base64.b64encode(image_file.read()).decode("utf-8")

        response_file_1_array = self.http_client.request(
            method='POST',
            url=self.url,
            body=json.dumps(file_1_array),
            headers=self.headers
        ).data.decode('utf-8')

        response_file_1_array = json.loads(response_file_1_array)

        response_file_2_array = self.http_client.request(
            method='POST',
            url=self.url,
            body=json.dumps(file_2_array),
            headers=self.headers
        ).data.decode('utf-8')

        response_file_2_array = json.loads(response_file_2_array)

        response = [np.array(response_file_1_array), np.array(response_file_2_array)]

        return response, clazz

import grpc
import pandas
import base64
import logging
from gateway_pb2 import GatewayRequest
from gateway_pb2_grpc import GatewayStub
import os
import functools
from multiprocessing import Pool
import swifter

images_location = "../img_celeba/"
dataset_file_location = "../output.txt"


def file_path_to_b64(path: str):
    with open(path, "rb") as f:
        return base64.b64encode(f.read())


def row_to_data(row, client):
    try:
        file_1 = row["file1"]
        file_2 = row["file1"]
        file_1 = file_path_to_b64(f"{images_location}{file_1}")
        file_2 = file_path_to_b64(f"{images_location}{file_2}")
        response = client.elaborate(GatewayRequest(
            images=[file_1, file_2]
        ))
        input_ = list(response.elements[0].data[0].array) + list(response.elements[1].data[0].array)
        output = (0, 1) if row["class"] == 1 else (1, 0)
        return pandas.Series(
            data=[input_, output, row["file1"], row["file1"], row["class"]],
            index=["input", "output", "file1", "file2", "class"]
        )
    except:
        logging.error(f"{row['file1']} or {row['file2']} errored")
        return pandas.Series(
            data=[None, None, row["file1"], row["file1"], row["class"]],
            index=["input", "output", "file1", "file2", "class"]
        )


def elaborate(step, step_size_, df):
    if not os.path.isfile(f"./dataset/step_{step + 1}_of_{step_size_}.pkl"):
        channel = grpc.insecure_channel('localhost:50051')
        gateway_client = GatewayStub(channel)
        print(f"Starting step #{step + 1} of {step_size_}")
        start_index = step_size_ * step
        end_index = start_index + step_size_

        step_dataset = df.iloc[start_index:end_index]
        step_dataset = step_dataset.swifter.progress_bar(True)\
            .apply(lambda row: row_to_data(row, gateway_client), axis=1)
        step_dataset.to_pickle(f"./dataset/step_{step + 1}_of_{step_size_}.pkl")


if __name__ == '__main__':

    training_dataset = pandas.read_csv(
        filepath_or_buffer=dataset_file_location,
        sep=" ",
        names=["file1", "file2", "class"]
    )

    training_dataset = training_dataset[training_dataset["class"] == 0].sample(12500) \
        .append(training_dataset[training_dataset["class"] == 1].sample(12500)) \
        .reset_index()

    items_count = len(training_dataset.index)
    step_size = int(items_count / 100)

    elaborate_packed = functools.partial(
        elaborate,
        step_size_=step_size,
        df=training_dataset
    )

    for step in range(0, step_size):
        elaborate_packed(step)

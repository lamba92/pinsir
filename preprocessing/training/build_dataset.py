from grpc import insecure_channel
import pandas
import base64
import logging
from gateway_pb2 import GatewayRequest
from gateway_pb2_grpc import GatewayStub
import os
import functools
from threading import Thread

images_location = "./img_celeba/"
dataset_file_location = "./output2.txt"


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


def elaborate(step, step_size_, parts, df, gateway_client):
    if not os.path.isfile(f"./dataset/step_{step + 1}_of_{parts}_part3.pkl"):
        print(f"Starting step #{step + 1} of {parts}")
        start_index = step_size_ * step
        end_index = start_index + step_size_

        step_dataset = df.iloc[start_index:end_index]
        step_dataset = step_dataset.apply(lambda row: row_to_data(row, gateway_client), axis=1)
        step_dataset.to_pickle(f"./dataset/step_{step + 1}_of_{parts}_part3.pkl", protocol=4, compression='zip')


def elaborate2(start, step_size_, parts, df, gateway_client):
    for i in range(start, parts):
        elaborate(i, step_size_, parts, df, gateway_client)


if __name__ == '__main__':
    training_dataset = pandas.read_csv(
        filepath_or_buffer=dataset_file_location,
        sep=" ",
        names=["file1", "file2", "class"]
    )

    training_dataset = training_dataset[training_dataset["class"] == 0].iloc[25000:50000] \
        .append(training_dataset[training_dataset["class"] == 1].iloc[25000:50000]) \
        .reset_index()

    items_count = len(training_dataset.index)
    parts = 100
    step_size = int(items_count / parts)

    threads = [
        Thread(
            target=functools.partial(
                elaborate2,
                start=7,
                step_size_=step_size,
                parts=8,
                df=training_dataset,
                gateway_client=GatewayStub(insecure_channel('localhost:50052'))
            )
        ),
        Thread(
            target=functools.partial(
                elaborate2,
                start=8,
                step_size_=step_size,
                parts=9,
                df=training_dataset,
                gateway_client=GatewayStub(insecure_channel('localhost:50053'))
            )
        ),
        Thread(
            target=functools.partial(
                elaborate2,
                start=9,
                step_size_=step_size,
                parts=10,
                df=training_dataset,
                gateway_client=GatewayStub(insecure_channel('localhost:50054'))
            )
        ),
        Thread(
            target=functools.partial(
                elaborate2,
                start=20,
                step_size_=step_size,
                parts=25,
                df=training_dataset,
                gateway_client=GatewayStub(insecure_channel('localhost:50051'))
            )
        )
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


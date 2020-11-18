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
        file_2 = row["file2"]
        file_1 = file_path_to_b64(f"{images_location}{file_1}")
        file_2 = file_path_to_b64(f"{images_location}{file_2}")
        response = client.elaborate(GatewayRequest(
            images=[file_1, file_2]
        ))
        input_ = list(response.elements[0].data[0].array) + list(response.elements[1].data[0].array)
        output = (0, 1) if row["class"] == 1 else (1, 0)
        return pandas.Series(
            data=[input_, output, row["file1"], row["file2"], row["class"]],
            index=["input", "output", "file1", "file2", "class"]
        )
    except:
        logging.error(f"#{row['index']} | {row['file1']} or {row['file2']} errored")
        return pandas.Series(
            data=[None, None, row["file1"], row["file2"], row["class"]],
            index=["input", "output", "file1", "file2", "class"]
        )


def elaborate(start, stop, df, gateway_client):
    step = int((stop-start)/10)
    for start_index in range(start, stop, step):
        end_index = start_index + step
        if not os.path.isfile(f"./dataset/step_from_{start_index}_to_{end_index}.pkl"):
            print(f"Starting step from #{start_index} to #{end_index}")
            current_df = df.iloc[start_index:end_index]
            current_df = current_df.apply(lambda row: row_to_data(row, gateway_client), axis=1)
            current_df.to_pickle(f"./dataset/step_from_{start_index}_to_{end_index}.pkl", protocol=4, compression='zip')


if __name__ == '__main__':
    training_dataset = pandas.read_csv(
        filepath_or_buffer=dataset_file_location,
        sep=" ",
        names=["file1", "file2", "class"]
    )

    training_dataset = training_dataset[training_dataset["class"] == 0].head(75000) \
        .append(training_dataset[training_dataset["class"] == 1].head(75000)) \
        .reset_index()

    items_count = len(training_dataset.index)
    parts = 6
    step_size = int(items_count / parts)

    threads = []

    for i in range(0, parts):
        threads.append(
            Thread(
                target=elaborate,
                args=(
                    i * step_size,
                    (i + 1) * step_size,
                    training_dataset,
                    GatewayStub(insecure_channel(f'localhost:5005{i + 1}'))
                )
            )
        )

    for t in threads:
        t.start()
    for t in threads:
        t.join()

import math

import pandas
import tensorflow.keras as keras
from keras import Model
from keras.layers import Dense, concatenate, Dropout, Input

from preprocessing.training.online_sequence import OnlineSequence


def build_net():
    i1 = Input(shape=(2048,))
    i2 = Input(shape=(2048,))

    d1 = Dense(1024, activation='relu', input_shape=(2048,))
    d2 = Dense(256, activation='relu')
    d3 = Dense(64, activation='relu')

    branch_1 = d1(i1)
    branch_2 = d1(i2)

    branch_1 = Dropout(0.4)(branch_1)
    branch_2 = Dropout(0.4)(branch_2)

    branch_1 = d2(branch_1)
    branch_2 = d2(branch_2)

    branch_1 = Dropout(0.2)(branch_1)
    branch_2 = Dropout(0.2)(branch_2)

    branch_1 = d3(branch_1)
    branch_2 = d3(branch_2)

    outputs = Dense(64, activation='relu')(concatenate([branch_1, branch_2]))
    outputs = Dropout(0.2)(outputs)
    outputs = Dense(16, activation='relu')(outputs)
    outputs = Dense(2, activation='softmax')(outputs)

    m = Model(inputs=[i1, i2], outputs=outputs)

    m.compile(
        optimizer=keras.optimizers.Adam(),
        loss=keras.losses.BinaryCrossentropy(),
        metrics=[keras.metrics.Accuracy()]
    )
    return m


if __name__ == '__main__':
    images_location = "../img_celeba/"
    dataset_file_location = "./output.txt"

    training_dataset = pandas.read_csv(
        filepath_or_buffer=dataset_file_location,
        sep=" ",
        names=["file1", "file2", "class"]
    )

    test_0_df = training_dataset[training_dataset["class"] == 0]
    test_0_df = test_0_df.sample(math.ceil(len(test_0_df.index) / 10), random_state=200)
    test_1_df = training_dataset[training_dataset["class"] == 1]
    test_1_df = test_1_df.sample(math.ceil(len(test_1_df.index) / 10), random_state=200)

    training_dataset = training_dataset.drop(test_0_df.index)
    training_dataset = training_dataset.drop(test_1_df.index)

    validation_0_class_df = test_0_df.sample(math.ceil(len(test_1_df.index) / 5), random_state=200)
    validation_1_class_df = test_1_df.sample(math.ceil(len(test_1_df.index) / 5), random_state=200)

    test_0_df = test_0_df.drop(validation_0_class_df.index)
    test_1_df = test_1_df.drop(validation_1_class_df.index)

    validation_dataset = pandas.concat([validation_0_class_df, validation_1_class_df])\
        .sample(frac=1, random_state=200)\
        .reset_index(drop=True)

    test_dataset = pandas.concat([test_0_df, test_1_df]) \
        .sample(frac=1, random_state=200) \
        .reset_index(drop=True)

    training_dataset = training_dataset.sample(frac=1, random_state=200) \
        .reset_index(drop=True)

    training_sequence = OnlineSequence(
        dataframe=training_dataset,
        services_port=8080,
        images_path=images_location,
        image_columns_1_name="file1",
        image_columns_2_name="file2",
        class_columns_name="class",
    )

    validation_sequence = OnlineSequence(
        dataframe=validation_dataset,
        services_port=8080,
        images_path=images_location,
        image_columns_1_name="file1",
        image_columns_2_name="file2",
        class_columns_name="class"
    )

    model = build_net()
    model.fit(
        training_sequence,
        validation_data=training_sequence,
        epochs=10,
        steps_per_epoch=training_sequence.__len__(),
        callbacks=[
            keras.callbacks.ModelCheckpoint(f"./checkpoint.h5"),
            keras.callbacks.EarlyStopping(monitor="accuracy")
        ],
        workers=8
    )

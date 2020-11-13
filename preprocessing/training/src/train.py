import pandas as pd
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import Accuracy
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import math
import numpy as np
import swifter

if __name__ == '__main__':
    training_dataset = pd.read_pickle("./dataset/step_1_of_250.pkl")
    for i in range(2, 101):
        current_df = pd.read_pickle(f"./dataset/step_{i}_of_250.pkl")
        training_dataset = training_dataset.append(current_df, ignore_index=True)


    def tolist(array):
        return np.asarray(array).astype('float64')

    training_dataset = training_dataset.dropna()

    training_dataset["input"] = training_dataset["input"].apply(tolist)
    training_dataset["output"] = training_dataset["output"].apply(tolist)

    test_0_df = training_dataset[training_dataset["class"] == 0]
    test_0_df = test_0_df.sample(math.ceil(len(test_0_df.index) / 10), random_state=200)
    test_1_df = training_dataset[training_dataset["class"] == 1]
    test_1_df = test_1_df.sample(math.ceil(len(test_1_df.index) / 10), random_state=200)

    training_dataset = training_dataset.drop(test_0_df.index)
    training_dataset = training_dataset.drop(test_1_df.index)

    model = Sequential([
        Dense(512, input_shape=(2048,), activation='relu'),
        Dropout(0.3),
        Dense(256, activation='relu'),
        Dense(2, activation='softmax')
    ])
    model.compile(
        optimizer=Adam(),
        loss=BinaryCrossentropy(),
        metrics=[Accuracy()]
    )
    model.fit(
        x=training_dataset['input'].tolist(),
        y=training_dataset['output'].tolist(),
        validation_split=0.1,
        batch_size=32,
        epochs=10,
        callbacks=[
            ModelCheckpoint("checkpoint.h5"),
            EarlyStopping(patience=3)
        ]
    )
    model.save("classifier.h5")

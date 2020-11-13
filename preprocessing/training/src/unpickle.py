import pandas as pd

if __name__ == '__main__':
    training_dataset = pd.read_pickle("./dataset/step_1_of_250.pkl")
    for i in range(1, 101):
        pd.read_pickle(f"./dataset/step_{i}_of_250.pkl")\
            .to_pickle(f"./dataset/v4/step_{i}_of_100_v4pickle.pkl", protocol=4, compression="zip")


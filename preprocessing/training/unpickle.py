import pandas as pd
from os import walk

if __name__ == '__main__':
    training_dataset = pd.DataFrame(columns=["input", "output", "file1", "file2", "class"])
    for (_, _, filenames) in walk("./dataset"):
        for f in filenames:
            if f.endswith(".pkl"):
                current_df = pd.read_pickle(f"./dataset/{f}",  compression="zip")
                training_dataset = training_dataset.append(current_df, ignore_index=True)
    training_dataset.to_pickle("complete_data.pkl", protocol=4, compression="zip")


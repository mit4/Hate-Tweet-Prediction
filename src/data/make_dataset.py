import pandas as pd
import numpy as np

train_data = pd.read_csv("../../data/raw/05-twitter-hate-train.csv")
test_data = pd.read_csv("../../data/raw/06-twitter-hate-test.csv")

train_data.drop_duplicates(inplace=True)
test_data.drop_duplicates(inplace=True)

train_data.to_csv("../../data/interim/train_data.csv")
test_data.to_csv("../../data/interim/test_data.csv")

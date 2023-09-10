import numpy as np
import pandas as pd
import sklearn as sk

train_data = pd.read_csv("../../data/processed/train_data.csv")
test_data = pd.read_csv("../../data/processed/test_data.csv")

# Predicting label for the test data
test_data["label"] = lr.predict(X_test)
test_data.to_csv("test_results.csv", index=False)

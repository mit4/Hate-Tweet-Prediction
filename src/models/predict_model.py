import numpy as np
import pandas as pd
import sklearn as sk

# Predicting label for the test data
test_data["label"] = lr.predict(X_test)
test_data.to_csv("test_results.csv", index=False)

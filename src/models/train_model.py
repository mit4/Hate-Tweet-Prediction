import numpy as np
import pandas as pd
import sklearn as sk

X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

lr = LogisticRegression(
    class_weight="balanced", random_state=42, solver="lbfgs", max_iter=1000, n_jobs=-1
)
lr.fit(X_train, y_train)

y_train_pred_count = lr.predict(X_train)
y_val_pred_count = lr.predict(X_val)

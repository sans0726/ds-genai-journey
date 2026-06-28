import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier

# ------------------------
# LOAD DATA
# ------------------------
df = pd.read_csv("dataset/data.csv")

print("Original Shape:", df.shape)

# ------------------------
# CLEAN DATA
# ------------------------
df = df.drop_duplicates()

# remove extreme rare class (class 2)
df = df[df["severe flares"] != 2]

print("After Cleaning Shape:", df.shape)

print("\nTarget Distribution:")
print(df["severe flares"].value_counts())

# ------------------------
# FEATURES & TARGET
# ------------------------
X = df.drop("severe flares", axis=1)
y = df["severe flares"]

# encode categorical columns
X = pd.get_dummies(X, drop_first=True)

# ------------------------
# TRAIN-TEST SPLIT
# ------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTrain distribution:")
print(y_train.value_counts())

print("\nTest distribution:")
print(y_test.value_counts())

# ------------------------
# MODEL (XGBOOST)
# ------------------------
model = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.1,
    scale_pos_weight=10,   # handles imbalance
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

# train model
model.fit(X_train, y_train)

# ------------------------
# PREDICTION
# ------------------------
y_pred = model.predict(X_test)

# ------------------------
# EVALUATION
# ------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

import joblib

# Save trained model
joblib.dump(model, "solar_flare_model.pkl")

# Save feature names
joblib.dump(X.columns.tolist(), "feature_names.pkl")

print("\nModel and feature names saved successfully!")

print("\nModified Zurich Class:")
print(df["modified Zurich class"].unique())

print("\nLargest Spot Size:")
print(df["largest spot size"].unique())

print("\nSpot Distribution:")
print(df["spot distribution"].unique())

print(X.columns.tolist())
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE


def handle_missing(df):

    df = df.fillna(df.median(numeric_only=True))

    return df


def encode_features(df):

    df = pd.get_dummies(df, drop_first=True)

    return df


def scale_features(X):

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled


def handle_imbalance(X, y):

    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X, y)

    return X_res, y_res

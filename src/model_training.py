from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier


def train_models(X_train, y_train):

    models = {}

    models["Logistic Regression"] = LogisticRegression(max_iter=1000).fit(X_train, y_train)

    models["Random Forest"] = RandomForestClassifier().fit(X_train, y_train)

    models["XGBoost"] = XGBClassifier(use_label_encoder=False, eval_metric='logloss').fit(X_train, y_train)

    models["LightGBM"] = LGBMClassifier().fit(X_train, y_train)

    return models

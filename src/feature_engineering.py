import pandas as pd

def aggregate_bureau(bureau):

    bureau_agg = bureau.groupby("SK_ID_CURR").agg({
        "AMT_CREDIT_SUM": ["mean", "sum"],
        "AMT_CREDIT_SUM_DEBT": ["mean", "sum"]
    })

    bureau_agg.columns = ["_".join(col) for col in bureau_agg.columns]
    bureau_agg.reset_index(inplace=True)

    return bureau_agg


def merge_datasets(application, bureau_agg):

    df = application.merge(bureau_agg, on="SK_ID_CURR", how="left")

    return df


def create_features(df):

    df["CREDIT_INCOME_RATIO"] = df["AMT_CREDIT"] / (df["AMT_INCOME_TOTAL"] + 1)
    df["ANNUITY_INCOME_RATIO"] = df["AMT_ANNUITY"] / (df["AMT_INCOME_TOTAL"] + 1)

    return df

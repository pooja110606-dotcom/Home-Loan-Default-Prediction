from sklearn.model_selection import train_test_split


def split_data(df):

    X = df.drop("TARGET", axis=1)
    y = df["TARGET"]

    return X, y


def train_test_split_data(X, y):

    return train_test_split(X, y, test_size=0.2, random_state=42)

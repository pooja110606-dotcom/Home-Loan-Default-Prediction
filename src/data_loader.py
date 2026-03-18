import pandas as pd

def load_data():

    application = pd.read_csv("data/raw/application_train.csv")
    bureau = pd.read_csv("data/raw/bureau.csv")
    bureau_balance = pd.read_csv("data/raw/bureau_balance.csv")
    previous = pd.read_csv("data/raw/previous_application.csv")
    installments = pd.read_csv("data/raw/installments_payments.csv")
    credit = pd.read_csv("data/raw/credit_card_balance.csv")
    
    return application, bureau, bureau_balance, previous, installments, credit

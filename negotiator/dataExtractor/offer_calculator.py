import os
import pandas as pd

isFirst = True
df = None


def run_offer_calculator(customer_name):
    global isFirst, df
    if isFirst:
        isFirst = False
        cwd = os.getcwd()
        cwd = cwd.replace("\\dataExtractor", "")
        data_path = cwd + "\\data\\score.csv"
        df = pd.read_csv(data_path)

    customer = df[df["name"] == customer_name]
    score = customer["credit_score"]
    offer = int(score * 15)
    return offer


run_offer_calculator("F")

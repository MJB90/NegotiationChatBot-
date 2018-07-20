import os
import pandas as pd

isFirst = True
df = None

'''
The function below calculates offer based on the customers credit score and 
churn score and uses the scores.csv file 

parameter : customer's name

return value : the offer given to the customer
'''


def run_offer_calculator(customer_name):
    global isFirst, df
    if isFirst:
        isFirst = False
        cwd = os.getcwd()
        cwd = cwd.replace("\\dataExtractor", "")
        data_path = cwd + "\\data\\score.csv"
        df = pd.read_csv(data_path)

    customer = df[df["name"] == customer_name]
    credit_score = float(customer["credit_score"])
    churn_score = float(customer["churn_score"])

    if (credit_score > 0.7) and (churn_score == 1):
        offer = int(credit_score * 15)
    elif (credit_score < 0.7) and (credit_score > 0.5) and churn_score == 1:
        offer = int(0.6 * credit_score * 15)
    else:
        offer = 0
    return offer



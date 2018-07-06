import os
import pandas as pd


is_first = True

df = pd.DataFrame()


def get_data_frame():
    cwd = os.getcwd()
    data_path = cwd.replace("dataExtractor", "")
    data_path += "\\data\\" + "billing_data.csv"
    df = pd.read_csv(data_path)
    df = df.fillna(0)
    return df


def get_user_details(df, name):
    row = df[df['PRBA_SEQUENCE_NUMBER'] == name]

    total_bill = 0
    total_payment = 0
    for i in range(7):
        month = i + 1
        bill = "RANK" + str(month) + "_BILLED_TOTAL_AMT"
        payment = "RANK" + str(month) + "_PAYMENT_AMT"
        total_bill += row[bill]
        total_payment += row[payment]
    payment_left = float(total_bill - total_payment)
    if payment_left < 0:
        payment_left = 0
    return payment_left


def run_extract_info(name):
    global is_first, df
    if is_first:
        is_first = False
        df = get_data_frame()

    payment_left = get_user_details(df, name)
    return payment_left

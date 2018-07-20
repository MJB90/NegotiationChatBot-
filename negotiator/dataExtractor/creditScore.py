import os
import random
import pandas as pd

'''
The below code is used to calculate the credit score for each customer and 
store in score.csv file .This code also includes storing random churn scores in the score.csv file 
'''


def replace_dates_na(df):
    for i in range(7):
        month = i + 1
        date = "RANK" + str(month) + "_DD_PAY_DAY_GAP"
        temp = df[date].fillna(100)
        df[date] = temp.values

    return df


def get_average_paid(row):
    total_bill = 0
    total_payment = 0

    # print(row["PRBA_SEQUENCE_NUMBER"])
    # Calculating due amount for 7 months
    for i in range(7):
        month = i + 1
        bill = "RANK" + str(month) + "_BILLED_TOTAL_AMT"
        payment = "RANK" + str(month) + "_PAYMENT_AMT"
        total_bill += row[bill]
        total_payment += row[payment]

    # Payment left to be paid
    payment_ratio = float(total_payment/total_bill)
    payment_ratio = round(payment_ratio, 4)
    return payment_ratio


def get_average_minus3(row):
    total_minus_3 = 0
    total_due_date = 0
    total_plus_3 = 0
    total_plus_3_5 = 0
    total_plus_5_7 = 0
    total_plus_7 = 0
    total_no_pay = 0
    for i in range(7):
        month = i + 1
        date = "RANK" + str(month) + "_DD_PAY_DAY_GAP"
        if row[date] < 0:
            total_minus_3 += 1
        elif row[date] == 0:
            total_due_date += 1
        elif (row[date] > 0) and (row[date] <= 3):
            total_plus_3 += 1
        elif (row[date] > 3) and (row[date] <= 5):
            total_plus_3_5 += 1
        elif (row[date] > 5) and (row[date] <= 7):
            total_plus_5_7 += 1
        elif (row[date] > 7) and (row[date] != 100):
            total_plus_7 += 1
        else:
            total_no_pay += 1

    total_minus_3 = float(total_minus_3 / 7)
    total_minus_3 = round(total_minus_3, 4)

    total_due_date = float(total_due_date / 7)
    total_due_date = round(total_due_date, 4)

    total_plus_3 = float(total_plus_3 / 7)
    total_plus_3 = round(total_plus_3, 4)

    total_plus_3_5 = float(total_plus_3_5 / 7)
    total_plus_3_5 = round(total_plus_3_5, 4)

    total_plus_5_7 = float(total_plus_5_7 / 7)
    total_plus_5_7 = round(total_plus_5_7, 4)

    total_plus_7 = float(total_plus_7 / 7)
    total_plus_7 = round(total_plus_7, 4)

    total_no_pay = float(total_no_pay / 7)
    total_no_pay = round(total_no_pay, 4)

    return total_minus_3, total_due_date, total_plus_3, total_plus_3_5, total_plus_5_7, total_plus_7, total_no_pay


def find_credit(df):

    scores = []

    for index, row in df.iterrows():
        avg_paid = get_average_paid(row)
        total_minus_3, total_due_date, total_plus_3,\
        total_plus_3_5, total_plus_5_7, total_plus_7, \
        total_no_pay = get_average_minus3(row)
        avg_paid *= 3
        total_minus_3 *= 5
        total_due_date *= 3
        total_plus_3 *= -1
        total_plus_3_5 *= -2
        total_plus_5_7 *= -3
        total_plus_7 *= -4
        total_no_pay *= -5

        score = avg_paid + total_minus_3 + total_due_date + total_plus_3 + \
                total_plus_3_5 + total_plus_5_7 + total_plus_7 + \
                total_no_pay

        score = (score + 8)/16

        scores.append(score)

    return scores


def run_credit_score():

    scores_frame = pd.DataFrame()
    cwd = os.getcwd()
    cwd = cwd.replace("\\dataExtractor", "")
    data_path = cwd + "\\data\\billing_data.csv"
    df = pd.read_csv(data_path)
    df = df.drop_duplicates()
    df = replace_dates_na(df)
    df = df.fillna(0)
    credit_score = find_credit(df)
    scores_frame['name'] = df["PRBA_SEQUENCE_NUMBER"]
    scores_frame['credit_score'] = credit_score

    # Generate random churn scores
    random_churn = []
    for i in range(len(credit_score)):
        random_churn.append(random.randrange(0, 2, 1))

    scores_frame['churn_score'] = random_churn
    saving_path = cwd + "\\data\\score.csv"
    scores_frame.to_csv(saving_path, index=False)


run_credit_score()

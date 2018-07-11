from decideResponse import affirmative_or_negative
from decideResponse import response_tree
import datetime
import os
import os.path
import pandas as pd

is_first = True
root = None
normal_conversation = 0
prev_time = 1
previous_time = 0
offer = 0


def save_data(customer_name, offer):
    today = str(datetime.date.today())
    cwd = os.getcwd()
    cwd = cwd.replace("\\dataExtractor", "")
    data_path = cwd + "\\data\\" + customer_name + ".csv"

    if os.path.isfile(data_path):
        df = pd.read_csv(data_path)
        df.loc[-1] = [customer_name, today, offer]
        df.index = df.index + 1
        df.to_csv(data_path, index=False)
    else:
        df = pd.DataFrame(columns=['customer', 'date', 'offer'])
        df.loc[-1] = [customer_name, today, offer]
        df.index = df.index + 1
        df.to_csv(data_path, index=False)


def response(msg, payment, customer_name):
    global is_first, root, normal_conversation, prev_time, previous_time, offer
    if is_first:
        is_first = False
        root, offer = response_tree.create_tree(payment, customer_name)
        return_msg = root.data
    else:
        affirmative = affirmative_or_negative.check_affirmation(msg)

        if affirmative == 'YES' and normal_conversation == 0:

            if root.data.find("We are happy to give you an offer of"):
                save_data(customer_name, offer)

            root = root.child['yes']

            return_msg = root.data
        elif affirmative == 'NO' and normal_conversation == 0:
            root = root.child['no']
            return_msg = root.data
        else:
            normal_conversation = 1
            return_msg = ""
            if prev_time:
                prev_time = 0
                dt = datetime.now()
                previous_time = dt.second

            dt = datetime.now()
            if prev_time == 0 and abs(dt.second - previous_time) > 15:
                prev_time = 1
                normal_conversation = 0
                return_msg = "I am sorry but i was here for something else!"
                return_msg += root.data

    return return_msg






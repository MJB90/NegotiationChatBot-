import os
import pandas as pd


def assign_names(df, data_path):
    speaker_number = 'A'
    speaker_count = 0
    name_list = []
    clearer = ''
    incrementor = 0
    for i in range(len(df)):
        var_z = str(chr(ord(speaker_number) + speaker_count))
        to_insert = clearer + var_z

        name_list.append(to_insert)
        speaker_count += 1
        if var_z == 'Z':
            clearer = name_list[incrementor]
            incrementor += 1
            speaker_number = 'A'
            speaker_count = 0

    df['PRBA_SEQUENCE_NUMBER'] = name_list
    df.to_csv(data_path, index=False)


def run_extractor():
    cwd = os.getcwd()
    data_path = cwd + "\\data\\billing_data.csv"
    df = pd.read_csv(data_path)
    df = df.drop_duplicates()

    # Assign each customer a name instead of an id
    assign_names(df, data_path)









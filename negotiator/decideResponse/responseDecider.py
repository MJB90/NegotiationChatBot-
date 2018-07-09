import os

is_first = True
pos_response = []
neg_response = []


def extract_responses():
    global pos_response, neg_response
    cwd = os.getcwd()
    cwd = cwd.replace("decideResponse", "")
    data_pos = cwd + "\\data\\positive_responses.txt"
    data_neg = cwd + "\\data\\negative_responses.txt"
    file_pos = open(data_pos, 'r')
    file_neg = open(data_neg, 'r')

    for line in file_pos:
        pos_response.append(str(line))

    for line in file_neg:
        neg_response.append(str(line))


def response(msg, payment):
    global is_first, pos_response, neg_response
    return_msg = ""
    if is_first:
        extract_responses()
        is_first = False
        return_msg = "You have a due of " + str(payment) + " rupees."
        return_msg += "Are you willing to pay the amount for continued services!"

    return return_msg


extract_responses()

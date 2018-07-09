from decideResponse import affirmative_or_negative
from decideResponse import response_tree
from datetime import datetime

is_first = True
root = None
normal_conversation = 0
prev_time = 1
previous_time = 0


def response(msg, payment):
    global is_first, root, normal_conversation, prev_time, previous_time
    if is_first:
        is_first = False
        root = response_tree.create_tree(payment)
        return_msg = root.data
    else:
        affirmative = affirmative_or_negative.check_affirmation(msg)

        if affirmative == 'YES' and normal_conversation == 0:
            root = root.right
            return_msg = root.data
        elif affirmative == 'NO' and normal_conversation == 0:
            root = root.left
            return_msg = root.data
        else:
            normal_conversation = 1
            return_msg = ""
            if prev_time:
                prev_time = 0
                dt = datetime.now()
                previous_time = dt.second

            dt = datetime.now()
            if prev_time == 0 and abs(dt.second - previous_time) > 10:
                prev_time = 1
                normal_conversation = 0
                return_msg = "I am sorry but i was here for something else!"
                return_msg += root.data

    return return_msg






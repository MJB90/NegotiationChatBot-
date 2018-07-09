from decideResponse import affirmative_or_negative
from decideResponse import response_tree

is_first = True
root = None


def response(msg, payment):
    global is_first, root
    if is_first:
        is_first = False
        root = response_tree.create_tree(payment)
        return_msg = root.data
    else:
        affirmative = affirmative_or_negative.check_affirmation(msg)

        if affirmative == 'YES':
            root = root.right
            return_msg = root.data
        else:
            root = root.left
            return_msg = root.data
    return return_msg






class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def create_tree(payment):
    msg = "You have a due of " + str(payment) + " rupees."
    msg += "Are you willing to pay the amount for continued services!"

    root = Tree()
    root.data = msg

    root.left = Tree()
    root.left.data = "Would you mind reconsidering your decision for an offer?"

    root.right = Tree()
    root.right.data = "Would you like to make the payment now ?"

    root.right.left = Tree()
    root.right.left.data = "Thanks!Please make your payment soon!"

    root.right.right = Tree()
    root.right.right.data = "Thank you very much.Here is the link for payment :https:\\www.payment.com"

    root.left.right = Tree()
    root.left.right.data = "We are happy to give you an offer of 15%! " \
                           "Would you like to make the payment now ?"

    root.left.right.right = root.right.right
    root.left.right.left = root.right.left

    return root



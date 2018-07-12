from dataExtractor import offer_calculator


class Tree(object):
    def __init__(self):
        self.child = {}
        self.data = None


def create_tree(payment, customer_name):
    msg = "You have a due of " + str(payment) + " rupees."
    msg += "Are you willing to pay the amount for continued services!"

    root = Tree()
    root.data = msg

    root.child['no'] = Tree()
    root.child['no'].data = "Would you mind reconsidering your " \
                            "decision for an offer if there is any?"

    root.child['yes'] = Tree()
    root.child['yes'].data = "Would you like to make the payment now ?"

    root.child['yes'].child['no'] = Tree()
    root.child['yes'].child['no'].data = "Thanks!Please make your payment soon!"

    root.child['yes'].child['yes'] = Tree()
    root.child['yes'].child['yes'].data = "Thank you very much.Here is the link for payment :https:\\www.payment.com"

    root.child['no'].child['yes'] = Tree()
    offer = offer_calculator.run_offer_calculator(customer_name)
    if offer > 0:
        root.child['no'].child['yes'].data = "We are happy to give you an offer of " + str(offer) + \
                                             "% Would you like to make the payment now ?"
    else:
        root.child['no'].child['yes'].data = "Sorry currently we don't have any offer for you." \
                                             "Would you like to make the payment now ?"

    root.child['no'].child['yes'].child['more'] = Tree()
    root.child['no'].child['yes'].child['more'].data = "Sorry but we don't have any better offers!" \
                                                       "Would you like to make the payment now ?"

    root.child['no'].child['yes'].child['more'].child['yes'] = root.child['yes'].child['yes']
    root.child['no'].child['yes'].child['more'].child['yes'] = root.child['yes'].child['no']

    root.child['no'].child['yes'].child['yes'] = root.child['yes'].child['yes']
    root.child['no'].child['yes'].child['no'] = root.child['yes'].child['no']

    return root, offer



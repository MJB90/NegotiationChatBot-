from decideResponse import sentimentCalculator

pos_word = ['yes', 'okay', 'okay!', 'will', 'might']
neg_words = ['no', 'sorry', "can't", "don't"]
more_offer = ['more', 'offer', 'offers', 'better']


def check_affirmation(sentence):
    sentiment = sentimentCalculator.check_sentiment("sentence")
    affirmative = -2
    sentence = sentence.lower()
    words = sentence.split()
    want_offer = 0

    # if Asking for better offers return MORE
    for word in words:
        if word in pos_word:
            affirmative = 1
            break
        elif word in neg_words:
            affirmative = 0
            break

    for word in words:
        if word in more_offer:
            want_offer += 1

    if want_offer == 2:
        affirmative = 2

    if affirmative == -2:
        return 'NOR'
    elif affirmative == 1:
        return 'YES'
    elif affirmative == 2:
        return 'MORE'

    return 'NO'

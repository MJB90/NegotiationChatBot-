from decideResponse import sentimentCalculator

pos_word = ['yes', 'okay', 'okay!', 'will do', 'might']
neg_words = ['no', 'sorry', "can't", "don't"]


def check_affirmation(sentence):
    sentiment = sentimentCalculator.check_sentiment("sentence")
    affirmative = -2
    sentence = sentence.lower()
    words = sentence.split()

    # if Asking for better offers return MORE
    for word in words:
        if word in pos_word:
            affirmative = 1
            break
        elif word in neg_words:
            affirmative = 0
            break

    if affirmative == -2:
        return 'NOR'
    elif affirmative == 1:
        return 'YES'

    return 'NO'

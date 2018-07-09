from nltk.sentiment.vader import SentimentIntensityAnalyzer


def check_sentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    if ss['neg'] > ss['pos']:
        return 'NO'
    else:
        return 'YES'


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

class Snenerizer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analizza(self, text):
        score = self.sia.polarity_scores(text)['compound']
        return score
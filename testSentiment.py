import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Crea un oggetto SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Analizza il sentimento del testo
text = "This film is so good"
score = sia.polarity_scores(text)['compound']

print("punteggio", score)
# Determina se il testo è positivo, negativo o neutro
if score > 0.03:
    print("Il testo è positivo.")
elif score < -0.03:
    print("Il testo è negativo.")
else:
    print("Il testo è neutro.")
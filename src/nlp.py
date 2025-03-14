import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download("punkt")
nltk.download("stopwords")

def process_text(text):
    if not text:
        return []

    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("spanish"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    
    return tokens


import numpy as np
import pandas as pd
import nltk  # Toolkit to peform natural language processing

nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords  # Stopwords corpus
from nltk.stem import WordNetLemmatizer

train_data = pd.read_csv("../../data/interim/train_data.csv")
test_data = pd.read_csv("../../data/interim/test_data.csv")

stop_words = stopwords.words("english")
stop_words.append("movie")


def clean_data(text):
    """Cleans text data containing punctuation, stopwords, emoticons, lemmas, and non-ascii characters."""

    # Removing punctuation, stopwords, and emoticons
    text = re.sub("<[^>]*>", "", text)
    text = re.sub(r"[0-9]", "", text)
    emoticons = re.findall("(?::|;|=)(?:-)", text)
    text = re.sub("[\W]+", " ", text.lower()) + " ".join(emoticons).replace("-", "")
    rm_words = [w for w in text.split() if w.lower() not in stop_words]

    # Performing Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemma_words = [lemmatizer.lemmatize(word) for word in rm_words]

    # Removing non-ascii characters
    non_ascii_words = list()
    for word in lemma_words:
        for character in word:
            if ord(character) > 128:
                word = word.replace(character, "")
        non_ascii_words.append(word)

    # Removing empty string values from the list
    non_ascii_words = list(filter(None, non_ascii_words))

    return " ".join(non_ascii_words)


train_data["tweet"] = train_data["tweet"].apply(clean_data)
test_data["tweet"] = test_data["tweet"].apply(clean_data)

train_data.to_csv("../../data/processed/train_data.csv")
test_data.to_csv("../../data/processed/test_data.csv")

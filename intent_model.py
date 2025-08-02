import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt_tab')

data = pd.read_csv('support_data.csv')

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return ' '.join(tokens)

data['text'] = data['text'].apply(preprocess)

vectorizer = CountVectorizer()
X=vectorizer.fit_transform(data['text'])

model = MultinomialNB()
model.fit(X, data['intent'])

with open('intent_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
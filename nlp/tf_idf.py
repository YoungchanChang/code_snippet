import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import mecab

mecab = mecab.MeCab()
def tokenizer(text):
    nouns = mecab.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]

count_vectorizer = CountVectorizer()
news = pd.read_csv("./sample_data.csv")
document_term_matrix = count_vectorizer.fit_transform(news['text'])

tf = pd.DataFrame(document_term_matrix.toarray(), columns=count_vectorizer.get_feature_names())


zzz = 3

import numpy as np

D = len(tf)
df = tf.astype(bool).sum(axis=0)
idf = np.log((D+1) / (df+1)) + 1
from sklearn.feature_extraction.text import TfidfVectorizer

kkk = 3


def tokenizer(text):
    nouns = mecab.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]


tfidf_vectorizer = TfidfVectorizer(tokenizer=tokenizer)
tfidf_matrix = tfidf_vectorizer.fit_transform(news['text'])


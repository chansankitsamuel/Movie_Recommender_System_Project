import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# read data from csv
indata = pd.read_csv("processed_data/indata.csv")

# reduce words to their stumps or roots
ps = PorterStemmer()
def stems(text):
    l = []
    for i in text.split():
        l.append(ps.stem(i))
    return " ".join(l)
indata.loc["all"] = indata["all"].apply(stems)

# extract text features
cv = CountVectorizer(max_features=5000, stop_words="english")
vector = cv.fit_transform(indata["all"].values.astype('U')).toarray()  # vectorize text
similarity = cosine_similarity(vector)  # obtain similarity

# export result to csv
np.save('processed_data/embeddings.npy', similarity)

import pandas as pd
import numpy as np


# read data from csv
data = pd.read_csv("processed_data/data.csv")
similarity = np.load('processed_data/embeddings.npy')

# get movie title by id
def get_title(id):
    return data.loc[data["id"] == id]["title"].to_string(index=False)

# get movie id by title
def get_id(title):
    return data.loc[data["title"] == title]["id"].to_string(index=False)

# recommand movie id by id
def recommend(id):
    index = data[data["id"] == id].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x:x[1], reverse=True)
    results = []
    for i in distances[1:6]:
        results.append(int(data.iloc[i[0]]["id"]))
    return results



print(recommend(49026))
# print(get_id("The Dark Knight Rises"))
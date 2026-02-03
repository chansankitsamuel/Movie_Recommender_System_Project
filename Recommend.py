import pandas as pd
import numpy as np
import requests


# read data from csv
data = pd.read_csv("processed_data/data.csv")
similarity = np.load('processed_data/embeddings.npy')

# # get movie list
# def get_movie_list():
#     return [(row.id, row.title) for row in data.itertuples(index=False)]

# get movie name list
def get_movie_name_list():
    return data["title"]

# get movie title by id
def get_title(id):
    return data.loc[data["id"] == id]["title"].to_string(index=False)

# get movie id by title
def get_id(title):
    return int(data.loc[data["title"] == title]["id"].to_string(index=False))

# recommand movie id by id
def recommend(id):
    index = data[data["id"] == id].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x:x[1], reverse=True)
    results = []
    for i in distances[1:6]:
        results.append(int(data.iloc[i[0]]["id"]))
    return results

# get movie poster url by id
def get_movie_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/images"
    headers = {
        "accept": "application/json", 
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZGM4NjJhMDcwZWFlZDA4NjQ5OGNhNTdjNGM1NGU0NCIsIm5iZiI6MTc3MDEwODc3OC4xMzYsInN1YiI6IjY5ODFiNzZhMjA4YWQzM2E5YjRjOTY5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NvPzOdE5Zbr92dyklxXfCV67j3U6PRX1aMwtm8iCa6Q"
    }
    response = requests.get(url, headers=headers).json()
    poster_path = "http://image.tmdb.org/t/p/w500" + response["posters"][0]["file_path"]
    return poster_path

import os
import ast

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read data from csv
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# merge 2 tables and simplify it
credits.rename(columns={'movie_id':'id'}, inplace=True)
data = pd.merge(movies, credits, on=["id", "title"])
data = data[["id", "title", "overview", "genres", "keywords", "cast", "crew"]]
data.dropna(inplace=True)

# convert columns into readable format
def convert(s): 
    l = []
    for i in ast.literal_eval(s):
        l.append(i["name"])
    return l
data["genres"] = data["genres"].apply(convert)
data["keywords"] = data["keywords"].apply(convert)
data["cast"] = data["cast"].apply(convert)
def fetch_director(s):
    l = []
    for i in ast.literal_eval(s):
        if i["job"] == "Director":
            return i["name"]
data["crew"] = data["crew"].apply(fetch_director)
data.rename(columns={'crew':'director'}, inplace=True)
data["overview"] = data["overview"].apply(lambda s:s.split())


# debug zone
print(data.head(1)['overview'])
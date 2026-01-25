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

# convert columns into format suitable for generating embeddings
def convert(s): 
    l = []
    for i in ast.literal_eval(s):
        l.append(i["name"])
    return l
data["genres"] = data["genres"].apply(convert)
data["keywords"] = data["keywords"].apply(convert).apply(str)
def convert_cast(s): 
    l = []
    counter = 0
    for i in ast.literal_eval(s):
        l.append(i["name"])
        counter += 1
        if counter > 5:
            break
    return l
data["cast"] = data["cast"].apply(convert_cast)
def fetch_director(s):
    l = []
    for i in ast.literal_eval(s):
        if i["job"] == "Director":
            return i["name"]
data["crew"] = data["crew"].apply(fetch_director)
data.rename(columns={'crew':'director'}, inplace=True)
data["overview"] = data["overview"].apply(lambda s:str(s).split()).apply(str)
def remove_space(s):
    l = []
    for i in str(s):
        l.append(i.replace(" ", ""))
    return "".join(l)
data["genres"] = data["genres"].apply(remove_space)
data["cast"] = data["cast"].apply(remove_space)
data["director"] = data["director"].apply(remove_space)

# merge all columns in to data["all"]
data["overview"] = data["overview"].apply(lambda x: ast.literal_eval(x.replace('][', '],[')))
data["genres"] = data["genres"].apply(lambda x: ast.literal_eval(x.replace('][', '],[')))
data["keywords"] = data["keywords"].apply(lambda x: ast.literal_eval(x.replace('][', '],[')))
data["cast"] = data["cast"].apply(lambda x: ast.literal_eval(x.replace('][', '],[')))
data["director"] = data["director"].apply(lambda x: ast.literal_eval(f"[{repr(x)}]"))
data["all"] = data[["genres", "keywords", "overview", "director", "cast"]].apply(lambda x: sum(x.tolist(), []), axis=1).apply(lambda x: ' '.join(x)).apply(lambda x: str(x).lower())

# create a new dataframe 'indata' for generating embeddings
indata = data[["id", "title", "all"]]


# debug zone
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option("display.max_colwidth", None)
# print(data.head(1))
# print(indata.dtypes)
print(indata.head(1)["all"])

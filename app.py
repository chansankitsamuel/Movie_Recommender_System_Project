import subprocess
import streamlit as st
from Recommend import *

# uncomment the 2 lines below to upate processed_data
# subprocess.run(["python3", "DataProcess.py"])
# subprocess.run(["python3", "GenerateEmbeddings.py"])

movie_list = get_movie_name_list()


st.header("Movies Recommendation System")

selected_movie = st.selectbox("Select a movie", movie_list)
if st.button("Show Recommendation"):
    recommended_movie_ids = recommend(get_id(selected_movie))
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(get_movie_poster(recommended_movie_ids[0]))
        st.text(get_title(recommended_movie_ids[0]))
    with col2:
        st.image(get_movie_poster(recommended_movie_ids[1]))
        st.text(get_title(recommended_movie_ids[1]))
    with col3:
        st.image(get_movie_poster(recommended_movie_ids[2]))
        st.text(get_title(recommended_movie_ids[2]))
    with col4:
        st.image(get_movie_poster(recommended_movie_ids[3]))
        st.text(get_title(recommended_movie_ids[3]))
    with col5:
        st.image(get_movie_poster(recommended_movie_ids[4]))
        st.text(get_title(recommended_movie_ids[4]))
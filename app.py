import streamlit as st
import pickle
import pandas as pd
import os
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8766797c0c11865ea6cb08044d1a9fac&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies=[]
    recommended_movies_poster=[]
    
    for i in movie_list:
       movie_id=movies.iloc[i[0]].movie_id
       recommend_movies.append(movies.iloc[i[0]].title)
       recommended_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies ,recommended_movies_poster  

os.chdir('E:/ML/myenv')

similarity=pickle.load(open('similarity.pkl', 'rb'))
# Load the pickle file

try:
    movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_list)
except FileNotFoundError:
    st.error("Error: 'movie_dict.pkl' file not found now.")

st.title('Movie Recommender System') 

Selected_Movie_Name = st.selectbox(
    'How would you like to watch?',
     movies['title'].values)

if st.button("Recommend", type="primary"):

    recommendation,posters =recommend(Selected_Movie_Name)

    col1, col2, col3 ,col4,col5 = st.columns(5)

    with col1:
        st.text(recommendation[0])
        st.image(posters[0])

    with col2:
        st.text(recommendation[1])
        st.image(posters[1])

    with col3:
        st.text(recommendation[2])
        st.image(posters[2])
    
    with col4:
        st.text(recommendation[3])
        st.image(posters[3])
    
    with col5:
        st.text(recommendation[4])
        st.image(posters[4])


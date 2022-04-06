import streamlit as st
import pickle
import requests


# fetching movie posters
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return full_path












# Recommend function for movie recommend

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters





movies = pickle.load(open('movies_list.pkl','rb'))
movies_list = movies['title'].values

# print(movies_list)

# similarity
similarity = pickle.load(open('similarity.pkl','rb'))



#title for model
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie from the dropdown below', movies_list)


# button for recommend

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.write(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.write(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.write(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.write(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

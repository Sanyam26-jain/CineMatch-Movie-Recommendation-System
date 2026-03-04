import streamlit as st
from recommender import recommend

st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎬")
st.title("🎬 Movie Recommendation System")
st.write("Type a movie name and get 5 similar movie suggestions!")

movie_input = st.text_input("Enter a movie name:", placeholder="e.g. Avatar, Inception, Titanic")

if st.button("Recommend"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        results = recommend(movie_input)
        if results is None:
            st.error(f"Movie '{movie_input}' not found. Try another title.")
        else:
            st.success(f"Movies similar to **{movie_input}**:")
            for i, movie in enumerate(results, 1):
                st.write(f"{i}. {movie}")
# 🎬 CineMatch - Movie Recommendation System
## 🚀 Live Demo

👉 [Try CineMatch Live](https://cinematch-sanyam.streamlit.app/)

CineMatch is a content-based movie recommendation system built with Python and Machine Learning. It recommends five movies similar to a movie entered by the user.

The application uses movie metadata such as overview, genres, keywords, cast, and director to identify movies with similar content.

## 🚀 Features

- Search for a movie by title
- Generate 5 similar movie recommendations
- Content-based recommendation approach
- TF-IDF based text feature extraction
- Cosine Similarity for measuring movie similarity
- Interactive Streamlit web interface
- Partial movie-title matching
- Clean and responsive user interface

## 🧠 How It Works

The recommendation pipeline works in the following steps:

1. Movie metadata is loaded from the TMDB dataset.
2. Important information such as overview, genres, keywords, cast, and director is extracted.
3. These features are combined into a single text representation for each movie.
4. TF-IDF Vectorization converts the text data into numerical vectors.
5. Cosine Similarity measures the similarity between the selected movie and other movies.
6. The five most similar movies are returned as recommendations.

### Recommendation Pipeline

```text
Movie Input
     ↓
Movie Metadata
     ↓
Data Preprocessing
     ↓
Feature Combination
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Top 5 Similar Movies
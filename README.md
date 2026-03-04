# Movie Recommendation System

A content-based movie recommendation engine built with Python and Machine Learning. The system recommends 5 similar movies based on any movie you search, covering Hollywood, Bollywood, Tollywood, and Kollywood films.

## How It Works

The system uses Natural Language Processing and Machine Learning techniques to find similar movies:

1. Movie data (genres, keywords, cast, director) is converted into numerical vectors using TF-IDF Vectorization
2. Cosine Similarity is calculated between the searched movie and all other movies in the dataset
3. The top 5 most similar movies are returned as recommendations

## Tech Stack

- **Python** - Core programming language
- **Pandas** - Data loading and preprocessing
- **Scikit-learn** - TF-IDF Vectorization and Cosine Similarity
- **Streamlit** - Web application interface

## Dataset

The model is trained on 48,987 movies combined from three datasets:

- TMDB 5000 Movies Dataset (Hollywood)
- Indian Movies Dataset (Bollywood, Tollywood, Kollywood, Malayalam)
- Hollywood and Bollywood Movies Dataset

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/AdapakaGunaSekhar004/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

Install dependencies:

```bash
pip install pandas scikit-learn streamlit
```

Download the datasets and place them in the project folder:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv
- All_Movies1.csv
- indian movies.csv

Run the application:

```bash
streamlit run app.py
```

## Usage

1. Open the app in your browser at `http://localhost:8501`
2. Type a movie name in the search box (e.g. Avatar, Dangal, Baahubali: The Beginning)
3. Click the Recommend button
4. View 5 similar movie recommendations

## Project Structure

```
Movie-Recommendation-System/
├── app.py              # Streamlit web application
├── recommender.py      # ML logic and recommendation engine
└── README.md           # Project documentation
```

## Key Concepts Demonstrated

- Content-based filtering using machine learning
- TF-IDF (Term Frequency - Inverse Document Frequency) vectorization
- Cosine similarity for measuring movie likeness
- Data preprocessing and merging multiple datasets
- Building and deploying an interactive web application with Python
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ── 1. TMDB dataset ─────────────────────────────────────────────

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

credits.columns = ["id", "title", "cast", "crew"]

movies = movies.merge(
    credits[["id", "cast", "crew"]],
    on="id"
)


def extract_names(text, max_items=5):
    try:
        items = ast.literal_eval(text)
        return " ".join(
            item["name"] for item in items[:max_items]
        )
    except:
        return ""


def get_director(crew_text):
    try:
        crew = ast.literal_eval(crew_text)

        for person in crew:
            if person["job"] == "Director":
                return person["name"]

        return ""
    except:
        return ""


movies["genres_clean"] = movies["genres"].apply(extract_names)

movies["keywords_clean"] = movies["keywords"].apply(
    lambda x: extract_names(x, 10)
)

movies["cast_clean"] = movies["cast"].apply(
    lambda x: extract_names(x, 5)
)

movies["director"] = movies["crew"].apply(get_director)

movies["overview_clean"] = movies["overview"].fillna("")


# Combine important movie features
movies["content"] = (
    movies["overview_clean"] + " " +
    movies["genres_clean"] + " " +
    movies["genres_clean"] + " " +
    movies["keywords_clean"] + " " +
    movies["cast_clean"] + " " +
    movies["director"]
)


tmdb_df = movies[
    ["title", "content"]
].dropna().copy()


# ── 2. Use TMDB dataset for recommendations ────────────────────

combined_df = tmdb_df.copy()

# Remove duplicate titles
combined_df = combined_df.drop_duplicates(
    subset="title",
    keep="first"
)

combined_df = combined_df.dropna()
combined_df = combined_df.reset_index(drop=True)

print(f"✅ Total movies loaded: {len(combined_df)}")


# ── 3. Build TF-IDF matrix ─────────────────────────────────────

tfidf = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    min_df=2
)

matrix = tfidf.fit_transform(combined_df["content"])

indices = pd.Series(
    combined_df.index,
    index=combined_df["title"].str.lower()
)

print("✅ TF-IDF matrix built successfully!")


# ── 4. Recommendation function ─────────────────────────────────

def recommend(movie_title):
    movie_title = movie_title.lower().strip()

    # Exact title match
    if movie_title not in indices:
        # Try partial match
        matches = [
            title for title in indices.index
            if movie_title in title
        ]

        if matches:
            movie_title = matches[0]
        else:
            return None

    idx = indices[movie_title]

    # Calculate similarity
    movie_vector = matrix[idx]
    scores = cosine_similarity(
        movie_vector,
        matrix
    ).flatten()

    # Get top 5 similar movies
    top_indices = scores.argsort()[::-1][1:6]

    recommendations = []

    for i in top_indices:
        movie_name = combined_df["title"].iloc[i]
        similarity_score = scores[i]

        recommendations.append(
            (movie_name, similarity_score)
        )

    return recommendations
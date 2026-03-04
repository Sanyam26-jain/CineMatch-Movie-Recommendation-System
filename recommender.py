import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ── 1. TMDB dataset (Hollywood with cast/crew) ──────────────────────────
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
credits.columns = ["id", "title", "cast", "crew"]
movies = movies.merge(credits[["id", "cast", "crew"]], on="id")

def extract_names(text, max=5):
    try:
        items = ast.literal_eval(text)
        return " ".join([i["name"].replace(" ", "") for i in items[:max]])
    except:
        return ""

def get_director(crew_text):
    try:
        crew = ast.literal_eval(crew_text)
        for person in crew:
            if person["job"] == "Director":
                return person["name"].replace(" ", "")
        return ""
    except:
        return ""

movies["genres_clean"]   = movies["genres"].apply(extract_names)
movies["keywords_clean"] = movies["keywords"].apply(extract_names)
movies["cast_clean"]     = movies["cast"].apply(lambda x: extract_names(x, 3))
movies["director"]       = movies["crew"].apply(get_director)
movies["content"] = (
    movies["genres_clean"] + " " +
    movies["keywords_clean"] + " " +
    movies["cast_clean"] + " " +
    movies["director"]
)
tmdb_df = movies[["title", "content"]].dropna()

# ── 2. All_Movies1 dataset (Hindi + English with overview) ──────────────
all_movies = pd.read_csv("All_Movies1.csv", engine="python", on_bad_lines="skip")
all_movies = all_movies[["title", "genres", "overview", "original_language"]].dropna()
all_movies["content"] = (
    all_movies["overview"].fillna("") + " " +
    all_movies["genres"].fillna("") + " " +
    all_movies["original_language"].fillna("")
)
all_movies_df = all_movies[["title", "content"]].dropna()

# ── 3. Indian movies dataset (Telugu, Tamil, Hindi, Malayalam etc.) ──────
indian = pd.read_csv("indian movies.csv", engine="python", on_bad_lines="skip")
indian = indian[["Movie Name", "Genre", "Language"]].dropna()
indian.rename(columns={"Movie Name": "title"}, inplace=True)
indian["content"] = (
    indian["Genre"].fillna("") + " " +
    indian["Language"].fillna("")
)
indian_df = indian[["title", "content"]].dropna()

# ── 4. Combine all 3 datasets ────────────────────────────────────────────
combined_df = pd.concat([tmdb_df, all_movies_df, indian_df], ignore_index=True)

# Remove duplicate titles (keep first occurrence)
combined_df = combined_df.drop_duplicates(subset="title", keep="first")
combined_df = combined_df.dropna()
combined_df = combined_df.reset_index(drop=True)

print(f"✅ Total movies loaded: {len(combined_df)}")

# ── 5. Build TF-IDF matrix (no full similarity matrix) ───────────────────
tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(combined_df["content"])
indices = pd.Series(combined_df.index, index=combined_df["title"].str.lower())

print("✅ TF-IDF matrix built successfully!")

# ── 6. Recommend function (computes similarity only for 1 movie) ──────────
def recommend(movie_title):
    movie_title = movie_title.lower().strip()
    if movie_title not in indices:
        # Try partial match
        matches = [t for t in indices.index if movie_title in t]
        if matches:
            movie_title = matches[0]
        else:
            return None
    idx = indices[movie_title]
    # Only compute similarity for this ONE movie (not all 48k!)
    movie_vector = matrix[idx]
    scores = cosine_similarity(movie_vector, matrix).flatten()
    top_indices = scores.argsort()[::-1][1:6]
    return combined_df["title"].iloc[top_indices].tolist()
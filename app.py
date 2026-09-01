import streamlit as st
from recommender import recommend


# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="centered"
)


# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────

st.markdown(
    """
    <style>

    /* Main app background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f0c29 0%,
            #302b63 50%,
            #24243e 100%
        );
    }

    /* Main content width */
    .block-container {
        max-width: 850px;
        padding-top: 4rem;
        padding-bottom: 4rem;
    }

    /* Main heading */
    .main-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #c8c8d8;
        margin-bottom: 35px;
    }

    /* Search box label */
    .search-label {
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 8px;
    }

    /* Recommendation card */
    .movie-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 18px 22px;
        margin: 12px 0;
        backdrop-filter: blur(10px);
        transition: 0.3s;
    }

    .movie-card:hover {
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.12);
    }

    .movie-number {
        font-size: 16px;
        color: #a8a8c8;
        font-weight: 600;
    }

    .movie-name {
        font-size: 23px;
        font-weight: 700;
        margin-top: 4px;
    }

    /* Result heading */
    .result-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #aaaabd;
        font-size: 14px;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────

st.markdown(
    '<div class="main-title">🎬 CineMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to your favorite films using '
    'content-based recommendation.'
    '</div>',
    unsafe_allow_html=True
)


# ─────────────────────────────────────────────
# SEARCH SECTION
# ─────────────────────────────────────────────

st.markdown(
    '<div class="search-label">🔎 Search for a movie</div>',
    unsafe_allow_html=True
)

movie_input = st.text_input(
    "",
    placeholder="Try: Avatar, Inception, Titanic...",
    label_visibility="collapsed"
)


# ─────────────────────────────────────────────
# RECOMMEND BUTTON
# ─────────────────────────────────────────────

if st.button("✨ Find Similar Movies", use_container_width=True):

    if movie_input.strip() == "":
        st.warning("Please enter a movie name first.")

    else:
        results = recommend(movie_input)

        if results is None:

            st.error(
                f"Movie '{movie_input}' was not found. "
                "Try another movie title."
            )

        else:

            st.markdown(
                f'<div class="result-title">'
                f'🍿 Movies similar to "{movie_input}"'
                f'</div>',
                unsafe_allow_html=True
            )

            for i, movie in enumerate(results, 1):

                st.markdown(
                    f"""
                    <div class="movie-card">
                        <div class="movie-number">
                            Recommendation #{i}
                        </div>
                        <div class="movie-name">
                            🎬 {movie}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────

st.markdown(
    '<div class="footer">'
    'Powered by TF-IDF & Cosine Similarity • CineMatch'
    '</div>',
    unsafe_allow_html=True
)
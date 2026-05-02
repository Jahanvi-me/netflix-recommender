import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# 📂 Load & preprocess data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/titles.csv")
    credits = pd.read_csv("data/credits.csv")

    df = df.merge(credits, on="id", how="left")

    df = df.drop(columns=[
        'seasons','age_certification','person_id','imdb_id','character'
    ], errors='ignore')

    df = df.groupby('id').agg({
        'title': 'first',
        'type': 'first',
        'description': 'first',
        'release_year': 'first',
        'genres': 'first',
        'imdb_score': 'first',
        'imdb_votes': 'first',
        'tmdb_popularity': 'first',
        'tmdb_score': 'first',
        'name': lambda x: list(x.dropna())
    }).reset_index()

    df['name'] = df['name'].apply(lambda x: ' '.join(x))
    df['description'] = df['description'].fillna('')
    df['genres'] = df['genres'].fillna('').astype(str)

    df['imdb_score'] = df['imdb_score'].fillna(df['imdb_score'].mean())

    df['combined'] = df['genres'] + " " + df['description'] + " " + df['name']

    return df


# -----------------------------
# 🤖 Build similarity model
# -----------------------------
@st.cache_data
def build_model(df):
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['combined'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity


# -----------------------------
# 🎯 Recommendation function
# -----------------------------
def recommend(title, df, similarity):
    matches = df[df['title'] == title]

    if matches.empty:
        return pd.DataFrame()

    idx = matches.index[0]
    selected_type = df.iloc[idx]['type']

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in scores[1:]:
        if df.iloc[i[0]]['type'] == selected_type:
            recommendations.append(i)
        if len(recommendations) == 10:
            break

    return df.iloc[[i[0] for i in recommendations]][['title', 'imdb_score']]


# -----------------------------
# 🤖 AI Explanation (Optional - Disabled)
# -----------------------------
# This feature can be enabled later using OpenAI API.
# Requires adding API key securely using environment variables.

# from openai import OpenAI
# import os
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def explain(movie, results):
#     prompt = f"""
#     A user liked '{movie}'.
#
#     Recommended movies:
#     {results['title'].tolist()}
#
#     Explain why these are similar.
#     """
#
#     res = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )
#
#     return res.choices[0].message.content


# -----------------------------
# 🎬 Streamlit UI
# -----------------------------
st.set_page_config(page_title="Netflix AI", layout="wide")

st.title("🎬 Netflix AI Recommender")
st.caption("Find movies similar to your taste using Machine Learning")

df = load_data()
similarity = build_model(df)

movie = st.selectbox(
    "🎬 Choose a movie",
    sorted(df['title'].dropna().astype(str).unique())
)

# Session storage
if "results" not in st.session_state:
    st.session_state.results = None

# Recommend button
if st.button("Recommend"):
    with st.spinner("Finding best matches... 🎯"):
        st.session_state.results = recommend(movie, df, similarity)

# Display results
if st.session_state.results is not None:
    results = st.session_state.results

    if results.empty:
        st.warning("No recommendations found.")
    else:
        for _, row in results.iterrows():
            st.markdown(f"""
            **🎬 {row['title']}**  
            ⭐ IMDB: {round(row['imdb_score'],1)}
            """)
            st.markdown("---")

        # Explanation placeholder
        if st.button("🤖 Why these recommendations?"):
            st.info("🔒 AI explanation feature will be enabled after API integration.")


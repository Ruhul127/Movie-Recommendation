from flask import Flask, render_template, request
import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Initialize Flask app
app = Flask(__name__)

# Load datasets
try:
    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")
except FileNotFoundError:
    raise Exception("Ensure 'movies.csv' and 'ratings.csv' are available in the 'data' folder.")

# Preprocess the movies data
movies['combined_features'] = movies['genres'].str.replace('|', ' ', regex=False)

# Calculate average movie ratings
movie_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
movies = movies.merge(movie_ratings, left_on='movieId', right_on='movieId', how='left')
movies['rating'] = movies['rating'].fillna(0)

# Recommendation logic
def get_recommendations(movie_title, num_recommendations=6):
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(movies['combined_features'])
    cosine_sim = cosine_similarity(count_matrix)
    try:
        movie_index = movies[movies['title'].str.contains(movie_title, case=False, na=False)].index[0]
    except IndexError:
        return []
    similarity_scores = list(enumerate(cosine_sim[movie_index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_indices = [idx for idx, score in sorted_movies[1:num_recommendations+1] if idx < len(movies)]
    recommendations = movies.iloc[recommended_indices][['title', 'genres', 'rating']]
    return recommendations.to_dict(orient='records')

def get_random_top_movies(num_movies=6):
    top_movies = movies.sort_values(by='rating', ascending=False).head(50)
    random_top_movies = top_movies.sample(n=min(num_movies, len(top_movies)))
    return random_top_movies[['title', 'genres', 'rating']].to_dict(orient='records')

def get_genre_recommendations(selected_genre, num_recommendations=6):
    genre_movies = movies[movies['genres'].str.contains(selected_genre, case=False, na=False)]
    top_genre_movies = genre_movies.sort_values(by='rating', ascending=False).head(num_recommendations)
    return top_genre_movies[['title', 'genres', 'rating']].to_dict(orient='records')

@app.route('/')
def index():
    top_movies = get_random_top_movies()
    return render_template('index.html', top_movies=top_movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie', '')
    recommendations = get_recommendations(movie_title)
    if not recommendations:
        return render_template('no_recommendations.html', query=movie_title, type='movie')
    return render_template('recommendations.html', recommendations=recommendations, query=movie_title, type='movie')

@app.route('/recommend_by_genre', methods=['POST'])
def recommend_by_genre():
    genre = request.form.get('genre', '')
    recommendations = get_genre_recommendations(genre)
    if not recommendations:
        return render_template('no_recommendations.html', query=genre, type='genre')
    return render_template('recommendations.html', recommendations=recommendations, query=genre, type='genre')

if __name__ == "__main__":
    app.run(debug=True)

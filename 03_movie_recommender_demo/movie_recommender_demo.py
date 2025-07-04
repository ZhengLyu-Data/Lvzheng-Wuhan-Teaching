import pandas as pd

# Load the original dataset
df = pd.read_csv('basic_recommender_ratings.csv')

# Drop any missing values (if any)
df = df.dropna()

# Optional: Filter to top 20 users and top 20 movies for simplified teaching
top_users = df['userId'].value_counts().head(20).index
top_movies = df['movieId'].value_counts().head(20).index
df_filtered = df[df['userId'].isin(top_users) & df['movieId'].isin(top_movies)]

# Save the cleaned file
df_filtered.to_csv('basic_recommender_ratings_cleaned.csv', index=False)

print("Cleaned dataset saved as 'basic_recommender_ratings_cleaned.csv'")

# Save the cleaned dataset
df.to_csv("cleaned_recommender_data.csv", index=False)

# Provide a download link if running in Google Colab
try:
    from google.colab import files
    files.download("cleaned_recommender_data.csv")
except:
    print("Cleaned file saved as 'cleaned_recommender_data.csv'")

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from google.colab import files

# Load cleaned ratings
df = pd.read_csv("basic_recommender_ratings.csv")

# Create pivot table
pivot = df.pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)

# Normalize for cosine similarity
scaler = StandardScaler()
scaled = scaler.fit_transform(pivot)
similarity = cosine_similarity(scaled)

# Choose target user
target_user_id = 68  # You can change this to any user in the data
target_index = list(pivot.index).index(target_user_id)

# Find top 3 similar users
similarities = pd.Series(similarity[target_index], index=pivot.index)
similar_users = similarities.sort_values(ascending=False)[1:4]

# Movies rated by similar users but not by target user
target_rated = pivot.loc[target_user_id]
recommendations = pd.Series(dtype=float)

for user in similar_users.index:
    user_ratings = pivot.loc[user]
    unrated = target_rated[target_rated == 0]
    recs = user_ratings[unrated.index]
    recommendations = recommendations.add(recs, fill_value=0)

top_recs = recommendations.sort_values(ascending=False).head(5)

# Save to file
with open("recommendation_output.txt", "w") as f:
    f.write(f"Top movie recommendations for user {target_user_id}:\n")
    if top_recs.empty:
        f.write("No unseen recommendations found.\n")
    else:
        for i, rec in enumerate(top_recs.index, 1):
            f.write(f"{i}. Movie ID: {rec} | Estimated Score: {top_recs[rec]:.2f}\n")

# Download
files.download("recommendation_output.txt")

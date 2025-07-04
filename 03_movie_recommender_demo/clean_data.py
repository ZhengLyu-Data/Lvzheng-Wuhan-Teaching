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
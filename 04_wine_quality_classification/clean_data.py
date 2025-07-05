import pandas as pd

# Load the original dataset
df = pd.read_csv("wine_quality_classification_raw.csv")

# Check for missing values (optional)
print("Missing values:\n", df.isnull().sum())

# Create a binary target variable:
# Label as 1 if quality >= 6 (good wine), otherwise 0 (average wine)
df['quality_label'] = df['quality'].apply(lambda x: 1 if x >= 6 else 0)

# Drop the original quality score column
df.drop(columns=['quality'], inplace=True)

# Save the cleaned dataset
df.to_csv("wine_quality_cleaned.csv", index=False)

print("Cleaned data saved as 'wine_quality_cleaned.csv'")
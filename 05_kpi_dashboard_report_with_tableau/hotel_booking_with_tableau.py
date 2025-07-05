import pandas as pd

# Load the raw dataset
df = pd.read_csv("hotel_booking_raw.csv")

# Drop rows with missing values (basic cleaning)
df.dropna(inplace=True)

# Standardize column names: lowercase + underscores
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Optional: Save a sample of relevant columns only (e.g., for teaching)
# df = df[['hotel', 'lead_time', 'arrival_date_year', 'country', 'is_canceled']]

# Save cleaned data
df.to_csv("hotel_booking_cleaned.csv", index=False)

print("Cleaned data saved to 'hotel_booking_cleaned.csv'")

from google.colab import files

# Download the cleaned dataset
files.download("hotel_booking_cleaned.csv")

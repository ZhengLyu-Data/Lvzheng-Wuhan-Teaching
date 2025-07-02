import pandas as pd

# Load raw appointment data
df = pd.read_csv('raw_appointments.csv')

# Preview data
print("Initial shape:", df.shape)
print(df.head())

# Rename columns for clarity
df.rename(columns={
    'ScheduledDay': 'scheduled_day',
    'AppointmentDay': 'appointment_day',
    'No-show': 'no_show',
}, inplace=True)

# Convert date columns
df['scheduled_day'] = pd.to_datetime(df['scheduled_day'])
df['appointment_day'] = pd.to_datetime(df['appointment_day'])

# Feature: Waiting days
df['waiting_days'] = (df['appointment_day'] - df['scheduled_day']).dt.days

# Save cleaned data
df.to_csv('appointments_cleaned.csv', index=False)
print("Cleaned data saved to data/appointments_cleaned.csv")

# pipeline.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('appointments_cleaned.csv')

# 1. No-show rate by gender
no_show_by_gender = pd.crosstab(df['Gender'], df['no_show'], normalize='index')
no_show_by_gender.to_csv('output/no_show_by_gender.csv')

# 2. No-show rate by weekday
# Convert appointment_day to datetime and get weekday name
df['appointment_day'] = pd.to_datetime(df['appointment_day'])
df['Weekday'] = df['appointment_day'].dt.day_name()
no_show_by_weekday = pd.crosstab(df['Weekday'], df['no_show'], normalize='index')
no_show_by_weekday.to_csv('output/no_show_by_weekday.csv')

# 3. No-show rate by age group
bins = [0, 18, 35, 50, 65, 100]
labels = ['0-18', '19-35', '36-50', '51-65', '66+']
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)
no_show_by_age_group = pd.crosstab(df['age_group'], df['no_show'], normalize='index')
no_show_by_age_group.to_csv('output/no_show_by_age_group.csv')

print("Pipeline executed successfully. CSV files saved to output/ folder.")

# run_pipeline.py
import os

# Step 1: Run data cleaning
os.system("python clean_data.py")

# Step 2: Run analysis and export charts
os.system("python pipeline.py")

print("All steps completed. Output saved to /output folder.")

import os

def download_cleaned_data():
    filename = 'appointments_cleaned.csv'
    filepath = os.path.join(os.getcwd(), filename)

    if not os.path.exists(filepath):
        print(f"❌ File not found: {filename}")
        return

    try:
        from google.colab import files
        files.download(filepath)
        print("✅ File downloaded via Colab interface.")
    except ImportError:
        print("📎 Not running in Colab. Please manually download the file from:")
        print(filepath)

if __name__ == "__main__":
    download_cleaned_data()

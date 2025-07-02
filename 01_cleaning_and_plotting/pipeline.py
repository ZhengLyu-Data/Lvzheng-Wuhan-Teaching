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
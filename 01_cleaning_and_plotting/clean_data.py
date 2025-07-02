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
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

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("wine_quality_cleaned.csv")

# Define features (X) and target variable (y)
X = df.drop(columns=['quality_label'])
y = df['quality_label']

# Add a constant term for the intercept
X = sm.add_constant(X)

# Fit the logistic regression model
model = sm.Logit(y, X)
result = model.fit()

# Print the summary of the model
print(result.summary())

# Predict probabilities and convert to binary labels
y_pred_prob = result.predict(X)
y_pred = (y_pred_prob >= 0.5).astype(int)

# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report

cm = confusion_matrix(y, y_pred)
print("\nConfusion Matrix:\n", cm)

# Classification report (accuracy, precision, recall, F1)
print("\nClassification Report:\n", classification_report(y, y_pred))

# Plot: Heatmap of confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("wine_classification_plot.png")
plt.show()

from google.colab import files

# Download the cleaned CSV file
files.download("wine_quality_cleaned.csv")

# Download the confusion matrix plot
files.download("wine_classification_plot.png")

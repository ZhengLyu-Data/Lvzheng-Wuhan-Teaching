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

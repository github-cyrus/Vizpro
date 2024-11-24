# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
data = pd.read_csv('SuperStore_Sales_Dataset.csv')

# Display first few rows of the dataset
print(data.head())

# Basic data overview
print(data.info())
print(data.describe())

# Handle missing values (if any)
data = data.dropna()  # Drop rows with missing values
# Alternatively, you can fill missing values: data.fillna(method='ffill', inplace=True)

# Exploratory Data Analysis (EDA)
# Visualize the distribution of key features
sns.pairplot(data, diag_kind='kde')
plt.show()

# Feature selection (Assuming the target variable is 'target')
# Replace 'feature1', 'feature2', ... with actual feature names
features = data.drop('target', axis=1)
target = data['target']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Model evaluation
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature importance to gain insights
feature_importances = pd.Series(model.feature_importances_, index=features.columns)
feature_importances = feature_importances.sort_values(ascending=False)

# Display feature importances
print("\nFeature Importances:\n", feature_importances)

# Visualize feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.title('Feature Importances')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.show()

# Insights: Analysis of feature importance can help understand which features contribute the most to the model's decisions.

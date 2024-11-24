# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
data = pd.read_csv('SuperStore_Sales_Dataset.csv')

# Display the first few rows of the dataset
print("Initial Data:\n", data.head())

# Basic overview of the data
print("\nData Info:\n")
print(data.info())

# Check for missing values
print("\nMissing Values in Each Column:\n")
print(data.isnull().sum())

# Handling missing values
# Option 1: Drop rows with missing values
data = data.dropna()

# Option 2: Fill missing values with mean, median, mode, or a specific value
# data['column_name'] = data['column_name'].fillna(data['column_name'].mean()) # For numerical columns
# data['column_name'] = data['column_name'].fillna(data['column_name'].mode()[0]) # For categorical columns

# Removing duplicates
data = data.drop_duplicates()

# Correcting data types (if necessary)
# Example: Converting a column to datetime
# data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')

# Detecting and removing outliers using Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))
data = data[(z_scores < 3).all(axis=1)]  # Keeping rows with z-score less than 3

# Renaming columns for consistency (if necessary)
# data.rename(columns={'old_name': 'new_name'}, inplace=True)

# Handling inconsistent data (e.g., standardizing text formats)
# Example: Converting all text in a column to lowercase
# data['text_column'] = data['text_column'].str.lower()

# Checking and converting categorical data (if necessary)
# Example: Encoding categorical variables
# data = pd.get_dummies(data, columns=['categorical_column'])

# Final cleaned data overview
print("\nCleaned Data Info:\n")
print(data.info())

# Display the first few rows of the cleaned data
print("\nCleaned Data:\n", data.head())

# Save the cleaned data to a new file (optional)
# data.to_csv('cleaned_dataset.csv', index=False)

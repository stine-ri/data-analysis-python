# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Show first 5 rows
print("=== First 5 Rows ===")
print(df.head())

# Basic information
print("\n=== Dataset Info ===")
print(df.info())

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Basic statistics
print("\n=== Basic Statistics ===")
print(df.describe())

# Group by species
print("\n=== Mean Measurements by Species ===")
print(df.groupby('species').mean())

# Create visualizations
plt.figure(figsize=(15, 10))

# 1. Line plot
plt.subplot(2, 2, 1)
df['sepal length (cm)'].plot(title='Sepal Length Variation')
plt.ylabel('Length (cm)')

# 2. Bar plot
plt.subplot(2, 2, 2)
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title('Average Petal Length by Species')
plt.ylabel('Length (cm)')

# 3. Histogram
plt.subplot(2, 2, 3)
df['sepal width (cm)'].hist(bins=15)
plt.title('Distribution of Sepal Width')
plt.xlabel('Width (cm)')

# 4. Scatter plot
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal vs Petal Length')

# Adjust layout and show plots
plt.tight_layout()
plt.show()
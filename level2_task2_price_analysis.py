import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Dataset .csv")

# Select relevant columns
df = df[['Price range', 'Aggregate rating']]
df.dropna(inplace=True)

# Most common price range
most_common_price = df['Price range'].value_counts()
print("Most Common Price Range:")
print(most_common_price)

# Plot most common price range
plt.figure(figsize=(6,4))
sns.barplot(x=most_common_price.index, y=most_common_price.values)
plt.title("Most Common Price Range")
plt.show()

# Average rating by price range
avg_rating_price = df.groupby('Price range')['Aggregate rating'].mean()
print("\nAverage Rating by Price Range:")
print(avg_rating_price)

# Plot average rating
plt.figure(figsize=(6,4))
sns.barplot(x=avg_rating_price.index, y=avg_rating_price.values)
plt.title("Average Rating by Price Range")
plt.show()

# Highest rated price range
highest_price = avg_rating_price.idxmax()
print("\nPrice Range with Highest Average Rating:", highest_price)

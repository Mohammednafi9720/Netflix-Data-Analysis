import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Program Started")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print(df.head())

# Graph 1 - Movies vs TV Shows
plt.figure(figsize=(6,4))

sns.countplot(
    x='type',
    data=df
)

plt.title("Movies vs TV Shows on Netflix")

plt.savefig("graph1.png")

print("Graph 1 Saved")

# Graph 2 - Top Countries
plt.figure(figsize=(10,5))

top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar')

plt.title("Top 10 Countries on Netflix")

plt.xlabel("Country")

plt.ylabel("Count")

plt.savefig("graph2.png")

print("Graph 2 Saved")

# Graph 3 - Ratings Distribution
plt.figure(figsize=(8,5))

sns.countplot(
    y='rating',
    data=df,
    order=df['rating'].value_counts().index
)

plt.title("Netflix Ratings Distribution")

plt.savefig("graph3.png")

print("Graph 3 Saved")

print("Project Finished")
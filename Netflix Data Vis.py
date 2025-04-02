import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv("netflix_data.csv")

# Display basic information
#print(df.info())
#print(df.head(2))  # Show the first few rows

# Fill missing values in 'director', 'cast', and 'country' with 'Unknown'
df[['director', 'cast', 'country']] = df[['director', 'cast', 'country']].fillna('Unknown')

# Drop rows where 'date_added' or 'rating' is missing
df = df.dropna(subset=['date_added', 'rating'])

# Export cleaned data to a new CSV file
df.to_csv("netflix_data_cleaned.csv", index=False)

# Confirm changes
#print(df.info())  # Check if there are still missing values
# Summary statistics
print("Release Year Range:", (df["release_year"].min(), df["release_year"].max()))
print("\nTop 5 Ratings:\n", df["rating"].value_counts().head())
print("\nContent Type Distribution:\n", df["type"].value_counts())
print("\nTop 5 Countries Producing Content:\n", df["country"].value_counts().head())
print("\nTop 5 Directors:\n", df["director"].value_counts().head())



# Create a figure with two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
sns.set_style("white")

# Release Year Histogram
sns.histplot(df["release_year"], bins=100, kde=True, color="#E50914", ax=axes[0])
axes[0].set_xlabel("Release Year", fontsize=12, color="black")
axes[0].set_ylabel("Count", fontsize=12, color="black")
axes[0].set_title("Netflix Releases by Year", fontsize=14, color="black")

# Ratings Distribution
sns.countplot(y=df["rating"], order=df["rating"].value_counts().index, color="#E50914", ax=axes[1])
axes[1].set_xlabel("Count", fontsize=12, color="black")
axes[1].set_ylabel("Rating", fontsize=12, color="black")
axes[1].set_title("Distribution of Content Ratings", fontsize=14, color="black")

# Adjust layout and display the plots together
# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.4)  # Increases space between plots

plt.show()

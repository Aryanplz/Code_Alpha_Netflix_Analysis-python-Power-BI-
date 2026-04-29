# ============================================================
# Netflix Movies & TV Shows Analysis Project
# Python EDA + Visualization
# Author: Aryan Gupta
# ============================================================

# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visualization settings
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==============================
# 2. Load Dataset
# ==============================
# Replace with your dataset path
file_path = "netflix_titles.csv"
df = pd.read_csv(file_path)

# ==============================
# 3. Basic Data Exploration
# ==============================
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe(include='all'))

# ==============================
# 4. Data Cleaning
# ==============================

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Extract year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()

# Remove duplicates
df.drop_duplicates(inplace=True)

# ==============================
# 5. Duration Cleaning
# ==============================
# Split duration into numeric and unit columns
df[['duration_value', 'duration_unit']] = df['duration'].str.split(' ', n=1, expand=True)
df['duration_value'] = pd.to_numeric(df['duration_value'], errors='coerce')

# ==============================
# 6. Movies vs TV Shows Analysis
# ==============================
plt.figure()
sns.countplot(x='type', data=df)
plt.title('Movies vs TV Shows on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.show()

# ==============================
# 7. Ratings Distribution
# ==============================
plt.figure(figsize=(12,6))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Distribution of Ratings')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()

# ==============================
# 8. Top 10 Countries Analysis
# ==============================
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# ==============================
# 9. Content Growth Over Time
# ==============================
plt.figure(figsize=(14,6))
sns.countplot(x='year_added', data=df, order=sorted(df['year_added'].dropna().unique()))
plt.xticks(rotation=45)
plt.title('Netflix Content Added Over Time')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.show()

# ==============================
# 10. Release Year Trend
# ==============================
plt.figure(figsize=(14,6))
sns.histplot(data=df, x='release_year', hue='type', bins=30, multiple='stack')
plt.title('Release Year Distribution by Content Type')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()

# ==============================
# 11. Genre Analysis
# ==============================
# Split genres and count
all_genres = df['listed_in'].str.split(', ').explode()
top_genres = all_genres.value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title('Top 10 Netflix Genres')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# ==============================
# 12. Top Directors Analysis
# ==============================
top_directors = df[df['director'] != 'Unknown']['director'].value_counts().head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.title('Top 10 Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

# ==============================
# 13. Movie Duration Analysis
# ==============================
movies = df[df['type'] == 'Movie']

plt.figure(figsize=(12,6))
sns.histplot(movies['duration_value'].dropna(), bins=30)
plt.title('Movie Duration Distribution')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Count')
plt.show()

# ==============================
# 14. Key Insights
# ==============================
print("\n========== Key Insights ==========")
print("Total Titles:", len(df))
print("Total Movies:", len(df[df['type'] == 'Movie']))
print("Total TV Shows:", len(df[df['type'] == 'TV Show']))
print("Top Country:", df['country'].value_counts().idxmax())
print("Most Common Rating:", df['rating'].value_counts().idxmax())
print("Top Genre:", all_genres.value_counts().idxmax())
print("Peak Content Addition Year:", df['year_added'].value_counts().idxmax())

# ==============================
# 15. Export Cleaned Dataset (Optional)
# ==============================
df.to_csv("cleaned_netflix_titles.csv", index=False)

print("\nCleaned dataset exported successfully!")

# ============================================================
# End of Project
# ============================================================

# TASK 4 - SENTIMENT ANALYSIS (Fixed Path for Your Folder Structure)
# CodeAlpha Internship - Omogoroye Israel

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import os

# Print current working directory for debugging
print("Current folder:", os.getcwd())

# Load CSV from parent folder (one level up)
df = pd.read_csv("Task_4_Sentiment_Analysis/Books_Plus_All_Categories.csv")  # <-- This fixes the path!

print("Dataset loaded successfully!")
print(df.head())

# Sentiment function
def get_sentiment(title):
    if pd.isna(title):
        return "Neutral"
    analysis = TextBlob(str(title))
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df['Sentiment'] = df['Title'].apply(get_sentiment)

# Save results in current folder
df.to_csv("sentiment_results.csv", index=False)
df.to_excel("sentiment_results.xlsx", index=False)

# Summary
print("\nSENTIMENT ANALYSIS RESULTS:")
print(df['Sentiment'].value_counts())

# Chart
plt.figure(figsize=(10,6))
colors = ['green', 'gray', 'red']
df['Sentiment'].value_counts().plot(kind='bar', color=colors)
plt.title("Sentiment Distribution of Book Titles (58 Books)")
plt.xlabel("Sentiment")
plt.ylabel("Number of Books")
plt.savefig("sentiment_chart.png")
plt.show()

print("\nSentiment by Category:")
print(df.groupby('Category')['Sentiment'].value_counts())
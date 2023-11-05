import pandas as pd

# Load the comparison results and EmoGen data
comparison_results = pd.read_csv('comparison_results.csv')
EmoGen = pd.read_csv('EmoGen.csv')

# Initialize Elo ratings for emotions and genres
emotion_ratings = {emotion: 1000 for emotion in EmoGen['Emotion']}
genre_ratings = {genre: 1000 for genre in EmoGen['Genre']}

# Set the K-factor
K = 50

# Define the Elo update function
def update_elo_rating(winner, loser, K, ratings):
    winner_rating = ratings[winner]
    loser_rating = ratings[loser]

    # Calculate the expected probability of the winner winning
    E_winner = 1 / (1 + 10**((loser_rating - winner_rating) / 400))

    # Update the ratings
    new_winner_rating = winner_rating + K * (1 - E_winner)
    new_loser_rating = loser_rating - K * E_winner

    return new_winner_rating, new_loser_rating

# Loop through comparison results to update ratings
for _, result in comparison_results.iterrows():
    song_1 = result['song_name_1']
    song_2 = result['song_name_2']
    preference = result['preference']

    # Retrieve the genre and emotion for each song
    genre_1, emotion_1 = EmoGen[EmoGen['Song'] == song_1].loc[:, ['Genre', 'Emotion']].values[0]
    genre_2, emotion_2 = EmoGen[EmoGen['Song'] == song_2].loc[:, ['Genre', 'Emotion']].values[0]

    # Update genre and emotion ratings based on user preference
    if preference == "Song 1":
        genre_ratings[genre_1], genre_ratings[genre_2] = update_elo_rating(genre_1, genre_2, K, genre_ratings)
        emotion_ratings[emotion_1], emotion_ratings[emotion_2] = update_elo_rating(emotion_1, emotion_2, K, emotion_ratings)
    else:
        genre_ratings[genre_2], genre_ratings[genre_1] = update_elo_rating(genre_2, genre_1, K, genre_ratings)
        emotion_ratings[emotion_2], emotion_ratings[emotion_1] = update_elo_rating(emotion_2, emotion_1, K, emotion_ratings)

# Create DataFrames for genre and emotion ratings
genre_ratings_df = pd.DataFrame(list(genre_ratings.items()), columns=['Genre', 'Rating'])
emotion_ratings_df = pd.DataFrame(list(emotion_ratings.items()), columns=['Emotion', 'Rating'])

# Save the ratings to CSV files
genre_ratings_df.to_csv('genre_ratings.csv', index=False)
emotion_ratings_df.to_csv('emotion_ratings.csv', index=False)

# Display the updated ratings
print("Updated Genre Ratings:")
print(genre_ratings_df)

print("\nUpdated Emotion Ratings:")
print(emotion_ratings_df)

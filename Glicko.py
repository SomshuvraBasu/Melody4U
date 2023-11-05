import pandas as pd
import math

# Load the comparison results and EmoGen data
comparison_results = pd.read_csv('comparison_results.csv')
EmoGen = pd.read_csv('EmoGen.csv')

# Initialize Glicko parameters for emotions and genres
emotion_ratings = {emotion: {'rating': 10, 'rd': 1000, 'volatility': 1} for emotion in EmoGen['Emotion']}
genre_ratings = {genre: {'rating': 10, 'rd': 1000, 'volatility': 1} for genre in EmoGen['Genre']}

# Set the system constant
tau = 0.5

# Create the Glicko functions
def g(phi):
    return 1 / (math.sqrt(1 + 3 * (phi**2) / (math.pi**2)))

def E(r1, r2, rd2):
    return 1 / (1 + math.exp(-g(rd2) * (r1 - r2)))

def d2(phi, sigma, E):
    return 1 / (1 / (phi**2) + 1 / E + 1 / (sigma**2))

def new_rating(r, rd, sigma, phi, delta):
    new_phi = 1 / (1 / (phi**2) + 1 / d2(phi, sigma, E(r, r, rd)))
    new_rating = r + new_phi**2 * g(rd) * (delta - E(r, r, rd))
    new_rd = math.sqrt(1 / (1 / (rd**2) + 1 / (new_phi**2)))
    new_volatility = math.sqrt(1 / (1 / (sigma**2) + 1 / (new_phi**2)))

    return new_rating, new_rd, new_volatility

# Loop through comparison results to update ratings
for _, result in comparison_results.iterrows():
    song_1 = result['song_name_1']
    song_2 = result['song_name_2']
    preference = result['preference']

    # Retrieve the genre and emotion for each song
    genre_1, emotion_1 = EmoGen[EmoGen['Song'] == song_1].loc[:, ['Genre', 'Emotion']].values[0]
    genre_2, emotion_2 = EmoGen[EmoGen['Song'] == song_2].loc[:, ['Genre', 'Emotion']].values[0]

    # Update genre and emotion ratings based on user preference using Glicko
    if preference == "Song 1":
        # Update emotion ratings
        delta_emotion = g(emotion_ratings[emotion_1]['rd']) * (1 - E(
            emotion_ratings[emotion_1]['rating'],
            emotion_ratings[emotion_2]['rating'],
            emotion_ratings[emotion_2]['rd']
        ))
        emotion_ratings[emotion_1]['rating'], emotion_ratings[emotion_1]['rd'], emotion_ratings[emotion_1]['volatility'] = new_rating(
            emotion_ratings[emotion_1]['rating'],
            emotion_ratings[emotion_1]['rd'],
            emotion_ratings[emotion_1]['volatility'],
            emotion_ratings[emotion_1]['rating'],
            delta_emotion
        )

        # Update genre ratings
        delta_genre = g(genre_ratings[genre_1]['rd']) * (1 - E(
            genre_ratings[genre_1]['rating'],
            genre_ratings[genre_2]['rating'],
            genre_ratings[genre_2]['rd']
        ))
        genre_ratings[genre_1]['rating'], genre_ratings[genre_1]['rd'], genre_ratings[genre_1]['volatility'] = new_rating(
            genre_ratings[genre_1]['rating'],
            genre_ratings[genre_1]['rd'],
            genre_ratings[genre_1]['volatility'],
            genre_ratings[genre_1]['rating'],
            delta_genre
        )
    else:
        # Update emotion ratings
        delta_emotion = g(emotion_ratings[emotion_2]['rd']) * (-E(
            emotion_ratings[emotion_1]['rating'],
            emotion_ratings[emotion_2]['rating'],
            emotion_ratings[emotion_1]['rd']
        ))
        emotion_ratings[emotion_2]['rating'], emotion_ratings[emotion_2]['rd'], emotion_ratings[emotion_2]['volatility'] = new_rating(
            emotion_ratings[emotion_2]['rating'],
            emotion_ratings[emotion_2]['rd'],
            emotion_ratings[emotion_2]['volatility'],
            emotion_ratings[emotion_2]['rating'],
            delta_emotion
        )

        # Update genre ratings
        delta_genre = g(genre_ratings[genre_2]['rd']) * (-E(
            genre_ratings[genre_1]['rating'],
            genre_ratings[genre_2]['rating'],
            genre_ratings[genre_1]['rd']
        ))
        genre_ratings[genre_2]['rating'], genre_ratings[genre_2]['rd'], genre_ratings[genre_2]['volatility'] = new_rating(
            genre_ratings[genre_2]['rating'],
            genre_ratings[genre_2]['rd'],
            genre_ratings[genre_2]['volatility'],
            genre_ratings[genre_2]['rating'],
            delta_genre
        )

# Create DataFrames for genre and emotion ratings
genre_ratings_df = pd.DataFrame({'Genre': genre_ratings.keys(), 'Rating': [rating['rating'] for rating in genre_ratings.values()]})
emotion_ratings_df = pd.DataFrame({'Emotion': emotion_ratings.keys(), 'Rating': [rating['rating'] for rating in emotion_ratings.values()]})

# Save the ratings to CSV files
genre_ratings_df.to_csv('glicko_genre_ratings.csv', index=False)
emotion_ratings_df.to_csv('glicko_emotion_ratings.csv', index=False)

# Display the updated ratings
print("Updated Glicko Genre Ratings:")
print(genre_ratings_df)

print("\nUpdated Glicko Emotion Ratings:")
print(emotion_ratings_df)

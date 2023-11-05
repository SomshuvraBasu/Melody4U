
# Sample user preferences (genre, emotion, language weights) and artist weights
# user_weights = {
#     "genre": {
#         "Pop": 0.7,
#         "Rock": 0.3,
#         "Hip-Hop": 0.4,
#     },
#     "emotion": {
#         "Happy": 0.6,
#         "Sad": 0.4,
#     }
# }

# Sample user's artist weights calculated from listening history
# user_artist_weights = {
#     "Artist X": 1200,
#     "Artist Y": 1100,
#     "Artist Z": 1050,
# }

# # Sample user history containing the number of songs listened by the user for each artist
# user_artist_history = {
#     "Artist X": 10,
#     "Artist Y": 5,
#     "Artist Z": 3,
# }

# Sample song data with artist and language
# song_data = {
#     "song_name": ["Song A", "Song B", "Song C", "Song D"],
#     "artist": ["Artist X", "Artist Y", "Artist Z", "Artist X"],
#     "genre": ["Pop", "Rock", "Hip-Hop", "Pop"],
#     "emotion": ["Happy", "Sad", "Happy", "Sad"],
# }

# Create a DataFrame from song_data

# Function to calculate artist weights based on the number of songs listened
# def calculate_artist_weights(user_artist_history, base_rating=1000, k=32):
#     artist_weights = {}  # Dictionary to store artist weights

#     for artist, num_songs_listened in user_artist_history.items():
#         # Calculate expected outcome based on Elo rating formula
#         expected_outcome = 1 / (1 + 10 ** ((base_rating - 1000) / 400))

#         # Calculate the outcome based on the number of songs listened
#         outcome = num_songs_listened

#         # Update artist weight using Elo rating formula
#         artist_weights[artist] = base_rating + k * (outcome - expected_outcome)

#     return artist_weights

# user_artist_weights = calculate_artist_weights(user_artist_history)
import pandas as pd
import json
from update_artist_weight import ArtistWeightCalculator

# update artist weights
history_file_path = "../data/history.csv"
output_file_path = "../data/artist_weights.json"

artist_weight_calculator = ArtistWeightCalculator(history_file_path, output_file_path)
artist_weight_calculator.read_user_history()
artist_weight_calculator.calculate_artist_weights()
artist_weight_calculator.save_artist_weights()

# read the song database, user weights, and artist weights
df = pd.read_csv("../data/song_db.csv")
user_weights = json.load(open("../data/user_weights.json"))
user_artist_weights = json.load(open("../data/artist_weights.json"))

# Function to calculate recommendation scores
def calculate_recommendation_scores(song_name, user_weights, user_artist_weights, df):
    idx = df[df["song_name"] == song_name].index[0]
    recommendation_scores = []

    for i in range(len(df)):
        song = df.iloc[i]

        # Calculate genre, emotion, and language scores based on user preferences
        genre_score = user_weights["genre"].get(song["genre"], 0)
        emotion_score = user_weights["emotion"].get(song["emotion"], 0)

        # Calculate artist weight score based on user's artist preferences
        artist_weight_score = user_artist_weights.get(song["artist"], 1000)  # 1000 is the default weight

        # Calculate the total recommendation score based on genre, emotion, language, and artist
        total_score = genre_score + emotion_score  + artist_weight_score
        recommendation_scores.append(total_score)

    return recommendation_scores

# Function to get song recommendations
def get_recommendations(song_name, user_weights, user_artist_weights, df):
    recommendation_scores = calculate_recommendation_scores(song_name, user_weights, user_artist_weights, df)
    song_indices = sorted(range(len(recommendation_scores)), key=lambda i: recommendation_scores[i], reverse=True)
    # add correspoding artist name
    recommened_song_artist = []
    for i in song_indices:
        recommened_song_artist.append(df["song_name"].iloc[i] + " - " + df["artist"].iloc[i])
    # convert to df
    recommened_song_artist = pd.DataFrame(recommened_song_artist, columns=["song_name"])
    # save this dataframe to csv in recommendation_song.csv
    recommened_song_artist.to_csv("../data/recommendation_song.csv", index=False)
    return recommened_song_artist[:5]
    # return df["song_name"].iloc[song_indices[:5]]

# Example: Recommend songs similar to "Song A"
recommendations = get_recommendations("Country Roads", user_weights, user_artist_weights, df)
print("Recommended Songs:")
print(recommendations)

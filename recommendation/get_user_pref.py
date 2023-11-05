import csv
import json

class UserWeightsConverter:
    def __init__(self, emotion_csv_file, genre_csv_file, output_json_file):
        self.emotion_csv_file = emotion_csv_file
        self.genre_csv_file = genre_csv_file
        self.output_json_file = output_json_file
        self.user_weights = {
            "genre": {},
            "emotion": {},
        }

    def process_emotion_csv(self):
        with open(self.emotion_csv_file, 'r') as emotion_csv:
            emotion_data = csv.DictReader(emotion_csv)
            for row in emotion_data:
                emotion = row['Emotion']
                rating = float(row['Rating'])
                self.user_weights["emotion"][emotion.lower()] = round(rating, 2)

    def process_genre_csv(self):
        with open(self.genre_csv_file, 'r') as genre_csv:
            genre_data = csv.DictReader(genre_csv)
            for row in genre_data:
                genre = row['Genre']
                rating = float(row['Rating'])
                self.user_weights["genre"][genre.lower()] = round(rating, 2)

    def save_user_weights_to_json(self):
        with open(self.output_json_file, 'w') as json_file:
            json.dump(self.user_weights, json_file, indent=4)
        print("Conversion completed and saved to", self.output_json_file)

if __name__ == "__main__":
    emotion_csv_file = '../emotion_ratings.csv'
    genre_csv_file = '../genre_ratings.csv'
    output_json_file = '../data/user_weights.json'

    converter = UserWeightsConverter(emotion_csv_file, genre_csv_file, output_json_file)
    converter.process_emotion_csv()
    converter.process_genre_csv()
    converter.save_user_weights_to_json()

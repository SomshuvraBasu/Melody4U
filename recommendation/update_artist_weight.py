import csv
import json

class ArtistWeightCalculator:
    def __init__(self, history_file_path, output_file_path):
        self.history_file_path = history_file_path
        self.output_file_path = output_file_path
        self.user_artist_history = {}
        self.artist_weights = {}

    def calculate_artist_weights(self, base_rating=1000, k=32):
        for artist, num_songs_listened in self.user_artist_history.items():
            expected_outcome = 1 / (1 + 10 ** ((base_rating - 1000) / 400))
            outcome = num_songs_listened
            self.artist_weights[artist] = base_rating + k * (outcome - expected_outcome)

    def read_user_history(self):
        with open(self.history_file_path, "r", newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                artist = row["Artist"]
                if artist in self.user_artist_history:
                    self.user_artist_history[artist] += 1
                else:
                    self.user_artist_history[artist] = 1

    def save_artist_weights(self):
        with open(self.output_file_path, "w") as json_file:
            json.dump(self.artist_weights, json_file)
        print("Artist weights saved to", self.output_file_path)

if __name__ == "__main__":
    history_file_path = "../data/history.csv"
    output_file_path = "../data/artist_weights.json"

    artist_weight_calculator = ArtistWeightCalculator(history_file_path, output_file_path)
    artist_weight_calculator.read_user_history()
    artist_weight_calculator.calculate_artist_weights()
    artist_weight_calculator.save_artist_weights()

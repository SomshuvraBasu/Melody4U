import random
import csv

class SongDatabase:
    def __init__(self, song_db_path, history_path):
        self.song_db_path = song_db_path
        self.history_path = history_path
        self.song_data = []
        self.history = []

    def read_song_database(self):
        with open(self.song_db_path, "r", newline="") as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Skip the header
            for row in csv_reader:
                self.song_data.append(row)

    def get_random_song(self):
        return random.choice(self.song_data)

    def generate_and_save_history(self, num_songs):
        for _ in range(num_songs):
            song = self.get_random_song()
            self.history.append(song)

        with open(self.history_path, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Song name", "Genre", "Emotion", "Artist"])
            csv_writer.writerows(self.history)
        print("History saved to", self.history_path)

if __name__ == "__main__":
    song_db_path = "../data/song_db.csv"
    history_path = "../data/history.csv"

    song_db = SongDatabase(song_db_path, history_path)
    song_db.read_song_database()
    song_db.generate_and_save_history(10)

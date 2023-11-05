import os
import csv
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load client secrets from the JSON file you downloaded in Step 2
client_secrets_file = 'Playlist/client_secret_489443072043-nmsii81i5hnt9jbmhlc9pb7oi7labgnr.apps.googleusercontent.com.json'
# Your YouTube Data API version and API key
api_service_name = 'youtube'
api_version = 'v3'

# Load the CSV file
csv_file = 'Playlist/songs.csv'

def create_youtube_playlist():
    # Use InstalledAppFlow for authentication
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, ['https://www.googleapis.com/auth/youtube.force-ssl'])
    credentials = flow.run_local_server()

    # Create a YouTube Data API service
    youtube = build(api_service_name, api_version, credentials=credentials)

    # Read the CSV file and create a playlist
    playlist_title = 'My Custom Playlist'
    request_body = {
        'snippet': {
            'title': playlist_title,
            'description': 'This Playlist has been genrated by Melody4U! Keep Grooving!',
        },
        'status': {
            'privacyStatus': 'private',  # You can change this if needed
        },
    }
    playlist_response = youtube.playlists().insert(part='snippet,status', body=request_body).execute()
    playlist_id = playlist_response['id']

    # Read the CSV file and add songs to the playlist
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            song_title = row['Song']
            artist = row['Artist']
            video_id = search_video_id(youtube, song_title, artist)
            if video_id:
                add_video_to_playlist(youtube, playlist_id, video_id)

def search_video_id(youtube, song_title, artist):
    # Search for a video with the song title and artist
    query = f'{song_title} {artist} official music video'
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=1
    ).execute()

    if 'items' in search_response:
        return search_response['items'][0]['id']['videoId']
    else:
        print(f'Video not found for {song_title} by {artist}')
        return None

def add_video_to_playlist(youtube, playlist_id, video_id):
    # Add a video to the playlist
    request_body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id,
            }
        }
    }
    youtube.playlistItems().insert(part='snippet', body=request_body).execute()

if __name__ == '__main__':
    create_youtube_playlist()

import streamlit as st
import pandas as pd
import os

# Define the paths to the folders containing images and audio clips
images_folder = 'Images'  # Path to the folder with album cover images
music_folder = 'Music'    # Path to the folder with audio clips

# Load your dataset
# Replace 'data.csv' with the path to your dataset
data = pd.read_csv('data.csv')

# Load or create the results CSV file
results_file = 'comparison_results.csv'

st.title("Style Your Taste")

# Initialize the session state to store results and current pair
if 'results' not in st.session_state:
    st.session_state.results = pd.DataFrame(columns=['song_name_1', 'song_name_2', 'preference'])
if 'current_pair_index' not in st.session_state:
    st.session_state.current_pair_index = 0

# Function to get the current pair for comparison
def get_current_pair():
    pair_index = st.session_state.current_pair_index
    if pair_index < len(data):
        return data.iloc[pair_index]
    else:
        return None

song_pair = get_current_pair()

if song_pair is not None:
    st.write("Listen to the 30-second clips and vote for your preference:")

    # Set the size for the album cover
    album_cover_size = 200  # You can adjust this size as needed

    col1, col2 = st.columns(2)

    # Container for the album cover and media player on the left side
    with col1:
        st.write("Song 1")
        image_path_1 = os.path.join(images_folder, song_pair['album_cover_1'])
        audio_path_1 = os.path.join(music_folder, song_pair['audio_clip_1'])
        st.image(image_path_1, width=album_cover_size)
        st.audio(audio_path_1, format="audio/mp3", start_time=0)

    # Container for the album cover and media player on the right side
    with col2:
        st.write("Song 2")
        image_path_2 = os.path.join(images_folder, song_pair['album_cover_2'])
        audio_path_2 = os.path.join(music_folder, song_pair['audio_clip_2'])
        st.image(image_path_2, width=album_cover_size)
        st.audio(audio_path_2, format="audio/mp3", start_time=0)

    if st.button("I prefer Song 1"):
        st.session_state.results = st.session_state.results.append(
            {'song_name_1': song_pair['song_name_1'], 'song_name_2': song_pair['song_name_2'], 'preference': 'Song 1'},
            ignore_index=True
        )
        st.session_state.current_pair_index += 1

    if st.button("I prefer Song 2"):
        st.session_state.results = st.session_state.results.append(
            {'song_name_1': song_pair['song_name_1'], 'song_name_2': song_pair['song_name_2'], 'preference': 'Song 2'},
            ignore_index=True
        )
        st.session_state.current_pair_index += 1

    # Show progress
    st.write(f"Comparison {st.session_state.current_pair_index} of {len(data)}")

    if st.session_state.current_pair_index == len(data):
        # All comparisons are done
        st.write("All comparisons are completed.")
        # Save the results to a CSV file
        st.session_state.results.to_csv(results_file, index=False)
else:
    st.write("All comparisons are completed.")

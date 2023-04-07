import sys
import spotipy
import spotipy.util as util

# Enter your Spotify username and playlist ID
username = ""
playlist_id = ""

# Read track IDs from the file "tracks.txt"
with open("tracks.txt", "r") as datafile:
    track_ids = datafile.read().split(',')

# Remove any leading/trailing whitespace from each track ID
track_ids = [track.strip() for track in track_ids if track.strip()]

# Remove duplicate track IDs
unique_track_ids = list(set(track_ids))

# Set the scope for the Spotify API access
scope = 'playlist-modify-public'

# Enter your client ID, client secret, and redirect URI
client_id = ""
client_secret = ""
redirect_uri = "http://localhost/"

# Request a token for the user
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Calculate the number of batches needed to process all tracks
num_batches = (len(unique_track_ids) // 100) + 1

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    # Process tracks in batches of 100
    for batch in range(num_batches):
        start = batch * 100
        end = min((batch + 1) * 100, len(unique_track_ids))
        print(f"Processing batch {batch + 1}/{num_batches}")

        # Add tracks to the playlist
        results = sp.user_playlist_add_tracks(username, playlist_id, unique_track_ids[start:end])
        print(results)
else:
    print(f"Can't get token for {username}")

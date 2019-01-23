import sys
import spotipy
import spotipy.util as util

#enter username and playlist_id
username = ""
playlist_id = ""
datafile = open("tracks.txt", "r")
track_ids_ = datafile.read()
   
print (track_ids_)
    
datafile.close()
   

for track in track_ids_:
    track.strip()

dataset_list = ''.join(track_ids_)
dataset_array = []
for item in dataset_list.split(','): 
    dataset_array.append(item)

dataset_array[:] = [item for item in dataset_array if item != '']

dataset_array_s = set(dataset_array) 
all_tracks = []
for item in dataset_array_s: 
    all_tracks.append(item)


print (all_tracks)

scope = 'playlist-modify-public'
# enter client id and client scret and redirect uri
token = util.prompt_for_user_token(username, scope, "client_id", "client_secret", "http://localhost/")


print("Len track:{%d}, Epochs:{%d}" % (len(all_tracks), int(round((len(all_tracks)/100) + 0.5))))

if token:
     sp = spotipy.Spotify(auth=token)
     sp.trace = False
     for epoch in range(0, int(round((len(all_tracks)/100) + 0.5))):
         print("Round:",epoch)
         ran = 0
         if ((len(all_tracks) - epoch*100) > 100):
             ran =(epoch * 100) + 100
             print ("Ran{%d} at Round{%d}" %(ran, epoch))
         else:
             ran = ((epoch * 100) + (len(all_tracks) - epoch*100))
             print ("Ran{%d} at Round{%d}" %(ran, epoch))
            
         results = sp.user_playlist_add_tracks(username, playlist_id,all_tracks[(epoch * 100): ran])
         print (results)

else:
    print ("Can't get token for", username)

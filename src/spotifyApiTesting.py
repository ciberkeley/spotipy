import pandas as pd
import spotipy
import numpy as np

sp = spotipy.Spotify() # Load the Spotipy Client

# Get specific artist object
artistId = '3TVXtAsR1Inumwj472S9r4' # Specify artist id: Drake
artist = sp.artist(artistId)
print(artist)

# Get specific album object
albumId = '40GMAhriYJRO1rsY4YdrZb' # Specific album id: Views
album = sp.album(albumId)
print(album)

# Get top 10 tracks for a given artist
top10 = sp.artist_top_tracks(artistId)
print(type(top10['tracks'])) # a list
top_track = top10['tracks'][0]
print(top_track) # Fake Love

# Get related artist based on "analysis of the Spotify community's listening history"
related_artists = sp.artist_related_artists(artistId)
print(type(related_artists['artists']))
print(related_artists['artists'][0]) # Most related artist



# Get specific track's features
trackId = top_track['id']
track = sp.track(trackId)
print(track)



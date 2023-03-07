from songs import Songs
from spotifyapp import Spotify

#Scrap the songs website to get the titles
songs = Songs()
title_details = songs.scrap_songs()

#Create spotify object and authenticate to generate the token and then create playlist
sp = Spotify()
sp.authenticate_spotify()
sp.spotify_create_play_list(title_details['title_text_list'], title_details['year'])






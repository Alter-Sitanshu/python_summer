import os
import requests
from bs4 import BeautifulSoup
import spotipy as spotify
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("SPOTIFY_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET")
#----Gets the year of search from the user-----
year = int(input("Enter the year of search : "))
URL = f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/"

#-----Scraping the Billboard page-----
response = requests.get(url=URL)
page = response.text
soup = BeautifulSoup(page, "html.parser")
songs = soup.select(selector="li #title-of-a-story")

#----Getting hold of the song titles using selectors------
song_list = [tags.getText().strip() for tags in songs]

#----Spotify logins and adding playlist------
scope = "playlist-modify-private"  #access is kept private but scope can be changed to public too
sp = spotify.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                scope=scope,
                                                redirect_uri="http://example.com"))

#----Getting hold of the user id after spotify authorization----
user_id = sp.current_user()["id"]
song_uri: list = []

#-----Searching all the songs to get their Spotify URI using loop------
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except KeyError:
        print(f"Song: {song} Doesn't Exist in Spotify. Skipped")

#------Creating the New Playlist-----
print("All tracks searched: Now Adding to playlist")
sp_playlist = sp.user_playlist_create(user= user_id, public=False, name=f"Billboard {year}")

#----Adding songs to playlist------
sp.playlist_add_items(sp_playlist["id"], items=song_uri)
print("Playlist created successfully !!")
from bs4 import BeautifulSoup
from json import loads
from pprint import pprint
from requests import get
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ----------------------------- CONSTANTS --------------------------------------- #
BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100"
REDIRECT_URL = "http://example.com"
SPOTIPY_CLIENT_ID = "[YOUR_CLIENT_ID]"
SPOTIPY_CLIENT_SECRET = "[YOUR_CLIENT_SECRET]"
SPOTIPY_SCOPE = "playlist-modify-private"
TOKEN = "[YOUR_ACCESS_TOKEN]"

# ----------------------------- USER DATE --------------------------------------- #
user_date = input("Which year do you want to travel to? Type the date in this format (YYYY-MM-DD):\t")

# --------------------------- BEAUTIFUL SOUP ------------------------------------ #
soup = BeautifulSoup(get(url=f"{BILLBOARD_ENDPOINT}/{user_date}").text, "html.parser")
songs = []
for title in soup.select(".o-chart-results-list__item > h3"):
    songs.append(title.get_text().strip())

# --------------------------- SPOTIFY OAUTH ------------------------------------- #
spotify_access = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                              client_secret=SPOTIPY_CLIENT_SECRET,
                              redirect_uri=REDIRECT_URL,
                              scope=SPOTIPY_SCOPE)
access_token = spotify_access.get_access_token()
access_token = spotify_access.get_cached_token()

# ---------------------------- SPOTIFY TOKEN ------------------------------------ #
try:
    with open(".cache") as file:
        file.read()
except FileNotFoundError:
    print("No token")
else:
    TOKEN = loads(file.read())
    user_client = spotipy.client.Spotify(auth=TOKEN["access_token"])

    # ----------------------------- SONG URIS --------------------------------------- #
    song_uris = []
    for song in songs:
        track_search = user_client.search(f"track: {song}", limit=1)
        try:
            uri = track_search["tracks"]["items"][0]["uri"]
        except KeyError:
            pass
        else:
            song_uris.append(uri)

    # -------------------------- CREATING PLAYLIST ---------------------------------- #
    user_id = user_client.current_user()["id"]
    my_playlist = user_client.user_playlist_create(user=user_id,
                                                   name=f"{user_date} Billboard 100",
                                                   description="Playlist Created With Python & Spotipy!",
                                                   public=False)

    playlist_id = my_playlist["id"]
    user_client.playlist_add_items(playlist_id=playlist_id, items=song_uris)

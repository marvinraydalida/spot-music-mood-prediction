import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


load_dotenv()
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def search_tracks(q):
    searched_track = []
    search = spotify.search(q=q, limit = 50, type = 'track')
    for item in search['tracks']['items']:
        tmp = {
            'name': item['name'],
            'album_art': item['album']['images'][0]['url'],
            'artist': item['album']['artists'][0]['name'],
            'id': item['id'],
            'uri': item['uri']
        }
        searched_track.append(tmp)    
    return searched_track


def get_track(uri):
    track = []
    track_details = spotify.track(uri,market='PH')
    details = {
        'track_name': track_details['name'],
        'track_artist': track_details['album']['artists'][0]['name'],
        'album_art': track_details['album']['images'][0]['url'],
        'preview_url': track_details['preview_url'],
        'redirect_url': track_details['external_urls']['spotify']
    }
    track.append(details)
    audio_features = spotify.audio_features(uri)
    track.append(audio_features[0])
    return track

# print(track['id'])
# print(track['name'])
# print(track['album']['artists'][0]['name'])
# print(track['album']['images'][0]['url'])
# print(track['preview_url'])

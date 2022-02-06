import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


load_dotenv()
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def search_tracks(q):
    searched_track = []
    search = spotify.search(q=q, limit = 50, type = 'track', market='PH')
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


def get_top_fifthy():
    #spotify:playlist:37i9dQZEVXbNBz9cRCSFkY
    tracks = []
    top_fifthy_uri = "spotify:playlist:37i9dQZEVXbNBz9cRCSFkY"
    top_track = spotify.playlist_tracks(playlist_id = top_fifthy_uri, market= 'PH')
    for item in top_track['items']:
        tmp = {
            'name': item['track']['name'],
            'album_art': item['track']['album']['images'][0]['url'],
            'artist': item['track']['album']['artists'][0]['name'],
            'id': item['track']['id'],
            'uri': item['track']['uri']
        }
        tracks.append(tmp)
    return tracks

# print(result['items'][0]['track']['id'])
# print(result['items'][0]['track']['name'])
# print(result['items'][0]['track']['album']['artists'][0]['name'])
# print(result['items'][0]['track']['album']['images'][0]['url'])
# print(result['items'][0]['track']['uri'])

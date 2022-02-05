from typing import AsyncIterable
import pandas as pd
from sklearn.linear_model import LogisticRegression

def predict_track(audio_features):
    

    data = pd.read_csv('./audio_features_v5.csv')

    feature_cols = [
        'danceability',
        'acousticness',
        'energy',
        'instrumentalness',
        'key',
        'liveness',
        'loudness',
        'speechiness',
        'tempo',
        'time_signature',
        'valence',
        'mode'
    ]
    #X is the feature matrix
    X = data[feature_cols]
    #y is the vector label
    y = data.mood_string

    
    model = LogisticRegression(max_iter=10000, penalty='l2')
    model.fit(X,y)
    track_af = pd.json_normalize(audio_features)
    X_pred = track_af[feature_cols]

    return model.predict(X_pred)
from typing import AsyncIterable
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def predict_track(audio_features):
    data = pd.read_csv('./audio_features_dataset.csv')
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

    gradient_boost_model = GradientBoostingClassifier()
    gradient_boost_model.fit(X,y)
    
    track_af = pd.json_normalize(audio_features)
    X_pred = track_af[feature_cols]

    return gradient_boost_model.predict(X_pred)
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.metrics.pairwise import linear_kernel

base_dir = os.path.dirname(os.path.abspath(__file__))

cosine_sim_path = os.path.join(base_dir, 'cosine_sim.pkl')
tfidf_vectorizer_path = os.path.join(base_dir, 'tfidf_vectorizer.pkl')
data_path = os.path.join(base_dir, 'data.pkl')

cosine_sim = pickle.load(open(cosine_sim_path, 'rb'))
tfidf_vectorizer = pickle.load(open(tfidf_vectorizer_path, 'rb'))
data = pickle.load(open(data_path, 'rb'))

tfidf_matrix = tfidf_vectorizer.fit_transform(data['combined_features'])

def get_destinations():
    return data['Destination']

def get_recommendations(destination, cosine_sim=cosine_sim):
    
    exact_match = data[data['Destination'] == destination]
    if not exact_match.empty:
        index = exact_match.index[0]
    else:
        destination_vector = tfidf_vectorizer.transform([destination])
        cosine_scores = linear_kernel(destination_vector, tfidf_matrix).flatten()
        matching_destinations = data.copy()
        matching_destinations['cosine_score'] = cosine_scores

        matching_destinations = matching_destinations.sort_values(by='cosine_score', ascending=False)

        index = matching_destinations.index[0]
    
    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:9]
    destination_indices = [i[0] for i in sim_scores]
    
    return data[['Destination', 'Image']].iloc[destination_indices]

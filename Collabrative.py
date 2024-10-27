import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def recommend_collaborative(user):
    interactions = pd.read_csv('games_data.csv', index_col=0)
    
    # Calculate the cosine similarity between users
    cosine_sim_matrix = cosine_similarity(interactions)
    cosine_sim_df = pd.DataFrame(cosine_sim_matrix, index=interactions.index, columns=interactions.index) # Convert to DF
    dot_product_df = cosine_sim_df.dot(interactions)

    # give Game Scores for user
    user_game_scores = dot_product_df.loc[user].to_dict()
    sorted_user_game_scores = dict(sorted(user_game_scores.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_user_game_scores
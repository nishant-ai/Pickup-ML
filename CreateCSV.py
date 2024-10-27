import pandas as pd
import json

def create_interaction_matrix(data_source):
    # If data_source is a string, assume it's a file path
    if isinstance(data_source, str):
        with open(data_source, 'r') as file:
            data = json.load(file)
    else:
        # If it's already a dictionary, use it directly
        data = data_source

    # First, collect all unique games and users
    all_games = set()
    all_users = set()

    for user, interactions in data.items():
        all_users.add(user)
        for interaction_type in ['GameLike', 'UnlikeGame']:
            if interaction_type in interactions:
                for game,  in interactions[interaction_type]:
                    all_games.add(game)

    # Create a DataFrame filled with zeros
    df = pd.DataFrame(0, 
                     index=sorted(list(all_users)), 
                     columns=sorted(list(all_games)))

    # Fill in the interactions
    for user, interactions in data.items():
        # Handle likes (1)
        if 'GameLike' in interactions:
            for game, _ in interactions['GameLike']:
                df.loc[user, game] = 1

        # Handle unlikes (-1)
        if 'UnlikeGame' in interactions:
            for game, _ in interactions['UnlikeGame']:
                df.loc[user, game] = -1

    return df

df = create_interaction_matrix(UserData)

df.to_csv('games_data.csv', index=True)


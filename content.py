import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

games_df = pd.DataFrame(games_data) # this will be json data of games
games_df.drop(columns=['max_players', 'min_players', 'date'], inplace=True)
games_df.drop(columns = ['format'], inplace =True)
nltk.download('punkt')
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))

def filter_stopwords(desc):
    tokens = word_tokenize(desc)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)  # Join the tokens back into a string

games_df['filtered_desc'] = games_df['desc'].apply(filter_stopwords)


def clean_text(desc):
    # Tokenize the text
    tokens = word_tokenize(desc)
    
    # Join tokens back into a string
    filtered_text = ' '.join(tokens)

    # Remove punctuation using regex
    cleaned_text = re.sub(r'[^\w\s]', '', filtered_text)  # Removes punctuation
    
    return cleaned_text    

games_df['cleaned_desc'] = games_df['filtered_desc'].apply(clean_text)
games_df.drop(columns=['filtered_desc'], inplace=True)
games_df.drop(columns=['desc'], inplace=True)
games_df = games_df.drop(columns=['sport'])

vectorizer = CountVectorizer()

games_df['Data'] = games_df[['id', 'name', 'skill', 'age_group', 'cleaned_desc']].agg(' '.join, axis=1)
vectorData = vectorizer.fit_transform(games_df['Data'])
dense_matrix = vectorData.todense()
dense_array = np.asarray(dense_matrix)
cosineMatrix = cosine_similarity(dense_array, dense_array)

def content_based_recommender(game_Index):
    topGames=cosineMatrix[game_Index]
    game_score={}
    for i in range(len(topGames)):
        game_score[i]=topGames[i]
    sorted_game_score=dict(sorted(game_score.items(),key=lambda x:x[1],reverse=True))
    return sorted_game_score



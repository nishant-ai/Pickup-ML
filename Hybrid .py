from Collabrative import recommend_collaborative
from content import content_based_recommender
import pandas as pd
def hybridrecommend(user, last_Game ):

    hybridScoreForUser = {}
    collabrative = recommend_collaborative(user)
    content = content_based_recommender(last_Game) # this is the index game or gameID 
    coloumngame = pd.read_csv('games_data.csv', index_col=0)
    coloumns= coloumngame.columns
    for  game in coloumns:
        hybridscore = (0.7*content[game]) + (0.3*collabrative[game])
        hybridScoreForUser[game] = hybridscore
    return hybridScoreForUser
    
acutalhybridscore=hybridrecommend("User10")
   
           
# Assuming your dictionary is called contentSimilarities
sorted_dict = dict(sorted(acutalhybridscore.items(), key=lambda item: item[1], reverse=True))
     

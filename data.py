GamesId={'3h5KaMRHrrLed4BIOjx0': 0,
 '3sG3P25q6iwJcCwA3Eag': 1,
 '44cCV3M5CxxHb1HCSxfu': 2,
 '45eQSAjrtn2Pxwmmhs15': 3,
 '56SlheN9Gdn8Mi8vp3vt': 4,
 '5AAe8Od7k627z5Xi1iKL': 5,
 '6BZ2c0b7buhy5aFNbBqV': 6,
 '6RxQ6bTrLbv5Er0Gy7Vo': 7,
 '6wvpaGbEhotGMCvPA7wJ': 8,
 '7E4z96w4fDNIZLrZ7kES': 9,
 '7FFIt92Ph78po5tbGYkE': 10,
 '8GqPuhGe4mnvoDUbMnO9': 11,
 'B9m6sPCgfW5cE2PW5xAv': 12,
 'CvgQA0mTP69EE1Bh97aw': 13,
 'D6lRgWBoeSl6MG1cvD1F': 14,
 'EGqpGCzoicLtjQPFe7wd': 15,
 'EGtPU4C72txIPUZwk2J0': 16,
 'ESLrlH91MyFlHadcqSSF': 17,
 'FVaADKMN9dZ8ulgMwWR9': 18,
 'G5gNs4yiAgN5rqRLT70n': 19,
 'H07lOBixd59GoAY7kMXm': 20,
 'HE52wY59wamFPYTQAGnQ': 21,
 'HPyn8effxcz7VMgf2djO': 22,
 'HZ4P8ddnpHrgRvZ3CVv3': 23,
 'JMPwx2OxleKj53JMw9oa': 24,
 'JyVpeUeCPmiBtnHy1XBm': 25,
 'KGtTkbjgYS0erctkyh5p': 26,
 'MDD6ECsbvCFFaiYw2zZ6': 27,
 'N1ef5aGSTpN31jrQEtBR': 28,
 'PUJNGyBuySWtx5GFbgwu': 29,
 'Pwodc1mPjSGYrpLhbaTO': 30,
 'QZDidUP1qkVjnfYoJ8ZJ': 31,
 'R9L9OXPpfVOTDdFoa6E2': 32,
 'T01gPLqGo0XwnGoavyIr': 33,
 'UBs6kC93jLcClh14FgtP': 34,
 'VIrvOxTgL9BSYUN3Qfto': 35,
 'VzmGHbuhJKzmk4TGG3t9': 36,
 'YeC7ibtvKl1HFA54TBeY': 37,
 'YfLDreb2PESI3n5Ht2TD': 38,
 'agxN6mFexqEywEHPGg9o': 39,
 'cx9ZOVu31JKvqGlVejad': 40,
 'e5MhtPRVEAH1dcWYo3L6': 41,
 'eBKSUrnoUgzBxv4mXFbF': 42,
 'fRyj3gjsBiRIbY6EYYIs': 43,
 'fYe89l99ZbWdjaJGxSXj': 44,
 'jsbZlUdFAOFoGlNiuUop': 45,
 'kX2HjDYE0d8lSkRDgSjv': 46,
 'lDzlYLane9GU2GBA3Nfk': 47,
 'mWg5ujqSS42hXcrdrI91': 48,
 'ocDheJvdECx1qYaVH4VT': 49,
 'osjB8f4aWHAYcrfCmNNn': 50,
 'pcGdMw4ud4eAiwy9i6gS': 51,
 'pxBkqv2BgXFknUsFtqDF': 52,
 'rN7VYGHVVZCricjOblKT': 53,
 'rQ7rlCivcyxYOfM4eZSu': 54,
 'rr9xoLqKpsuRb7lOUj0Z': 55,
 'tSobFSGK7CVxjXN5wGAr': 56,
 'tjsr1m5EbNBqhJNAh5q7': 57,
 'uaZqIOhviz8WjBLkrXFb': 58,
 'v8sjGmlA6nJQN3bNFld0': 59,
 'w2qWjNEKxQisfuJIjUD0': 60,
 'wF8nEh1trLJP6RtSidEf': 61,
 'wUmUgD38BvcaiTxOKejg': 62,
 'x7miOf01JROWPo2f4EQs': 63,
 'xqlSZ4b6hbEdo2VCBBO7': 64,
 'yAuBMr7ZckZWEvyeLQKQ': 65,
 'yB7gTDqhm02MkRfNXZKh': 66,
 'z3G9n3UOhqvJTnXUpt7V': 67,
 'zMGwzTYvO3kUPad6T6mr': 68}


import pandas as pd
import random

  # This gives you a number from 0 to 69 (inclusive)# import os
# print(os.getcwd())
# os.chdir("C:/Users/madha/Deskstop/MLRecommendation/MLALGO")

new_data = pd.read_csv('cosineMatrix.csv')


def findRelative(gameId):
    try:
        # Check if gameId exists in GamesId dictionary using .get() method
        index = GamesId.get(gameId)
        if index is not None:
            row = new_data.iloc[index]
        else:
            index = random.randint(0, 69)
            row = new_data.iloc[index]
        
        similar = filterData(row)
        return similar
        
    except Exception as e:
        print(f"Error in findRelative: {e}")
        # You might want to return a default value or raise the exception
        return None  # or return [] depending on what filterData returns


def filterData(row):
    gamehash = {}  # Initialize gamehash inside the function to avoid retaining data between calls
    # Loop through the games and their relativity scores
    for gameId, gawmeRelativity in zip(GamesId.keys(), row):  # Use keys() to get game IDs
        gamehash[gameId] = gameRelativity  # Add to the hash

    # Sort the games based on relativity scores in descending order
    similar = dict(sorted(gamehash.items(), key=lambda x: x[1], reverse=True))
    return similar
    


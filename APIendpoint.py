import os
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
from data  import findRelative
from flask_cors import CORS,cross_origin  # Import CORS
os.getcwd()

# Load environment variables
load_dotenv()

# Firebase configuration from environment variables
api_key = os.getenv('REACT_APP_API_KEY')
auth_domain = os.getenv('REACT_APP_AUTH_DOMAIN')
project_id = os.getenv('REACT_APP_PROJECT_ID')
storage_bucket = os.getenv('REACT_APP_STORAGE_BUCKET')
messaging_sender_id = os.getenv('REACT_APP_MESSAGING_SENDER_ID')
app_id = os.getenv('REACT_APP_APP_ID')

# Initialize Firebase with credentials and project settings
cred = credentials.Certificate("./key.json")  # Replace with your service account key path
firebase_admin.initialize_app(cred, {
    'projectId': project_id,
    'storageBucket': storage_bucket,
})

# Initialize Firestore
db = firestore.client()

app = Flask(__name__)
CORS(app)

# Function to handle new user logic
def new_user(game_id):
    data=findRelative(game_id)
    # print(data)
    return data

# Function to handle returning user logic
def history(user_data):
    return []

# Recommendation Endpoint
@cross_origin(origins='*')
@app.route('/recommendation/<user_id>', methods=['GET', 'OPTIONS'])
def recommendation(user_id):
    try:
        # print(f"Received request for user_id: {user_id}")
        print(user_id)
        
        ## Fetch document reference & Retrieve game_id and like from query parameters
        game_id = request.args.get('game_id', 'EGtPU4C72txIPUZwk2J0')  # Default game_id if not provided
        print(game_id)
        like = request.args.get('like', 'false').lower() == 'true'  # Convert the "like" parameter to boolean
        user_ref = db.collection('users').document(user_id)
        
        # Fetch document snapshot
        user = user_ref.get()  # This fetches the document snapshot
        # print(f"user snapshot: {user}")
        
        if user.exists:
            user_doc = user.to_dict()
            # print("User data:", user_doc)
            
            # Access liked and unliked games safely
            liked_games = user_doc.get('likedGames', [])
            unliked_games = user_doc.get('unlikedGames', [])
            # print(liked_games, unliked_games)
            
            # Determine which function to call based on the combined length
            if (len(unliked_games) + len(liked_games)) < 15:
                new_recommend_games = new_user(game_id)
                # 1. Sort the dictionary based on values in descending order
                sorted_games = dict(sorted(new_recommend_games.items(), key=lambda item: item[1], reverse=True))
                # 2. Select the top 15 pairs if `like=True`, else select the last 15 pairs
                top_or_bottom_games = dict(list(sorted_games.items())[:15] if like else list(sorted_games.items())[-15:])

                return jsonify(top_or_bottom_games), 200
            else:
                recommended_games = new_user(user_doc)
                return jsonify(recommended_games), 200
        else:
            print("User not found in Firestore.")
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        print("An error occurred:", e)
        return jsonify({"message": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)


# 1. (user_id, game_id, swipe)
# 2. + -> First Pref. (15)
# 3. - -> Last Items. (15)
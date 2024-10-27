import os
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

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

# Function to handle new user logic
def new_user(user_data):
     return 

# Function to handle returning user logic
def history(user_data):
    return 

# Recommendation Endpoint
@app.route('/recommendation', methods=['GET'])
def recommendation():

    user_ref = db.collection("users")
    user_doc = user_ref.stream()
    print(user_doc)
    users={}
    for doc in user_doc:
        users[doc.id]=doc.to_dict()
    # Calculate combined length of liked and unliked games
        liked_games = doc.get("likedGames")
        unliked_games = doc.get("unlikedGames")
        combined_length = len(liked_games) + len(unliked_games)
        print(combined_length)
    # Call appropriate function based on combined length
    if combined_length < 10:
        response_data = new_user(user_doc)
    else:
        response_data = history(user_doc)
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)

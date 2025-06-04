from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']   
chat_logs = db['chat_logs']  # Collection to store chat logs

app = Flask(__name__)
CORS(app) 

# Load the pre-trained model and tokenizer
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = chatbot(message, max_length=50)[0]['generated_text']
    chat_logs.insert_one({
        'user_message': message,
        'bot_response': response
    })
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)  
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import base64

load_dotenv()

app = Flask(__name__)
CORS(app)

PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
PIXABAY_API_KEY = os.getenv('PIXABAY_API_KEY')

PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PIXABAY_API_URL = "https://pixabay.com/api/"


class PerplexityChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_response(self, user_message):
        """Get response from Perplexity API"""
        payload = {
            "model": "pplx-7b-online",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "max_tokens": 1024
        }
        
        try:
            response = requests.post(PERPLEXITY_API_URL, json=payload, headers=self.headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"


class ImageSearcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_images(self, query, per_page=5):
        """Search images from Pixabay"""
        params = {
            "key": self.api_key,
            "q": query,
            "per_page": per_page,
            "image_type": "photo",
            "safesearch": True
        }
        
        try:
            response = requests.get(PIXABAY_API_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            images = []
            for hit in data.get('hits', []):
                images.append({
                    "url": hit['largeImageURL'],
                    "thumbnail": hit['previewURL'],
                    "user": hit['user']
                })
            return images
        except requests.exceptions.RequestException as e:
            return []


@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    data = request.json
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    # Get response from Perplexity
    chatbot = PerplexityChatbot(PERPLEXITY_API_KEY)
    response_text = chatbot.get_response(user_message)
    
    # Search for related images
    image_searcher = ImageSearcher(PIXABAY_API_KEY)
    images = image_searcher.search_images(user_message)
    
    return jsonify({
        "message": user_message,
        "response": response_text,
        "images": images
    })


@app.route('/api/search-images', methods=['POST'])
def search_images():
    """Search for images endpoint"""
    data = request.json
    query = data.get('query', '').strip()
    
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    image_searcher = ImageSearcher(PIXABAY_API_KEY)
    images = image_searcher.search_images(query)
    
    return jsonify({"images": images})


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

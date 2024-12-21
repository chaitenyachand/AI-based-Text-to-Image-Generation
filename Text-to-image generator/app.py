from flask import Flask, request, jsonify, render_template
import requests
import base64
import random
from PIL import Image
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Replace with your actual Hugging Face token
token = "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"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
headers = {"Authorization": f"Bearer {token}"}

translator = Translator()  # Initialize the translator

def query(prompt):
    images = []
    for _ in range(1):
        random_seed = random.randint(0, 100000)
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt, "seed": random_seed})
        if response.status_code == 200:
            images.append(response.content)
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
    return images

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.json  # Get the JSON payload from the client
    prompt = data.get('prompt', '')  # Extract the prompt from the request data

    try:
        # Translate the prompt to English
        translated_prompt = translator.translate(prompt, dest='en').text

        # Query the Hugging Face API with the translated prompt and get multiple images
        image_bytes_list = query(translated_prompt)

        # Prepare base64 strings for sending back to the client
        base64_images = [
            f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
            for image_bytes in image_bytes_list
        ]

        return jsonify(base64_images)  # Send base64 encoded images back to the client
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML template

if __name__ == '__main__':
    app.run(debug=True, port=5000)

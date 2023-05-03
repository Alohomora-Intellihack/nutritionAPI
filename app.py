from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import requests

# Import the get_nutritional_values function from the first code block
from get_nutritional_values import get_nutritional_values

# Import the Roboflow model and predict function from the second code block
from roboflow import Roboflow
rf = Roboflow(api_key="Z1RBFMNjnZcbtx4QhZ7G")
project = rf.workspace().project("food-detection-a2s1p")
model = project.version(1).model

app = Flask(__name__)
CORS(app)

@app.route('/api/nutrients', methods=['POST'])
def get_nutrients_from_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    img = Image.open(image)
    print("start")

    # Save the image temporarily
    img.save("temp.jpg")

    # Get the food name from the image

    food_data = model.predict("temp.jpg", confidence=10, overlap=30).json()
    name_data = model.predict("temp.jpg", confidence=10, overlap=30)
    class_names = []

    for prediction in food_data['predictions']:
        class_names.append(prediction['class'])

    print(class_names)

    # Extract the food name from the response
    try:
        food_name = class_names[0]
    except (IndexError, KeyError):
        return jsonify({'error': 'No food detected in the image'}), 404

    # Get the nutritional values for the food name
    nutrients = get_nutritional_values(class_names[0])

    # Return the nutritional values as JSON
    return jsonify(nutrients)

if __name__ == '__main__':
    app.run(debug=True)

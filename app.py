from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import requests
import pandas as pd
import pickle
from get_nutritional_values import get_nutritional_values
from roboflow import Roboflow
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

# Set up the Flask app
app = Flask(__name__)
CORS(app)

# Load the trained linear regression model
with open('linear_regression_model.pkl', 'rb') as file:
    linear_regression_model = pickle.load(file)


# Load the trained model and scaler
vector = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


# Import the Roboflow model and predict function from the second code block
from roboflow import Roboflow
rf = Roboflow(api_key="Z1RBFMNjnZcbtx4QhZ7G")
project = rf.workspace().project("food-detection-a2s1p")
model = project.version(1).model

# Define the API routes
@app.route('/api/nutrients', methods=['POST'])
def get_nutrients_from_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    img = Image.open(image)

    # Save the image temporarily
    img.save("temp.jpg")

    # Get the food name from the image
    food_data = model.predict("temp.jpg", confidence=10, overlap=30).json()
    class_names = [prediction['class'] for prediction in food_data['predictions']]
    food_name = class_names[0] if class_names else None

    if not food_name:
        return jsonify({'error': 'No food detected in the image'}), 404

    # Get the nutritional values for the food name
    nutrients = get_nutritional_values(food_name)

    # Return the nutritional values as JSON
    return jsonify(nutrients)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json

    # Convert the input data to a pandas DataFrame
    input_df = pd.DataFrame(input_data, index=[0])

    # Use the trained linear regression model to make a prediction on the input data
    prediction = linear_regression_model.predict(input_df)

    # Convert the prediction to a JSON response
    response = {'prediction': prediction[0]}

    return jsonify(response)


@app.route('/calories', methods=['POST'])
def calories():
    # Get the input data as a JSON object
    data = request.get_json()

    # Convert categorical variable Gender to numerical using label encoding
    le = LabelEncoder()
    data['Gender'] = le.fit_transform([data['Gender']])[0]

    # Preprocess the input data
    X = np.array([[data['Gender'], data['Age'], data['Height'], data['Weight'], data['Duration']]])
    X[:, 2:4] = scaler.transform(X[:, 2:4])

    # Make predictions using the model
    y_pred = vector.predict(X)[0]

    # Return the predictions as a JSON object
    response = {'Calories': round(float(y_pred), 2)}
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

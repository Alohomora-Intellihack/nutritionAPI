import requests
import json

# Define the input data as a JSON object
input_data = {'Gender': 'male', 'Age': 30, 'Height': 180, 'Weight': 80, 'Duration': 15}

# Send a POST request to the Flask API with the input data
url = 'http://localhost:5000/calories'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json.dumps(input_data))

# Print the response from the API
print(response.json())
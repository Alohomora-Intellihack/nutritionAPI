# NutritionAPI

## Description

NutritionAPI powers an application designed for nutrition and health. With this server, users can upload a food picture, and it will provide the nutrition information per serving in percentages. Furthermore, it can calculate your body fat percentage, pinpoint areas of excess fat, and provide exercise recommendations along with a weekly schedule to reduce the fat.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Docker (optional)

### Steps

1. Clone the repository:
   \```sh
   git clone https://github.com/Alohomora-Intellihack/nutritionAPI.git
   \```
2. Navigate to the project directory:
   \```sh
   cd nutritionAPI
   \```
3. Install the required packages:
   \```sh
   pip install -r requirements.txt
   \```
4. (Optional) Build the Docker image:
   \```sh
   docker build -t nutritionapi .
   \```

## Usage

To utilize the NutritionAPI, ensure your server is running and use the available API endpoints to upload food images and retrieve nutritional information, calculate body fat percentage, and receive personalized exercise recommendations and schedules.

### Example

```python
import requests

# Ensure the server is running and accessible at this URL
base_url = 'http://0.0.0.0:5000'

# Example 1: Get nutrients from an image
image_file_path = 'path_to_your_image_file.jpg'
with open(image_file_path, 'rb') as image_file:
    response = requests.post(f'{base_url}/api/nutrients', files={'image': image_file})
    print('Nutrients from image:', response.json())

# Example 2: Get nutrients from a food name
food_name = 'apple'
response = requests.post(f'{base_url}/api/text', json={'food_name': food_name})
print('Nutrients from name:', response.json())

```


## API Endpoints

Describe the available API endpoints, their methods (GET, POST, etc.), parameters, and usage examples.

- `/api/nutrients`: Retrieve nutritional information from an uploaded image.
  - **Method**: POST
  - **Parameters**: An image file with the key `'image'`.
  - **Usage Example**:
    ```python
    import requests

    image_file_path = 'path_to_your_image_file.jpg'
    with open(image_file_path, 'rb') as image_file:
        response = requests.post('http://0.0.0.0:5000/api/nutrients', files={'image': image_file})
        print('Nutrients from image:', response.json())
    ```
  
- `/api/text`: Retrieve nutritional information by providing the food name.
  - **Method**: POST
  - **Parameters**: JSON object containing the food name, e.g., `{"food_name": "apple"}`.
  - **Usage Example**:
    ```python
    import requests

    food_name = 'apple'
    response = requests.post('http://0.0.0.0:5000/api/text', json={'food_name': food_name})
    print('Nutrients from name:', response.json())
    ```
  
- `/predict`: [Description needed.]
  - **Method**: POST
  - **Parameters**: JSON object with input data for prediction.
  - **Usage Example**:
    ```python
    import requests

    input_data = {
        # Your input data here
    }
    response = requests.post('http://0.0.0.0:5000/predict', json=input_data)
    print('Prediction:', response.json())
    ```
  
- `/calories`: Calculate the calories based on provided data.
  - **Method**: POST
  - **Parameters**: JSON object with input data (Gender, Age, Height, Weight, Duration).
  - **Usage Example**:
    ```python
    import requests

    input_data = {
        'Gender': 'Male',
        'Age': 30,
        'Height': 180,
        'Weight': 75,
        'Duration': 30
    }
    response = requests.post('http://0.0.0.0:5000/calories', json=input_data)
    print('Calories:', response.json())
    ```
  
- `/recommend`: Receive workout recommendations and a schedule based on provided data.
  - **Method**: POST
  - **Parameters**: JSON object with input data.
  - **Usage Example**:
    ```python
    import requests

    input_data = {
        # Your input data here
    }
    response = requests.post('http://0.0.0.0:5000/recommend', json=input_data)
    print('Workout Recommendations:', response.json())
    ```

## Contributing

We welcome contributions from the community! Here's how you can contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request



## License

Include information about the license, or provide a link to the LICENSE file if it exists.

import requests

def get_nutritional_values(food_name, timezone='US/Eastern'):
    print(food_name)
    API_KEY = '9a21b5c54a3e42b36cab2b0cb964f374'
    APP_ID = '64492bba'

    url = f'https://trackapi.nutritionix.com/v2/natural/nutrients'

    headers = {
        'Content-Type': 'application/json',
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }

    data = {
        'query': food_name,
        'timezone': timezone
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

def print_nutritional_values(food_data):
    try:
        food = food_data['foods'][0]
        print(f"Nutritional values for {food['food_name']} (per {food['serving_qty']} {food['serving_unit']}):")
        print(f"  Calories: {food['nf_calories']} kcal")
        print(f"  Total Fat: {food['nf_total_fat']} g")
        print(f"  Saturated Fat: {food['nf_saturated_fat']} g")
        print(f"  Cholesterol: {food['nf_cholesterol']} mg")
        print(f"  Sodium: {food['nf_sodium']} mg")
        print(f"  Total Carbohydrate: {food['nf_total_carbohydrate']} g")
        print(f"  Dietary Fiber: {food['nf_dietary_fiber']} g")
        print(f"  Sugars: {food['nf_sugars']} g")
        print(f"  Protein: {food['nf_protein']} g")
        print(f"  Potassium: {food['nf_potassium']} mg")
        print(f"  Vitamin A: {food['nf_vitamin_a']} IU")
        print(f"  Vitamin C: {food['nf_vitamin_c']} mg")
        print(f"  Calcium: {food['nf_calcium']} mg")
        print(f"  Iron: {food['nf_iron']} mg")
    except (IndexError, KeyError):
        print('No results found.')

if __name__ == "__main__":
    food_name = 'apple'
    food_data = get_nutritional_values(food_name)
    if food_data:
        print_nutritional_values(food_data)

import os
import json
import requests

#Access AI API
api_key = os.getenv("AI_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/gpt2"
print(api_key)
headers = {"Authorization": f"Bearer {api_key}"}

def classify_brand(brand_name):
    prompt = f"Classify the clothing brand '{brand_name}' as one of the following: low, mid, expensive, or luxury. Respond with only the category name."

    def query(payload):
        print(payload)
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({"inputs": prompt})
    print(output)

    return "Luxery"

def test_api():
    prompt = f"Classify the clothing brand 'Zara' as one of the following: low, mid, expensive, or luxury. Respond with only the category name."

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response

    output = query({"inputs": prompt})
    print(output)



#Read from file
with open('klädmärken.txt', 'r', encoding='utf-8') as file:
    brands = file.readlines()

#Data cleaning and conversion to json data
brands = [brand.strip() for brand in brands]
json_data = [{'name': name, 'rating': "Luxury"} for name in brands]

#Upload to json file
with open('clothingBrands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

test_api()
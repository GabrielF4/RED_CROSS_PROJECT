import json
import requests

def classify_brand(brand_name):
    prompt = f"Classify the clothing brand '{brand_name}' as one of the following: cheap, mid, expensive, or luxury. Respond with only the category name."

    return "Luxury"

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}

#Read from file
with open('klädmärken.txt', 'r', encoding='utf-8') as file:
    brands = file.readlines()

#Data cleaning and conversion to json data
brands = [brand.strip() for brand in brands]
json_data = [{'name': name, 'rating': classify_brand(name)} for name in brands]

#Upload to json file
with open('clothingBrands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
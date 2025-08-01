import json

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}


# Open the file in read mode
with open('klädmärken.txt', 'r', encoding='utf-8') as file:
    brands = file.readlines()

# Strip newline characters and store each line as a string in a list
brands = [brand.strip() for brand in brands]

ratings = []

json_data = [{'name': name, 'rating': 'unknown'} for name in brands]

with open('clothingBrands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
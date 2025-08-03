import json

#Read from file
with open('klädmärken.txt', 'r', encoding='utf-8') as file:
    brands = file.readlines()

#Data cleaning and conversion to json data
brands = [brand.strip() for brand in brands]
print(brands)
json_data = [{'name': name, 'rating': 'unknown'} for name in brands]

#Upload to json file
with open('clothingBrands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
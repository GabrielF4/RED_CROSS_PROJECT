import os
import json
from openai import OpenAI

#Access AI API
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPEN_AI_API_KEY"),
)

#Classify brand with AI
def classify_brand(brand_name):

    response = client.responses.create(
        model="gpt-3.5-turbo",
        instructions="Always respond with either 'cheap', 'medium', 'expensive' or 'luxerious'. Nothing else.",
        input=f"Classify the clothing brand '{brand_name}' as one of the following: 'cheap', 'medium', 'expensive', or 'luxury'. Respond with only the category name. The category should be accurate to what you find when going to the store to buy clothes there."
    )

    print(response.output_text)

    return response.output_text


#Read from file
with open('klädmärken.txt', 'r', encoding='utf-8') as file:
    brands = file.readlines()

#Data cleaning and conversion to json data
brands = [brand.strip() for brand in brands]
json_data = [{'name': name, 'rating': 'unknown'} for name in brands]

#classify_brand(name).capitalize()

#Upload to json file
with open('clothingBrands.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
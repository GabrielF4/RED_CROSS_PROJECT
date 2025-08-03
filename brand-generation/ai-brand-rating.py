import os
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

#classify_brand(name).capitalize()
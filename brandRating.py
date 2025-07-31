import openai

openai.api_key = "your-api-key"

def classify_brand(brand_name):
    prompt = f"Classify the clothing brand '{brand_name}' as one of the following: cheap, mid, expensive, or luxury. Respond with only the category name."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
        temperature=0  # low temperature = more deterministic
    )

    return response.choices[0].message['content'].strip().lower()

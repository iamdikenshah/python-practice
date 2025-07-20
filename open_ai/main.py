import requests
from openai import OpenAI


open_ai_key= "Open_api_key"


open_ai = OpenAI(api_key=open_ai_key)
response = open_ai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response.choices[0].message.content)  # Output: "The 2020 World Series was played at Globe Life Field in Arlington, Texas."   
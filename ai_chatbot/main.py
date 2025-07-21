from openai import OpenAI
from dotenv import load_dotenv
import os

chat_messages = []

def main():
    load_dotenv()



def completion(message):
    open_ai_key = os.getenv("OPEN_AI_KEY")
    open_ai = OpenAI(api_key=open_ai_key)
    global chat_messages
    chat_messages.append({
                "role": "user", 
                "content": message
            }
    )
    print(f"{chat_messages}")
    response = open_ai.chat.completions.create(
        model="gpt-4o",
        messages=chat_messages
        )
    message = {
        "role":"assistant",
        "content":response.choices[0].message.content
    }
    chat_messages.append(message)
    print(f"Jarvis: {message["content"]}")



if __name__ == "__main__":
    main()
    print("Hello, I am Diken, How may I help you? (quit to exit chat): \n")
    while True:
        message = input("User: ")
        completion(message)


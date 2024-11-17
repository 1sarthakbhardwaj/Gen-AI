import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Please make sure you have set the GROQ_API_KEY in the .env file.")

client = Groq()
model_id = "llama-3.2-11b-text-preview"

# function to get response

def get_response(user_query):
    messages = [
        {"role": "user", "content": user_query}
    ]
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=messages,
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
    
    # get the main function

if __name__ == "__main__":
    print("Welcome to the Llama-powered chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("you: ")
        if user_input.lower() == exit:
            break
        response = get_response(user_input)
        print(response)



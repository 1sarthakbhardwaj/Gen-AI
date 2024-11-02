import os
import re
from together import Together
from dotenv import load_dotenv
from src.utils.context_manager import ContextManager
from src.utils.crypto_api import fetch_crypto_price
from src.utils.language_manager import translate_to_english

# Load environment variables from .env
load_dotenv()

# Initialize Together API client and context manager
api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key)
context_manager = ContextManager()

def is_crypto_query(user_message):
    match = re.search(r'price of (\w+)(?: in (\w+))?', user_message, re.IGNORECASE)
    if match:
        crypto_id = match.group(1).lower()
        currency = match.group(2).lower() if match.group(2) else "usd"
        return True, crypto_id, currency
    return False, None, None

def query_llama_model(user_message):
    # Translate user input to English if it's not in English
    user_message_in_english = translate_to_english(user_message)

    # Check for reset command
    if user_message_in_english.lower() == "reset":
        context_manager.clear_context()
        return "Conversation context has been reset. How can I help you?"

    try:
        # Check if the user is asking about a cryptocurrency price
        is_crypto, crypto_id, currency = is_crypto_query(user_message_in_english)
        if is_crypto:
            price = fetch_crypto_price(crypto_id, currency)
            if price is not None:
                response = f"The current price of {crypto_id.capitalize()} in {currency.upper()} is {price}."
            else:
                response = f"Sorry, I couldn't fetch the price of {crypto_id.capitalize()} in {currency.upper()} at the moment."
            
            context_manager.add_message("user", user_message_in_english)
            context_manager.add_message("assistant", response)
            return response

        context_manager.add_message("user", user_message_in_english)
        messages = context_manager.get_context()
        stream = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=messages,
            stream=True
        )
        response = ""
        for chunk in stream:
            response += chunk.choices[0].delta.content or ""

        context_manager.add_message("assistant", response)
        return response

    except Exception as e:
        print(f"Error querying LLaMA model: {e}")
        return "Sorry, I'm having trouble connecting to the language model."

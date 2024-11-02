from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    """
    Translates the input text to English.
    """
    try:
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Return original text if translation fails

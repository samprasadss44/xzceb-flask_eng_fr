from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translator = MyMemoryTranslator(source='en-GB', target='fr-BE')
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translator = MyMemoryTranslator(source='fr-BE', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text

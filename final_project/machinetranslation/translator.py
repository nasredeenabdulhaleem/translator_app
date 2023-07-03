"""Translator Module"""
from deep_translator import MyMemoryTranslator

#English to French Translator
def english_to_french(english_text):
    """English to French Translator"""
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    return french_text

#French to English Translator
def french_to_english(french_text):
    """French to English Translator"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    return english_text

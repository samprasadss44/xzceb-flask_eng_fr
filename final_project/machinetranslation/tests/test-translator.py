import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):

    def test_englishToFrench_hello(self):
        english = 'Hello'
        french_text = english_to_french(english)
        self.assertEqual(french_text, 'Bonjour')
  
    def test_frenchToEnglish_hello(self):
        french = 'Bonjour'
        english_text = french_to_english(french)
        self.assertEqual(english_text, 'Good Morning')

    
if __name__ == '__main__':
    unittest.main()

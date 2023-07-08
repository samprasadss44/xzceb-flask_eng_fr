import unittest
import sys
import os
from machinetranslation.translator import english_to_french, french_to_english

# Get the directory path of the translator module
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_dir)

class TranslatorTests(unittest.TestCase):

    def test_englishToFrench_hello(self):
        english = 'Hello'
        french_text = english_to_french(english)
        self.assertEqual(french_text, 'Bonjour')
  
    def test_frenchToEnglish_hello(self):
        french = 'Bonjour'
        english_text = french_to_english(french)
        self.assertEqual(english_text, 'Good Morning')



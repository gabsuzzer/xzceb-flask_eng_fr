import unittest
from translator import frenchToEnglish, englishToFrench 

class TestTranslatorFunctions(unittest.TestCase):
    def test_null_input_frenchToEnglish(self):
        result = frenchToEnglish(None)
        self.assertEqual(result, None)
    
    def test_null_input_englishToFrench(self):
        result = englishToFrench(None)
        self.assertEqual(result, None)
    
    def test_hello_to_bonjour(self):
        result = englishToFrench("Hello")
        self.assertEqual(result, "Bonjour")
    
    def test_bonjour_to_hello(self):
        result = frenchToEnglish("Bonjour")
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()

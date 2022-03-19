import unittest
  
class Tester(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # Returns True if the string is equal.
    def test_strings_a(self):
        self.assertEqual( 'abc'*4, 'abcabcabcabc')
  
    # Returns True if the string is in upper case.
    def test_upper(self):        
        self.assertEqual('teststring'.upper(), 'TESTSTRING')
  
    # Returns TRUE if the string is in uppercase and False if lower.
    def test_isupper(self):        
        self.assertTrue('TEST'.isupper())
        self.assertFalse('test'.isupper())

    # Splits the string and checks if it matches the given output.
    def test_split(self):        
        s = 'Hello world'
        self.assertEqual(s.split(), ['Hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

# used to run the code in the file
if __name__ == '__main__':
    unittest.main()
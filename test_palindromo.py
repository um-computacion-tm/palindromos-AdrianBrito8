import unittest
from palindromo import palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome("neuquen"))
        self.assertFalse(palindrome("jamon"))
        self.assertTrue(palindrome("anna"))
        
    
if __name__ == '__main__':

    unittest.main()
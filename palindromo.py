import unittest

def palindrome(word):
    if len(word) <= 1 :
        return True
    if word [0] == word[-1]:
        return palindrome(word[1: -1])
    return False

if __name__ == '__main__':

    unittest.main()
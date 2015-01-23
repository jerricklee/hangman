__author__ = 'jerrick'
import unittest
import hangman

class HanmanTestCase(unittest.TestCase):

    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

if __name__ == "__main__" :
    unittest.main()
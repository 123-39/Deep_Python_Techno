""" filter_file function tests """
import unittest

from filter_line_file import filter_file


class TestFilterFile(unittest.TestCase):

    def test_zero_find(self):

        find_sentenses = filter_file("foo.txt", ["Ваня"])

        self.assertEqual(find_sentenses, [])

    def test_correct_find(self):

        find_sentenses = filter_file("foo.txt", ["wAiT", "mE"])
        out = ["Wait right here",
               "But to me girl you're so much more than gorgeous",
               "If you give me time I could work on it",
               "Give me some time while I work on it",
               "The Earth's in rotation you're waiting for me",
               "That's why your friends always hatin' on me",
               "That's why she text me and tell me she love me",
               "I think it's funny she open up to me get comfortable with me",
               "Once I got it comin' I love her she love me",
               "I know that I'm nothing like someone the family want me to be",
               "Look at my face while you talkin' to me",
               "Shout out to everyone makin' my beats you helpin' me preach"
               ]

        self.assertEqual(find_sentenses, out)

    def test_non_full_words(self):

        find_sentenses = filter_file("foo.txt", ["wai", "talk"])

        self.assertEqual(find_sentenses, [])

    def test_non_file(self):

        find_sentenses = filter_file("fake_file.txt", ["wai", "talk"])

        self.assertEqual(find_sentenses, "There is no file 'fake_file.txt'")


if __name__ == "__main__":

    unittest.main()

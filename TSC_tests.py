import unittest
import tweet_syllable_count


class TestFunctions(unittest.TestCase):
    def test_WordCount(self):
        # test Word Count function
        self.assertEqual(tweet_syllable_count.word_count('K'), 1)
        self.assertEqual(tweet_syllable_count.word_count('Hello World'), 2)
        self.assertEqual(tweet_syllable_count.word_count('The Ball is Red'), 4)
        self.assertEqual(tweet_syllable_count.word_count(':'), 0)
        self.assertEqual(tweet_syllable_count.word_count('a'), 1)
        self.assertEqual(tweet_syllable_count.word_count('k'), 1)
        self.assertEqual(tweet_syllable_count.word_count('Be'), 1)
        self.assertEqual(tweet_syllable_count.word_count('bad'), 1)
        self.assertEqual(tweet_syllable_count.word_count('sad'), 1)
        self.assertEqual(tweet_syllable_count.word_count("they're"), 1)
        self.assertEqual(tweet_syllable_count.word_count('GOP'), 0)
        self.assertEqual(tweet_syllable_count.word_count('#MAGA'), 0)
        self.assertEqual(tweet_syllable_count.word_count('bounce'), 1)
        self.assertEqual(tweet_syllable_count.word_count('conscious'), 1)
        self.assertEqual(tweet_syllable_count.word_count('"Mother'), 1)
        self.assertEqual(tweet_syllable_count.word_count('squishy'), 1)
        self.assertEqual(tweet_syllable_count.word_count('American'), 1)
        self.assertEqual(tweet_syllable_count.word_count(
            'super-volcano'), 1)
        self.assertEqual(tweet_syllable_count.word_count(
            'smash-and-grab'), 1)
        self.assertEqual(tweet_syllable_count.word_count(
            'smash and grab'), 3)

    def test_SyllableCount(self):
        # test syllable counter function
        self.assertEqual(tweet_syllable_count.syllable_count('K'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('Hello World'), 3)
        self.assertEqual(tweet_syllable_count.syllable_count(
            'The Ball is Red'), 4)
        self.assertEqual(tweet_syllable_count.syllable_count(' '), 0)
        self.assertEqual(tweet_syllable_count.syllable_count(':'), 0)
        self.assertEqual(tweet_syllable_count.syllable_count('a'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('k'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('Be'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('bad'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('sad'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count("they're"), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('GOP'), 0)
        self.assertEqual(tweet_syllable_count.syllable_count('#MAGA'), 0)
        self.assertEqual(tweet_syllable_count.syllable_count('bounce'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('conscious'), 2)
        self.assertEqual(tweet_syllable_count.syllable_count('"Mother'), 2)
        self.assertEqual(tweet_syllable_count.syllable_count('squishy'), 2)
        self.assertEqual(tweet_syllable_count.syllable_count('American'), 4)
        self.assertEqual(tweet_syllable_count.syllable_count('college'), 2)
        self.assertEqual(tweet_syllable_count.syllable_count(
            'super-volcano'), 5)
        self.assertEqual(tweet_syllable_count.syllable_count(
            'smash-and-grab'), 3)
        self.assertEqual(tweet_syllable_count.syllable_count(
            'smash and grab'), 3)

    def test_Gettysburg(self):
        self.assertEqual(tweet_syllable_count.syllable_count('four'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('score'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('and'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('seven'), 2)
        self.assertEqual(tweet_syllable_count.syllable_count('years'), 1)
        self.assertEqual(tweet_syllable_count.syllable_count('ago'), 2)

    def test_Syllables_phrase(self):
        self.assertEqual(tweet_syllable_count.get_syllables_phrase(
            'four score, seven years ago'), 7)


class TestLiveFunctions(unittest.TestCase):
    def test_cloudhouseTweet(self):
        self.assertEqual(
            tweet_syllable_count.get_syllables_per_word('tehclubhouse').split(
                'syllable')[0], 'This tweet from @tehclubhouse has a 1.29 ')


if __name__ == '__main__':
    unittest.main(verbosity=2)

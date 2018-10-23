import unittest

import tweepy
import tweet_syllable_count

class TestFunctions(unittest.TestCase):
	def test_WordCount(self):
		#test Word Count function
		self.assertEqual(tweet_syllable_count.word_count('K'), 1)
		self.assertEqual(tweet_syllable_count.word_count('Hello World'), 2)
		self.assertEqual(tweet_syllable_count.word_count('The Ball is Red'), 4)

	def test_SyllableCount(self):
		#test syllable counter function
		self.assertEqual(tweet_syllable_count.syllable_count('a'),1)
		self.assertEqual(tweet_syllable_count.syllable_count(' '),1)
		self.assertEqual(tweet_syllable_count.syllable_count('k'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('Be'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('bounce'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('conscious'),2)


	def test_Gettysburg(self):
		self.assertEqual(tweet_syllable_count.syllable_count('four'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('score'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('and'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('seven'),2)
		self.assertEqual(tweet_syllable_count.syllable_count('years'),1)
		self.assertEqual(tweet_syllable_count.syllable_count('ago'),2)

	def test_Syllables_phrase(self):
		self.assertEqual(tweet_syllable_count.get_syllables_phrase('four score and seven years ago'),8)

class TestLiveFunctions(unittest.TestCase):
    def test_keys(self):
        self.assertEqual(tweet_syllable_count.initTwitter(), 1)
        
    def test_cloudhouseTweet(self):
        self.assertEqual(
            tweet_syllable_count.get_syllables_per_word(
                'tehclubhouse'),
                'This tweet from @tehclubhouse has a 1.11 syllable to word ratio. \n\t\thttps://twitter.com/15387997/status/530408516641886209'
            )
if __name__ == '__main__':
	unittest.main(verbosity=2)

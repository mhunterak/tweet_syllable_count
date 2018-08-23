# -*- coding: utf-8 -*-

# imports
import tweepy, time
import sys

from collections import Counter


# import twitter keys
from tw_keys import *


# variables setups


tw_auth = tweepy.OAuthHandler("TW_CONSUMER_KEY", "TW_CONSUMER_SECRET")

tw_auth=tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
tw_auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
tw_api=tweepy.API(tw_auth)

# functions
def syllable_count(word):
    word = word.lower()
    syllable_count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
            if word.endswith("e"):
                syllable_count -= 1
    if syllable_count == 0:
        syllable_count += 1
    return syllable_count

def word_count(phrase):
	return len(Counter(phrase.split()))

def get_syllables_per_word(at_user):
	user = tw_api.get_user(at_user)
	status=user.timeline()[0]
	tweet = status.text.encode('ascii', 'ignore')



	s_count=syllable_count(tweet)
	w_count=word_count(str(tweet))
	ratio = (float(s_count)/float(w_count))
	print("Tweet found.")
	print("{} syllables. {} words, {} ratio".format(
		s_count,
		w_count,
		ratio,
		))
	return """This tweet from @{} has a {} syllable to word ratio. 
		https://twitter.com/{}/status/{}""".format(
			at_user,
			"{0:.2f}".format(float(s_count)/float(w_count)),
			user.id,
			status.id
			)
at_user = 'realdonaldtrump'
print(
	"boot sequence complete. Checking for tweets from @{}".format(
		at_user))
while True:
	try:
		new_tweet = get_syllables_per_word(at_user)
		tw_api.update_status(new_tweet)
		print("Sending the following tweet:")
		print(new_tweet)
	except tweepy.error.TweepError:
		print("no new tweet found.")
	time.sleep(600000)


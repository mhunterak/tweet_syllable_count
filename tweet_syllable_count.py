# -*- coding: utf-8 -*-
# imports
import tweepy
from collections import Counter
# variables setups
# inaert twitter API keys here
TW_CONSUMER_KEY=	''
TW_CONSUMER_SECRET=	''
TW_ACCESS_TOKEN=	''
TW_ACCESS_SECRET=	''

#twitter API setup
tw_auth=tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
tw_auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
tw_api=tweepy.API(tw_auth)

# functions
# get numvwe od syllables in a string
def syllable_count(word):
    word = word.lower()
    syllable_count = 0
    vowels = "aeiouy"
    # add a syllable is the first letter is a voewl
    if word[0] in vowels:
        syllable_count += 1
    # for the rest of the word
    for index in range(1, len(word)):
    	# if a letter is a vowel, and the next letter isn't a vowel
        if word[index] in vowels and word[index - 1] not in vowels:
        	# add a syllable
            syllable_count += 1
            # if the word ends with e, it doesn't count
            if word.endswith("e"):
                syllable_count -= 1
    # if there isn't a syllable so far,
    if syllable_count == 0:
    	# make it one syllable
        syllable_count = 1
    # return the count
    return syllable_count

# get the nubmer of words in a phrase
def word_count(phrase):
	return len(Counter(phrase.split()))

# get the syllable to word ratio for a user's most recent tweet
def get_syllables_per_word(user):
	# get user
	user = tw_api.get_user(user)
	# get the most esent tweet
	status=user.timeline()[0]
	# get the status message from the tweet
	tweet = status.text.encode('ascii', 'ignore')
	# get the syllable count
	s_count=syllable_count(tweet)
	# get the word count
	w_count=word_count(str(tweet))
	# get the syllable ratio
	ratio = (float(s_count)/float(w_count))
	# return a string with the ratio message
	return """This tweet from {} has {} syllable to word ratio. 
	https://twitter.com/{}/status/{}>""".format(
		user.name,
		"{0:.2f}".format(float(s_count)/float(w_count)),
		user.id,
		status.id
		)

# send the tweet	
tw_api.update_status(
	get_syllables_per_word('realdonaldtrump'),
	)

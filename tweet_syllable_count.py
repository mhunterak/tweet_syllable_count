# -*- coding: utf-8 -*-
# imports
import datetime
import time
import tweepy
from tw_keys import *

# variables setups
# inaert twitter API keys here, or use tw_keys
'''
TW_CONSUMER_KEY=	''
TW_CONSUMER_SECRET=	''
TW_ACCESS_TOKEN=	''
TW_ACCESS_SECRET=	''
'''

#twitter API setup
def twitterSetup():
	tw_auth=tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
	tw_auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
	tw_api=tweepy.API(tw_auth)
	return tw_api

tw_api = twitterSetup()

# functions
def get_syllables_phrase(phrase):
	#split phrase into words
	words = phrase.split(' ')
	#init counter
	syllables = 0
	for word in words:
		syllables += syllable_count(word)
	return syllables

def ignore(word):
	#if true, the word is ignored and not counted
	#ignore words that start with @ and #
	if word[0] in '@#':
		return True
	#ignore words in all Caps that are more than 1, and less than 5 letters long
	if len(word) < 5 and len(word) > 1 and (word == word.upper()):
		return True
	if not word.isalpha():
		return True
	else:
		return False

def syllable_count(word): #count the number of syllables per word
	if ignore(word):
		return 0
	word = word.lower() #lowercase everthing
	syllable_count = 0 #track syllable count
	vowels = "aeiouy" # we're using vowels to detirmine syllables
	if word[0] in vowels: #if the word starts with a vowel
		syllable_count += 1 #increment syllable_count
	for index in range(1, len(word)): #for the rest of the word
		#if the letter is a vowel, and the letter before it isn't,
		if (word[index] in vowels) and (word[index - 1] not in vowels):
			syllable_count += 1 #increment syllable_count
			if word.endswith("e"): #if the word ends with "e"
				syllable_count -= 1 #deincrement syllable_count
	if syllable_count == 0: #if it's a word that doesn't have a syllable yet,
		syllable_count += 1 #increment syllable_count
	return syllable_count #return the count

def word_count(phrase): #count the number of words
	#return the number of words separated by whitespace
	counter = 0
	# split phrase into separate words
	words = phrase.split(' ')
	for word in words:
		#only count the word if it's on the ignore list
		if not ignore(word):
			counter += 1
	#return the number of words separated by whitespace
	return counter

#get the syllables to word ratio
def get_syllables_per_word(at_user):
	#get the selected user with the api
	user = tw_api.get_user(at_user)
	#get the most recent tweet
	status=user.timeline()[0]
	#get text the the tweet
	tweet = status.text.encode('ascii', 'ignore')

	#get syllable count
	s_count=get_syllables_phrase(tweet)
	#get word count
	w_count=word_count(str(tweet))
	#get the ratio
	ratio = (float(s_count)/float(w_count))

	#return the formatted text
	return """This tweet from @{} has a {} syllable to word ratio. 
		https://twitter.com/{}/status/{}""".format(
			at_user,
			"{0:.2f}".format(float(s_count)/float(w_count)),
			user.id,
			status.id
			)
#change this to target user
tracked_users = ['neiltyson','realdonaldtrump']
print 'boot sequence complete'

#loop forever - check for new tweets, then wait 10 minutes
if __name__ == '__main__':
	#print initializtion sequence
	while True:
		for user in tracked_users:
			print(
				"Checking for tweets from @{}".format(user))
			try:
				#generate ratio tweet text
				new_tweet = get_syllables_per_word(user) 
				#send the tweet - will throw exception if it's already been sent
				tw_api.update_status(new_tweet) 
				#print a sucess message
				print("Sending the following tweet:")
				print(new_tweet)
			#non unique text error
			except tweepy.error.TweepError: 
				#print failure message
				print("no new tweets, not posting right now.") 
			#print wait message
			print "{} - sleeping for ten minutes".format(datetime.datetime.now())
		#wait ten minutes
		time.sleep(600) 

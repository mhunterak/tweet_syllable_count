# -*- coding: utf-8 -*-

# imports
import datetime
import tweepy, time
from collections import Counter
# import twitter keys
from tw_keys import *


# variables setups - Twitter API initialization
tw_auth = tweepy.OAuthHandler("TW_CONSUMER_KEY", "TW_CONSUMER_SECRET")
tw_auth=tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
tw_auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
tw_api=tweepy.API(tw_auth)

# functions
def syllable_count(word): #count the number of syllables per word
    word = word.lower() #lowercase everthing
    syllable_count = 0 #track syllable count
    vowels = "aeiouy" # we're using vowels to detirmine syllables
    if word[0] in vowels: #if the word starts with a vowel
        syllable_count += 1 #increment syllable_count
    for index in range(1, len(word)): #for the rest of the word
    	#if the letter is a vowel, and the letter before it isn't,
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1 #increment syllable_count
            if word.endswith("e"): #if the word ends with "e"
                syllable_count -= 1 #increment syllable_count
    if syllable_count == 0: #if it's a word that doesn't have a syllable yet,
        syllable_count += 1 #increment syllable_count
    return syllable_count #return the count

def word_count(phrase): #count the number of words
	#return the number of words separated by whitespace
	return len(Counter(phrase.split())) #return the number of words separated by whitespace

def get_syllables_per_word(at_user): #get the syllables to word ratio
	user = tw_api.get_user(at_user) #get the selected user with the api
	status=user.timeline()[0] #get the most recent tweet
	tweet = status.text.encode('ascii', 'ignore') #get text the the tweet

	s_count=syllable_count(tweet) #get syllable count
	w_count=word_count(str(tweet)) #get word count
	ratio = (float(s_count)/float(w_count)) #get the ratio

	#return the formatted text
	return """This tweet from @{} has a {} syllable to word ratio. 
		https://twitter.com/{}/status/{}""".format(
			at_user,
			"{0:.2f}".format(float(s_count)/float(w_count)),
			user.id,
			status.id
			)


at_user = 'realdonaldtrump' #change this to target user

#print initializtion sequence
print(
	"boot sequence complete. Checking for tweets from @{}".format(
		at_user))

#loop forever - check for new tweets, then wait 10 minutes
while True:
	try:
		new_tweet = get_syllables_per_word(at_user) #generate ratio tweet text
		#send the tweet - will throw exception if it's already been sent
		tw_api.update_status(new_tweet) 
		#print a sucess message
		print("Sending the following tweet:")
		print(new_tweet)
	except tweepy.error.TweepError: #non unique text error
		print("no new tweets, not posting right now.") #print failure message
	#print wait message
	print "{} - sleeping for ten minutes".format(datetime.datetime.now())
	time.sleep(600000) #wait ten minutes


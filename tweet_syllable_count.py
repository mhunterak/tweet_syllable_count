# -*- coding: utf-8 -*-

# imports
import tweepy, time
import sys

from collections import Counter



# variables setups


TW_CONSUMER_KEY=	'512uK6qgZ3UYCIIzldubUBcH5'
TW_CONSUMER_SECRET=	'KrWuuJtvTp4y4cj9mg7O5wZk2P3lFgP3BH4wI3iHpUtnPzPGSe'
TW_ACCESS_TOKEN=	'992997820947877889-WfR69OIfhPf7wkNpY0Ilc7MOGvZCdGF'
TW_ACCESS_SECRET=	'rxksTk7m6FmAqMZu7qeBCvDDePEUH0comLsAx3OpZXKxE'


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

def get_syllables_per_word(user):
	user = tw_api.get_user(user)
	status=user.timeline()[0]
	tweet = status.text.encode('ascii', 'ignore')



	s_count=syllable_count(tweet)
	w_count=word_count(str(tweet))
	ratio = (float(s_count)/float(w_count))
	return "This tweet from {} has {} syllable to word ratio. https://twitter.com/{}/status/{}>".format(
		user.name,
		"{0:.2f}".format(float(s_count)/float(w_count)),
		user.id,
		status.id
		)



tw_api.update_status(
	get_syllables_per_word('realdonaldtrump'),
	)

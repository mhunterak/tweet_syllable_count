# -*- coding: utf-8 -*-
# imports
import datetime
import re
import time
import tweepy

import tw_keys

# variables setups
# inaert twitter API keys here, or use tw_keys
'''
TW_CONSUMER_KEY=    ''
TW_CONSUMER_SECRET=    ''
TW_ACCESS_TOKEN=    ''
TW_ACCESS_SECRET=    ''
'''


# twitter API setup
def twitterSetup():
    tw_auth = tweepy.OAuthHandler(
        tw_keys.TW_CONSUMER_KEY, tw_keys.TW_CONSUMER_SECRET)
    tw_auth.set_access_token(
        tw_keys.TW_ACCESS_TOKEN, tw_keys.TW_ACCESS_SECRET)
    tw_api = tweepy.API(tw_auth)
    return tw_api


# functions
def get_syllables_phrase(phrase):
    # split phrase into words
    words = phrase.split(' ')
    # init counter
    syllables = 0
    for word in words:
        syllables += syllable_count(word)
    return syllables


def sanitize(word):
    return re.sub("""[-'".,!?]""", '', word)


def ignore(word):
    # if true, the word is ignored and not counted
    # ignore words that start with @ and #
    if word[0] in '@#':
        return True
    # ignore words in all Caps that are more than 1, and less than 5 letters
    if len(word) < 5 and len(word) > 1 and (word == word.upper()):
        return True
    # remove all characters that are allowed in some words (like hyphens)
    word = sanitize(word)
    if not word.isalpha():
        if ''.join(list(word).pop(-1)).isalpha():
            return False
        else:
            return True
    else:
        return False


# count the number of syllables per word
def syllable_count(word):
    if ignore(word):
        return 0
    # lowercase everthing
    word = word.lower()
    # remove all characters that are allowed in some words (like hyphens)
    word = sanitize(word)
    # track syllable count
    syllable_count = 0
    # we're using vowels to detirmine syllables
    vowels = "aeiouy"
    # if the word starts with a vowel
    if word[0] in vowels:
        # increment syllable_count
        syllable_count += 1
    # for the rest of the word
    for index in range(1, len(word)):
        # if the letter is a vowel, and the letter before it isn't,
        if (word[index] in vowels) and (word[index - 1] not in vowels):
            # increment syllable_count
            syllable_count += 1
            # if the word ends with "e"
            if word.endswith("e"):
                # deincrement syllable_count
                syllable_count -= 1
    # if it's a word that doesn't have a syllable yet,
    if syllable_count == 0:
        # increment syllable_count
        syllable_count += 1
    # return the count
    return syllable_count


# count the number of words
def word_count(phrase):
    # return the number of words separated by whitespace
    counter = 0
    # split phrase into separate words
    words = phrase.split(' ')
    for word in words:
        # only count the word if it's on the ignore list
        if not ignore(word):
            counter += 1
    # return the number of words separated by whitespace
    return counter


# get the syllables to word ratio
def get_syllables_per_word(at_user):
    # get the selected user with the api
    user = tw_api.get_user(at_user)
    # get the most recent tweet
    status = user.timeline()[0]
    # get text the the tweet
    tweet = status.text.encode('ascii', 'ignore')

    # get syllable count
    s_count = get_syllables_phrase(tweet)
    # get word count
    w_count = word_count(str(tweet))
    # get the ratio
    ratio = (float(s_count)/float(w_count))

    # return the formatted text
    return """This tweet from @{} has a {} syllable to word ratio.
        https://twitter.com/{}/status/{}""".format(
            at_user,
            "{0:.2f}".format(ratio),
            user.id,
            status.id
            )


# change this to target user
tracked_users = ['neiltyson', 'realdonaldtrump']
print 'boot sequence complete'


tw_api = twitterSetup()


# loop forever - check for new tweets, then wait 10 minutes
if __name__ == '__main__':
    # print initializtion sequence
    while True:
        for user in tracked_users:
            print("Checking for tweets from @{}".format(user))
            # continue only if the tweet is loaded successfully
            cont = False
            # init Fibonacci numbers
            fibo = [0, 1]
            while cont is False:
                try:
                    # generate ratio tweet text
                    newTweet = get_syllables_per_word(user)
                    # if the tweet is loaded successfully, continue
                    cont = True
                # if an error occurs
                except tweepy.error.TweepError:
                    print ("sleeping for {} seconds".format(sum(fibo)))
                    # sleep for the Fibonacci number in seconds
                    time.sleep(sum(fibo))
                    # next Fibonacci number is the sum of the last two numbers
                    nextInt = sum(fibo)
                    # move 2nd number to the first number
                    fibo[0] = fibo[1]
                    # set 2ne number as the sum of the last two
                    fibo[1] = nextInt
            # send the tweet if it's not in the timeline
            duplicate = False
            myTwitter = tw_api.get_user('SyllableCounter')
            for myTweet in myTwitter.timeline():
                # if the new tweet has the same ratio as another recent tweet
                if (newTweet.split('https')[0]) == (
                   myTweet.text.split('https')[0]):
                    # tweet already sent
                    print 'Tweet already sent'
                    # mark it as a duplicate
                    duplicate = True
            # if it's not marked as a duplicate
            if not duplicate:
                # send the tweet
                tw_api.update_status(newTweet)
                # print a sucess message
                print("Sending the following tweet:")
                print(newTweet)
        # print wait message
        print "{} - sleeping for ten minutes".format(datetime.datetime.now())
        # wait ten minutes
        time.sleep(600)

""" 
    NEOALPACA EBOOK BOT

    Twitter: @neoalpaca
    Twitter del bot: @neoalpaca_bot
    Instagram: @neoalpacaband
    neoalpaca.rf.gd

    -----NEOALPACA EN SPOTIFY-----
"""

import random
import re
import os
import tweepy

from config import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# están todos los nombres de cosas en inglés porque es muy awkward ponerlo en español

SOURCE_TEXT = 'text.txt'
IS_TEXT_FILE = False

TWEETS = ''

#probabilidades
ALL_CAPS_ODDS = 10
FINAL_PERIOD_ODDS = 60
EXCLAMATION_ODDS = 2
INTERROGATION_ODDS = 2
ELLIPSIS_ODDS = 4 #si no se añade un punto al final, así que acaba siendo menos

MIN_LEN = 1
MAX_LEN = 50

EXCLUDED_END_START = ['y', 'de', 'un', 'o', 'a', 'son', 'los', 'se', 'la', 'en', 'y', 'con', 'las', 'el', 'como', 'nos', 'e', 'que', 'hay', 'lo', 'del', 'es']
EXCLUDED_END_CHARS = ['.', ',', '(', ')', '-', ':']
EXCLUDED = ['(', ')', '"', '”']

# mierda de twitter que ya está en config.py 
""" API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET'] """

def generate_text(tweets):

    m = 'FAILED'
    while m == 'FAILED':
        m = ''

        if IS_TEXT_FILE:
            text = open(SOURCE_TEXT, 'r', encoding='utf-8').read()
            text = ''.join([i for i in text if not i.isdigit()]).replace("\n", " ").split(' ')
        else:
            text = tweets.split()

        index = 1
        chain = {}
        length = random.randint(MIN_LEN, MAX_LEN)
        
        for word in text[index:]:
            key = text[index-1]
            if key in chain:
                chain[key].append(word)
            else:
                chain[key] = [word]
            index += 1
        
        word1 = random.choice(list(chain.keys()))
        message = word1
        
        while len(message.split(' ')) < length:
            try:
                word2 = random.choice(chain[word1])
            except KeyError:
                m = 'FAILED'
            word1 = word2
            message += ' ' + word2 
        message = message.lower()
    
        for i in range(5): #eliminar palabras del inicio y final malas
            if length != 1:
                for item in EXCLUDED_END_START:
                    message_split = message.split()
                    try:
                        if item == message_split[0]:
                            message_split.pop(0)
                    except IndexError:
                        m = 'FAILED'
                    try:
                        if item == message_split[-1]:
                            message_split.pop(-1)
                    except IndexError:
                        m = 'FAILED'
                    message = ' '.join(message_split)

        for i in range(10):
            for char in EXCLUDED_END_CHARS:
                try:
                    if char == message[-1]:
                        message = message.replace(message[-1], '')
                except IndexError:
                    m = 'FAILED'

        for character in EXCLUDED:
            message = message.replace(character, '')

        message = '. '.join(map(lambda s: s.strip().capitalize(), message.split('.')))

        if random.randint(0, 100) < 50:
            if random.randint(0, 100) < EXCLAMATION_ODDS:
                message = '¡' + message + '!'
        else:
            if random.randint(0, 100) < INTERROGATION_ODDS:
                message = '¿' + message + '?'

        try:
            if message[-1] == '!':
                pass
            else:
                if random.randint(0, 100) < FINAL_PERIOD_ODDS:
                    message = message + '.'
                
                if message[-1] != '.':
                    if random.randint(0, 100) < ELLIPSIS_ODDS:
                        message = message + '...'

        except IndexError:
            m = 'FAILED'

        if random.randint(0, 100) < ALL_CAPS_ODDS:
            message = message.upper()
        
        if length < 4 and random.randint(0, 100) < 35:
            message = message.upper()

    return message

def save_tweets():
    
    tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, id='Neoalpaca').items():
        tweets.append(tweet.text)

    #limpiar basura de los tweets, links y menciones
    text = ' '.join(tweets)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\S+", "", text)

    return text

def send_tweet(text):
    api.update_status(text)

def main():
    # loguearse
    global api
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    tweets = save_tweets()
    tweet_ready = generate_text(tweets)

    send_tweet(tweet_ready)
    print("Tweet sent: " + tweet_ready)

    
if __name__ == '__main__':
    main()
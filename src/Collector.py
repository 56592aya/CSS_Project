from slistener import SListener
import time
import sys
import tweepy
import codecs

consumer_key="oNKbn27R5HKxkCCGGeyfnQ"
consumer_secret="ifIR9VUcewWw5qn969v0hoNG2v7IOuDxtP3mEPs2swc"
access_key = "49574951-wGd6EaXhgSkW0ufN23IienrxEZeIgT06DWPZ9SY7n"
access_secret = "E2CnjvAAnWu17P25w29qunET3Az3pxRZvNl41ogBjE" 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        string = ""
        string += str(status.created_at) + '\t' +status.author.id_str + '\t' 

        for i in status.entities['hashtags']:
            string += i['text'].lower() + ','
        string += '\n'
        print string
        output.write(unicode(string).encode("utf-8"))
        return
        
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

output = open('game.txt', 'wb')
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
track = ['bulls', 'deron', 'noah', 'nets', 'nbaplayoff', 'chicago bulls', 'chicagobulls', 'BrooklynNets', 'DeronWilliams', 'deron williams', 'Joakim Noah', 'JoakimNoah', 'BrookLopez1', 'Brook Lopez', 'ReggieEvans30', 'Reggie Evans', 'TheJoeJohnson7', 'Joe Johnson', 'Gerald Wallace', 'LuolDeng9', 'Luol Deng', 'MisterCBooz', 'Carlos Boozer', 'boozer', 'mr_2eight1', 'Jimmy Butler', 'Kirk Hinrich']
sapi.filter(track=track)
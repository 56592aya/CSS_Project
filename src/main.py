from slistener import SListener
import time, tweepy, sys

## authentication
consumer_key = 'oNKbn27R5HKxkCCGGeyfnQ'
consumer_secret = 'ifIR9VUcewWw5qn969v0hoNG2v7IOuDxtP3mEPs2swc'
access_token = '49574951-wGd6EaXhgSkW0ufN23IienrxEZeIgT06DWPZ9SY7n'
access_token_secret = 'E2CnjvAAnWu17P25w29qunET3Az3pxRZvNl41ogBjE'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    track = ['rockets', 'okcthunder']
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()

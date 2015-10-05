# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
'''
Consumer Key (API Key)	qMsN2aQpK4fAmFGdruBe5di9A
Consumer Secret (API Secret)	othoTGONfw2gJuBYN4tKYNgmFpbhROqXdu91vZXSpdoFqq0hNZ
Access Level	Read and write (modify app permissions)
Owner	tpkhot93
Owner ID	3728885357

Access Token	3728885357-5eQZSpqXsnjtB5mn1QEWpMCPTXw2zpFq8JcPCKF
Access Token Secret	wN2pHegJ6rENA0dALQlgZWhUc3K4fkpW01KnzWpBfDP5m
Access Level	Read and write
Owner	tpkhot93
Owner ID	3728885357
'''
__author__ = "tejashree"
__date__ = "$Oct 5, 2015 10:06:53 AM$"

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3728885357-5eQZSpqXsnjtB5mn1QEWpMCPTXw2zpFq8JcPCKF"
access_token_secret = "wN2pHegJ6rENA0dALQlgZWhUc3K4fkpW01KnzWpBfDP5m"
consumer_key = "qMsN2aQpK4fAmFGdruBe5di9A"
consumer_secret = "othoTGONfw2gJuBYN4tKYNgmFpbhROqXdu91vZXSpdoFqq0hNZ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    seeds=["#happy", "#sad", "#disgusted", "#fearful", "#angry", "#surprised", "#scared"]


    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=seeds)
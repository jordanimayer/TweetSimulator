import markovify

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:36:50 2017

@author: Jordan Mayer, mayer15@purdue.edu

A very simple Twitter bot that replies to @Queen__Arthur
and calls her a nerd. Ignores retweets. Might ignore replies
in the future.

Mostly intended as a learning experience for the developer.

Utilizes tweepy and Molly White's twitter bot framework.
"""

# Copyright (c) 2015–2016 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import html
import tweepy
from secrets import *

# ====== Individual bot configuration ==========================
bot_username = 'ArtIsANerd'
logfile_name = bot_username + ".log"

# ==============================================================

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    while True:

        print("\nEnter the twitter handle of the account you wish to simulate")
        handle = input("@")
        print("\nHow many tweets would you like to simulate?")
        number = int(input())

        allTweets = api.user_timeline(screen_name=handle,count=10000,tweet_mode="extended")
        tweets = ""
        for tweet in allTweets:
            if not tweet.retweeted and ('RT @' not in tweet.full_text):
                tweets += tweet.full_text + "\n"
        text_model = markovify.NewLineText(tweets)
        #print(tweets)

        for i in range(number):
            print("")
            print(text_model.make_short_sentence(140))

        print("\nWould you like to do that again? (y/n)")
        ans = input()
        if ans == "n":
            break


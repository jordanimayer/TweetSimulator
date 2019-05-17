#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utilize Markov chaining to simulate tweets from a given twitter user. Uses
markovify library to learn.

Partially based on Molly White's twitter bot framework:

  Copyright (c) 2015–2016 Molly White

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS" without WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION with THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.

TODO: create own library to implement n-gram learning model

Current issues:
  Gets stuck reading some people's tweets (@sweet_susurrus, @preposterousbee)
  Will only generate one-sentence-long tweets

@author: Jordan Mayer, isaacmayer42@gmail.com
@version: 05.13.2019
"""

import tweepy
import markovify
from flask import Flask, render_template, request, redirect, Response
import random, json
from shhh import C_KEY, C_SECRET, A_TOKEN, A_TOKEN_SECRET

class TweetSimulator:
  """
  Simulate tweets (duh).

  Data attributes:
    auth: tweepy authentication handler
    api: tweepy API access
  """
  def __init__(self):
    """
    Constructor. Set up data attributes.
    """
    self.auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    self.auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    self.api = tweepy.API(self.auth)

  def simulate(self, handle, num_tweets=1):
    """
    Simulate a given number of tweets from a given user.

    Inputs:
      handle (str): twitter handle of user to simulate, without @
      num_tweets (int): number of tweets to simulate (default: 3)

    Return:
      0 on success, -1 on failure

    Example:
      sim.simulate('BarackObama')
    """

    print('\n\nSimulating tweet for @' + handle + '\n\n')

    # retrieve 10,000 most recent tweets from user
    try:
      train_tweets = self.api.user_timeline(screen_name=handle,
                                            count=10000,
                                            tweet_mode='extended')
    except tweepy.error.TweepError:
      return ('Oops! Something went wrong. Make sure the twitter handle you ' + 'entered belongs to an existing public account')

    # combine all tweets into a single string of training text
    train_text = ""
    dummy_model = markovify.Text('dummy')  # only used for test_sentence_input
    for tweet in train_tweets:
      if not tweet.retweeted and ('RT @' not in tweet.full_text):
        # ignore retweets
        text = tweet.full_text
        text.replace('\n', '. ').replace('\r', '\n')
          # markovify parses by newlines, so separate tweets by newlines and
          # replace existing newlines with periods
          # TODO: preserve newlines in tweets

        if dummy_model.test_sentence_input(text):
          # only include text markovify can handle
          train_text += text + '\n'

    text_model = markovify.NewlineText(train_text)  # train!

    # use model to make new tweet
    #sim_tweets = []
    #for i in range(num_tweets):
      #print('')
      #print(text_model.make_short_sentence(140))
    return text_model.make_short_sentence(140)


handle = ""

app = Flask(__name__)

@app.route('/')
def output():
    # serve index.html
    return render_template('index.html')

# not ideal, but it's the only way that's worked so far
@app.route('/@<handle>')
def get_tweet(handle):
    sim = TweetSimulator()
    sim_tweet = sim.simulate(handle, 1)
    return render_template('tweet.html', tweet=sim_tweet)


if __name__ == '__main__':
  """
  Accept input for username and number of tweets to generate, then simulate
  some tweets!
  """

  # sim = TweetSimulator()
  #
  # while True:
  #   print('\nEnter the twitter handle of the account you wish to simulate')
  #   handle = input('@')
  #   print('\nHow many tweets would you like to generate?')
  #   num_tweets = int(input())
  #
  #   status = sim.simulate(handle, num_tweets)
  #
  #   if status == 0:
  #     print('\nWould you like to do that again? (y/n)')
  #     ans = input()
  #     if ans == 'n':
  #       break

  app.run()

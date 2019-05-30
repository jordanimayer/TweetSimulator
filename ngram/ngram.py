# -*- coding: utf-8 -*-

"""
Use n-gram learning model to attempt to reproduce language.

@author: Jordan Mayer, isaacmayer42@gmail.com
@version: 05.29.2019
"""

import sys

def words_list(file):
  """
  Read file and return list of words in sequential order.

  Input:
    file: file in read mode

  Return:
    List of words in sequential order
  """
  if file.mode == "r":  # make sure file is in Read mode
    words = []
    lines = file.readlines()
    for line in lines:
      words.extend(line.split())
    return words
  else:
    raise ValueError("file not in Read mode")

def sentences_list(file):
  """
  Read file and return list of sentences (as strings) in sequential order.

  Input:
    file: file in read mode

  Return:
    List of words in sequential order
  """
  if file.mode == "r":  # make sure file is in Read mode
    text = file.read()
    sentences = text.split(".")
    return sentences
  else:
    raise ValueError("file not in Read mode")


def parse_text(filename, n):
  """
  Parse text file for necessary frequencies.

  Input:
    filename: path to .txt file as string
    n: number of sequential words to take into account (n-gram model)
       currently only developing for n >= 2

  Return:
    (freq_cond, freq_seq)
    freq_cond: dictionary of dictionaries of conditional frequencies
      {"word" : {"previous sequence": count(word | previous sequence)}}
    freq_seq: dictionary of sequence frequencies
      {"sequence" : count(sequence)}
  """
  file = open(filename, "r")
  sentences = sentences_list(file)  # list of all sentences in sequential order

  freq_cond = {}
  freq_seq = {}

  for sentence in sentences:
    words = sentence.split()  # list of words in sequential order
    for i in range(n-1):
      words.insert(0, "*")  # "*" indicates no previous words
                            # (start of sentence)
    for j in range(len(words) - (n-1)):
      i = j + (n-1)  # ignore starting "*" entries when generating conditionals
      w_i = words[i]  # this word
      w_prev = words[(i-(n-1)):i]  # (n-1) previous words
      prev_str = " ".join(w_prev)

      # initialize dictionary entries if necessary
      if w_i not in freq_cond:
        freq_cond[w_i] = {}
      if prev_str not in freq_cond[w_i]:
        freq_cond[w_i][prev_str] = 0
      if prev_str not in freq_seq:
        freq_seq[prev_str] = 0

      # increment counts
      freq_cond[w_i][prev_str] += 1
      freq_seq[prev_str] += 1

#  words = words_list(file)  # list of all words in sequential order
#  for i in range(n-1):
#    words.insert(0, "*")  # "*" indicates no previous words (start of text)
#  freq_cond = {}
#  freq_seq = {}
#
#  for j in range(len(words) - (n-1)):
#    i = j + (n-1)  # ignore starting "*" entries
#    w_i = words[i]  # this word
#    w_prev = words[(i-(n-1)):i]
#    prev_str = " ".join(w_prev)  # string of previous (n-1) words
#
#    if len(w_i) > 0:  # ignore empty strings
#      if w_i not in freq_cond:
#        freq_cond[w_i] = {}
#      if prev_str not in freq_cond[w_i]:
#        freq_cond[w_i][prev_str] = 0
#      if prev_str not in freq_seq:
#        freq_seq[prev_str] = 0
#      freq_cond[w_i][prev_str] += 1
#      freq_seq[prev_str] += 1

  return (freq_cond, freq_seq)

def generate_text(freq_cond, freq_seq, num_words, n):
  """
  Generate text using n-gram model.

  Inputs:
    freq_cond: conditional frequencies dictionary
    freq_seq: sequence frequencies dictionary
    num_words: number of words to generate
    n: use n-gram model

  Return:
    Generated text as string
  """

  words = ["*"] * (n-1)

  distinct_words = freq_cond.keys()
  vocab_size = len(distinct_words)

  for j in range(num_words):
    word_probs = {}

    i = j + (n-1)  # ignore starting "*" entries
    w_prev = words[(i-(n-1)):]
    prev_str = " ".join(w_prev)

    if prev_str in freq_seq:
      c_prev = freq_seq[prev_str]
    else:
      c_prev = 0

    for w in distinct_words:
      if prev_str in freq_cond[w].keys():
        c_w_after_prev = freq_cond[w][prev_str]
      else:
        c_w_after_prev = 0
      word_probs[w] = (c_w_after_prev + 1.0)/(c_prev + vocab_size)

    w_j = max(word_probs, key = lambda w: word_probs[w])
    words.append(w_j)

  generated_str = " ".join(words[(n-1):])

  return generated_str


if __name__ == "__main__":
  """
  Test things (TODO: better comment here).
  """
  # extract command line arguments
#  args = sys.argv
#  if len(args) != 4:
#    print("Usage: python ngram.py file.txt n num_words")
#    exit(0)
#  filename = args[1]
#  n = int(args[2])
#  num_words = int(args[3])
  filename = "bigsherlock.txt"
  n = 3
  num_words = 30

  freq_cond, freq_seq = parse_text(filename, n)
  print(generate_text(freq_cond, freq_seq, num_words, n))
  exit(0)  # break here for debugging
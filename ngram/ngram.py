# -*- coding: utf-8 -*-

"""
Use n-gram learning model to attempt to reproduce language.

@author: Jordan Mayer, isaacmayer42@gmail.com
@version: 05.29.2019
"""

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
  words = words_list(file)  # list of all words in sequential order
  for i in range(n-1):
    words.insert(0, "*")  # "*" indicates no previous words (start of text)
  freq_cond = {}
  freq_seq = {}

  for j in range(len(words) - (n-1)):
    i = j + (n-1)  # ignore starting "*" entries
    w_i = words[i]  # this word
    w_prev = words[(i-(n-1)):i]
    prev_str = " ".join(w_prev)  # string of previous (n-1) words

    if len(w_i) > 0:  # ignore empty strings
      if w_i not in freq_cond:
        freq_cond[w_i] = {}
      if prev_str not in freq_cond[w_i]:
        freq_cond[w_i][prev_str] = 0
      if prev_str not in freq_seq:
        freq_seq[prev_str] = 0
      freq_cond[w_i][prev_str] += 1
      freq_seq[prev_str] += 1

  return (freq_cond, freq_seq)


if __name__ == "__main__":
  """
  Test things (TODO: better comment here).
  """

  freq_cond, freq_seq = parse_text("testfile.txt", 2)
  exit(0)  # break here for debugging
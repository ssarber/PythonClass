#!/usr/local/bin/python3
print('Content-type: text/html\n')
# coding: utf-8

# ********* Lab 3 ex. 3.1 *************#
import itertools
import re

class WrongNumberOfPlayersError(Exception): pass
class NoSuchStrategyError(Exception): pass

def flatten_list(alist):
  chain = itertools.chain(*alist)
  return list(chain)

game = [["Armando", "r"], ["Dave", "s"]]

def rps_game_winner(game):
  if len(game) != 2:
      raise WrongNumberOfPlayersError('Wrong number of players!')

    # flatten the list
  game = flatten_list(game)

  # Write the code for the NoSuchStratgyError
  if game[1].lower() not in ['p', 's', 'r'] or game[3].lower() not in ['p', 's', 'r']:

          raise NoSuchStrategyError('No Such Strategy!')

  # Write the code to determine the winner
  # Paper and Rock
  if game[1].lower() == 'p' and game[3].lower() == 'r':
      winner = [game[0], game[1]]
      return winner

  elif game[1].lower() == 'r' and game[3].lower() == 'p':
      winner = [game[2], game[3]]
      return winner

  # Rock and scissors
  elif game[1].lower() == 'r' and game[3].lower() == 's':
      winner = [game[0], game[1]]
      return winner

  elif game[1].lower() == 's' and game[3].lower() == 'r':
      winner = [game[2], game[3]]
      return winner

  # Scissors and Paper
  elif game[1].lower() == 's' and game[3].lower() == 'p':
      winner = [game[0], game[1]]
      return winner

  elif game[1].lower() == 'p' and game[3].lower() == 's':
      winner = [game[2], game[3]]
      return winner


# ********* Lab 3 ex. 3.2 *************#
def sort_by_value(x):
    return x[1]

def get_numbers_from_file(file_name):

    # file_one = 'speeches/abraham_lincoln_1st.txt'
    speeches_file = open(file_name);
    speeches_file = speeches_file.read()

    stop_words = open('stop_words.txt')
    stop_words = re.split('\W+',stop_words.read())

    words = re.split('\W+',speeches_file)
    word_count = len(words)

    lines = re.split('\n',speeches_file)
    line_count = len(re.split('\n',speeches_file));

    paragraph_count = len(re.split('\n\n',speeches_file));

    # print(word_count)
    # print(line_count)

    meaningful_word_count = 0
    char_count = 0

    word_dict = {}
    meaniningful_words = {}
    i = 0
    for word in speeches_file.split():
        char_count +=len(list(word))
        word_dict[i] = word
        i = i + 1

        if word.lower() not in stop_words:
            meaningful_word_count += 1
            meaniningful_words[i] = word

    occurencies = {}
    for word in meaniningful_words:
        occurencies[word] = occurencies.get(word.lower(), 0) + 1
    # for word in occurencies:
    #     print("Word", word, "occurs", occurencies[word])
    # # not yet working, will try to get it 

    sorted_list = dict(sorted(occurencies.items(), key=lambda x:x[1], reverse = True)[:2])
    # print(sorted_list)

    print ("<pre>" + "File %s has %d paragraphs, %d lines, %d words, %d meaniningful words, %d characters.\n" % (file_name, paragraph_count, line_count, word_count, meaningful_word_count, char_count) + "</pre>")

# def get_ten_most_frequent(file_name)


get_numbers_from_file('speeches/abraham_lincoln_1st.txt')
# get_numbers_from_file('speeches/abraham_lincoln_2nd.txt')
# get_numbers_from_file('speeches/barack_obama.txt')
# get_numbers_from_file('speeches/bill_clinton_1st.txt')
# get_numbers_from_file('speeches/franklin_roosevelt_2nd.txt')
# get_numbers_from_file('speeches/john_kennedy.txt')
# get_numbers_from_file('speeches/richard_nixon.txt')
# get_numbers_from_file('speeches/ronald_reagan_1st.txt')
# get_numbers_from_file('speeches/teddy_roosevelt.txt')
# get_numbers_from_file('speeches/thomas_jefferson_1st.txt')

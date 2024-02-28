import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# print(LETTER_SCORES)


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open (DICTIONARY,'r') as file:
        file_content = [lines.strip() for lines in file.readlines()]
        return file_content

# abc = load_words()
def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    word = word.upper()
    score = sum(LETTER_SCORES.get(letter,0) for letter in word)
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    words_score = list(map(lambda word: calc_word_value(word),words))
    max_score = max(words_score)
    max_score_index = words_score.index(max_score)
    return words[max_score_index]
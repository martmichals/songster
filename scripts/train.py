"""
    Command-line script that trains a given model type, and then generates
    text once the model is trained
"""

import ast
import re
import random
from models.transition_matrix import TransitionMatrix


def preprocess_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"[^\w\d.!?\s]+", '', sentence)
    sentence = re.sub('([.,!?])', r' \1 ', sentence)
    sentence = re.sub('\s{2,}', ' ', sentence)
    return sentence


# reads in lyric data into str of lyrics
lyrics_file = open("../data/MF_DOOM_lyrics.txt", "r")
lyrics_dict = ast.literal_eval(lyrics_file.read())
lyrics_file.close()

all_lyrics = ""
for key in lyrics_dict.keys():
    song_lyrics = lyrics_dict[key].split(" ")
    for lyric in song_lyrics:
        try:
            if lyric[0].isupper():
                all_lyrics += "."
        except IndexError:
            continue
        all_lyrics += lyric + " "

transition_matrix = TransitionMatrix()
all_lyrics = all_lyrics.replace(" a ", " ")
all_lyrics = all_lyrics.replace(" an ", " ")
all_lyrics = all_lyrics.replace(" the ", " ")
all_lyrics = all_lyrics.replace(" to ", " ")
all_lyrics = all_lyrics.replace(" for ", " ")

# all_lyrics = [x.strip() for x in all_lyrics]
# all_lyrics = [x.strip() for x in all_lyrics if x != ""]

# Process file
for text in all_lyrics.split("."):
    doc = preprocess_sentence(text)
    doc = doc.split()
    length = len(doc)
    for i in range(2, length):
        transition_matrix.add_triple(doc[i-2], doc[i-1], doc[i])

matrix = transition_matrix.get_matrix()
rand_seed = random.choice(list(matrix.keys())).split(",")
# lyric_list = all_lyrics.split(" ")
word1 = rand_seed[0]
word2 = rand_seed[1]
story = word1 + " " + word2

for i in range(50):
    new_word = transition_matrix.next_word(word1, word2)
    story = story + " " + new_word
    word1 = word2
    word2 = new_word
print(story)

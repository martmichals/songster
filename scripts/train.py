"""
    Command-line script that trains a given model type, and then generates
    text once the model is trained
"""

import ast
import re
import random
from models.transition_matrix import TransitionMatrix


class TextGenerator:

    def __init__(self, file_path, song_length=50):
        lyrics_file = open(file_path, "r")
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

        all_lyrics = self.remove_stop_words(all_lyrics)
        self.transition_matrix = self.create_transition_matrix(all_lyrics)
        self.song_length = song_length

    def preprocess_sentence(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub(r"[^\w\d.!?\s]+", '', sentence)
        sentence = re.sub('([.,!?])', r' \1 ', sentence)
        sentence = re.sub('\s{2,}', ' ', sentence)
        return sentence

    def remove_stop_words(self, lyrics):
        lyrics = lyrics.replace(" a ", " ")
        lyrics = lyrics.replace(" an ", " ")
        lyrics = lyrics.replace(" the ", " ")
        lyrics = lyrics.replace(" to ", " ")
        lyrics = lyrics.replace(" for ", " ")
        lyrics = lyrics.replace("?", " ")

        return lyrics

    def create_transition_matrix(self, lyrics):
        matrix = TransitionMatrix()

        for text in lyrics.split("."):
            doc = self.preprocess_sentence(text)
            doc = doc.split()
            length = len(doc)
            for i in range(2, length):
                matrix.add_triple(doc[i - 2], doc[i - 1], doc[i])

        return matrix

    def generate_text(self):
        matrix = self.transition_matrix.get_matrix()
        rand_seed = random.choice(list(matrix.keys())).split(",")
        word1 = rand_seed[0]
        word2 = rand_seed[1]
        story = word1 + " " + word2

        for i in range(self.song_length):
            new_word = self.transition_matrix.next_word(word1, word2)
            story = story + " " + new_word
            word1 = word2
            word2 = new_word

        return story


temp = TextGenerator("../data/Taylor_Swift_lyrics.txt")
print(temp.generate_text())

import ast
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from models.transition_matrix import TransitionMatrix


class MarkovMatrixGenerator:

    def __init__(self, file_path):
        lyrics_file = open(file_path, "r")
        lyrics_dict = ast.literal_eval(lyrics_file.read())
        lyrics_file.close()

        all_lyrics = []
        for key in lyrics_dict.keys():
            song_lyrics = lyrics_dict[key].replace("START", " ").split("END")

            # tags each word in sentence and adds tagged words to list of lyrics
            for sentence in song_lyrics:
                tokenized_words = nltk.word_tokenize(sentence)
                tagged_words = nltk.pos_tag(tokenized_words)
                all_lyrics.extend(tagged_words)

        self.transition_matrix = TransitionMatrix(all_lyrics)

    def generate_text(self, song_length=50):
        matrix = self.transition_matrix.get_matrix()
        rand_seed = random.choice(list(matrix.keys()))
        word1 = rand_seed[0]
        word2 = rand_seed[1]
        story = word1[0] + " " + word2[0]

        word_count = 0
        while word_count < song_length:
            # if word_count % 10 == 0:
            #     story += "\n"

            new_word = self.transition_matrix.next_word(word1, word2)
            if new_word is None:
                # story += "\n"
                # if the given word1/word2 pair does not exist in the matrix then None is
                # returned by next_word so we get a new random key word pair and 'start over'
                rand_key = random.choice(list(matrix.keys())).split(",")
                word1 = rand_key[0]
                word2 = rand_key[1]
                story += " " + word1[0] + " " + word2[0]
                word_count += 2
            else:
                story += " " + new_word[0]
                word1 = word2
                word2 = new_word

                word_count += 1

        return story


temp2 = MarkovMatrixGenerator("../data/Taylor_Swift_lyrics2.txt")
temp2.generate_text()

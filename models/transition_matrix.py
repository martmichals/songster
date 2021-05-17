import random
import re


class TransitionMatrix:

    def __init__(self, lyrics):
        self.SparseMatrix = {}
        self.create_transition_matrix(lyrics)

    def create_transition_matrix(self, lyrics):
        for i in range(2, len(lyrics)):
            self.add_triple(lyrics[i - 2], lyrics[i - 1], lyrics[i])

    def add_triple(self, word1, word2, word3):
        key = (word1, word2)

        if key in self.SparseMatrix:
            if word3 in self.SparseMatrix[key]:
                self.SparseMatrix[key][word3] = self.SparseMatrix[key][word3] + 1
            else:
                self.SparseMatrix[key][word3] = 1
        else:
            self.SparseMatrix[key] = {word3: 1}

    def next_word(self, word1, word2):
        key = (word1, word2)
        if key in self.SparseMatrix:
            poss_words = []
            # creates list of possible third words based on frequency
            for index in range(len(self.SparseMatrix[key])):
                temp = [list(self.SparseMatrix[key].keys())[index]] * list(self.SparseMatrix[key].values())[index]
                poss_words.extend(temp)

            return random.choice(poss_words)
        else:
            return None

    def get_matrix(self):
        return self.SparseMatrix

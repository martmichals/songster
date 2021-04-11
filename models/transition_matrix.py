import random
import nltk

class TransitionMatrix:

    def __init__(self):
        self.SparseMatrix = {}

    def add_triple(self, word1, word2, word3):
        key = word1 + "," + word2

        if key in self.SparseMatrix:
            if word3 in self.SparseMatrix[key]:
                self.SparseMatrix[key][word3] = self.SparseMatrix[key][word3] + 1
            else:
                self.SparseMatrix[key][word3] = 1
        else:
            self.SparseMatrix[key] = {word3: 1}

    def next_word(self, word1, word2):
        key = word1 + "," + word2
        if key in self.SparseMatrix:
            poss_words = []
            # creates list of possible third words based on frequency
            for index in range(len(self.SparseMatrix[key])):
                temp = [list(self.SparseMatrix[key].keys())[index]] * list(self.SparseMatrix[key].values())[index]
                poss_words.extend(temp)

            return random.choice(poss_words)
            # count = sum(self.SparseMatrix[key].values())
            # rand_val = count * random.random()
            # total = 0
            # for word, idx in self.SparseMatrix[key].items():
            #     total += idx
            #     if rand_val <= total:
            #         return word
        else:
            return None


    def get_matrix(self):
        return self.SparseMatrix

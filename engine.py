from math import log2

from dataSource import DataSource
from game import compareWords


class Engine:
    dataSource = DataSource()

    def __init__(self):
        self.possibleWords = Engine.dataSource.words

    def chooseWord(self):

        file = open("output.txt", "w")

        entropies = []
        index = 0
        for word in self.possibleWords:
            index += 1
            entropies.append((word, self.computeEntropy(word)))
            if index % 500 == 0:
                print(index)

        entropies.sort(key=lambda x: x[1], reverse=True)

        for pair in entropies:
            print(pair, file=file)

        print(entropies)

    def computeEntropy(self, word):
        buckets = [0] * 243
        for secretWord in self.possibleWords:
            buckets[compareWords(secretWord, word)] += 1

        entropy = 0
        for count in buckets:
            if count == 0:
                continue
            p = count / len(self.possibleWords)
            entropy = entropy + p * (-log2(p))

        return entropy

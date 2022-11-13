from math import log2

from dataSource import DataSource
from game import compareWords


class Engine:
    dataSource = DataSource()

    def __init__(self, queue):
        self.possibleWords = Engine.dataSource.words
        self.queue = queue
        self.isFinished = False

        print(self.chooseWord())
        self.queueListener()

    def queueListener(self):
        while True:
            word, value = self.queue.get()
            if value == 242:
                break
            self.updateWords(word, value)
            print(self.chooseWord())

    def chooseWord(self):

        if len(self.possibleWords) > 10000:
            return "TAREI"
        if len(self.possibleWords) <= 1:
            return self.possibleWords[0]

        # file = open("output.txt", "w")

        # entropies = []
        # index = 0
        best_word = "aaaaa"
        max = 0
        for word in DataSource.words:
            entropy = self.computeEntropy(word)
            if max < entropy:
                max = entropy
                best_word = word

        return best_word

        # entropies.sort(key=lambda x: x[1], reverse=True)

        # for pair in entropies:
        #     print(pair, file=file)
        #
        # print(entropies)

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

    def updateWords(self, word, value):
        new_list = []
        for secretWord in self.possibleWords:
            if compareWords(secretWord, word) == value:
                new_list.append(secretWord)
        self.possibleWords = new_list
        if len(self.possibleWords) == 1:
            self.isFinished = True

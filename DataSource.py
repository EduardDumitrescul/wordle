class DataSource:
    words = []

    def __init__(self):
        file = open('cuvinte_wordle.txt', 'r')
        self.words = [word[:-1].upper() for word in file if len(word[:-1]) == 5]



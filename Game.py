from DataSource import DataSource


def wordIsValid(word):
    if len(word) != 5:
        return False
    if word not in DataSource.words:
        return False
    return True


def getGuess():
    guess_word = input("Your guess: ").upper()
    while not wordIsValid(guess_word):
        guess_word = input("Your guess is invalid. Please choose another one: ").upper()
    return guess_word


# to modify
def compareWords(word, guess):
    assert len(word) == 5
    assert len(guess) == 5

    code = [0] * 5
    for i in range(5):
        if word[i] == guess[i]:
            code[i] = 2

    for i in range(5):
        if code[i] != 0:
            continue
        for j in range(5):
            if code[j] != 0:
                continue
            if word[i] == guess[j]:
                code[j] = 1

    value = 0
    for i in code:
        value = value * 3 + i

    return value


def toBase3(value):
    ans = ""
    for i in range(5):
        ans = str(value % 3) + ans
        value //= 3
    return ans


class Game:
    dataSource = DataSource()

    def __init__(self):
        self.secretWord = None
        self.chooseRandomWord()
        print(self.secretWord)
        print("A random word has been chosen!")
        self.play()

    def chooseRandomWord(self):
        self.secretWord = self.dataSource.getRandomWord()

    def play(self):
        tries = 0
        game_finished = False
        while not game_finished:
            guess = getGuess()
            tries += 1

            if guess == self.secretWord:
                game_finished = True
                print(f"You have guessed the word in {tries} tries")
                continue

            value = compareWords(self.secretWord, guess)

            print(toBase3(value))

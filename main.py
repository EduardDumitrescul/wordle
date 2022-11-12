from game import Game, compareWords, toBase3
from engine import Engine


def startGame():
    game = Game()
    engine = Engine()
    engine.chooseWord()

    # game.play()


startGame()

from game import Game
from engine import Engine


def startGame():
    game = Game()
    engine = Engine()
    engine.chooseWord()
    # game.play()


startGame()

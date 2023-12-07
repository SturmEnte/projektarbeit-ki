from game import Game
from threading import Thread
from time import sleep

game = Game()
game_thread = Thread(target=game.start)
game_thread.start()



while True:
    sleep(0.1)
    if game.initialized:
        break

while True:
    pass # add ai stuff
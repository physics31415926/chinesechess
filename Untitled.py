from Game import Game
import random

game = Game()
step = 0
while 1:
    step += 1
    if step % 2:
        steps = game.find_steps()
    else:
        steps = game.find_steps(2)
    x, y, dx, dy = random.choice(steps)
    game.move(x, y, dx, dy)
    game.table.show()
    if game.win != 0:
        print("player" + str(game.win) + " wins !")
        break

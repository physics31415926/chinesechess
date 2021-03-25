from Table import Table
from Chess import *
import time
import random


class Game(object):
    def __init__(self):
        print("start a new game !")
        self.win = 0

        # init the chess
        self.chess = []
        self.init_chess()

        # init the table
        self.table = Table()
        self.table.show()

    def __del__(self):
        print("delete the game !")

    def find_steps(self, side=1):
        steps = []
        for chess in self.chess:
            if chess.side == side:
                steps.extend(self.find_step(chess))
        return steps

    def find_step(self, chess):
        x = chess.x
        y = chess.y
        steps = []
        # shuai and shi and bing
        if chess.type == 1 or chess.type == 2 or chess.type == 7:
            for dx, dy in chess.moves:
                if (x + dx, y + dy) in chess.range:
                    s, t = self.table.qipan[x + dx][y + dy]
                    if s != chess.side:
                        steps.append((x, y, dx, dy))
        # xiang
        elif chess.type == 3:
            for dx, dy in chess.moves:
                if (x + dx, y + dy) in chess.range:
                    if self.table.qipan[(2 * x + dx) // 2][(2 * y + dy) // 2] != (0, 0):
                        # blocked
                        continue
                    s, t = self.table.qipan[x + dx][y + dy]
                    if s != chess.side:
                        steps.append((x, y, dx, dy))
        # ma
        elif chess.type == 4:
            for dx, dy in chess.moves:
                if (x + dx, y + dy) in chess.range:
                    if abs(dx) > abs(dy):
                        bx = x + dx // 2
                        by = y
                    else:
                        bx = x
                        by = y + dy // 2
                    if self.table.qipan[bx][by] != (0, 0):
                        # blocked
                        continue
                    s, t = self.table.qipan[x + dx][y + dy]
                    if s != chess.side:
                        steps.append((x, y, dx, dy))
        # jv
        elif chess.type == 5:
            towards = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in towards:
                ax = x
                ay = y
                while 1:
                    ax += dx
                    ay += dy
                    if ax > 8 or ax < 0 or ay > 9 or ay < 0:
                        break
                    s, t = self.table.qipan[ax][ay]
                    if s == 0:
                        steps.append((x, y, ax - x, ay - y))
                        continue
                    elif s != chess.side:
                        steps.append((x, y, ax - x, ay - y))
                        break
                    else:
                        break

        # pao
        elif chess.type == 6:
            towards = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in towards:
                ax = x
                ay = y
                flag = 0  # paojia
                while 1:
                    ax += dx
                    ay += dy
                    if ax > 8 or ax < 0 or ay > 9 or ay < 0:
                        break
                    s, t = self.table.qipan[ax][ay]
                    if s == 0 and flag == 0:
                        steps.append((x, y, ax - x, ay - y))
                        continue
                    elif s != 0 and flag == 0:
                        flag = 1
                        continue
                    elif s == 0 and flag == 1:
                        continue
                    elif s != 0 and flag == 1:
                        if s == chess.side:
                            break
                        else:
                            steps.append((x, y, ax - x, ay - y))
                            break

        return steps

    def move(self, x, y, dx, dy):
        try:
            if self.table.qipan[x][y] == (0, 0):
                print("no chess to move !")
            else:
                for index, chess in enumerate(self.chess):
                    if chess.position == (x + dx, y + dy):
                        print("eat!")
                        if chess.type == 1:
                            if chess.side == 1:
                                self.win = 1
                            else:
                                self.win = 2
                            break
                        self.chess.pop(index)
                    if chess.position == (x, y):
                        chess.move(dx, dy)
                        if chess.type == 7:
                            self.cross_the_river(chess)
                self.table.qipan[x + dx][y + dy] = self.table.qipan[x][y]
                self.table.qipan[x][y] = (0, 0)
        except Exception:
            self.table.show()
            print("something is wrong")

    def cross_the_river(self, chess):
        chess.moves = [(-1, 0), (3 - 2 * chess.side, 0), (0, 1)]

    def init_chess(self):
        shuai1 = Shuai(1)
        shuai2 = Shuai(2)
        shi11 = Shi(1, 1)
        shi21 = Shi(2, 1)
        shi12 = Shi(1, 2)
        shi22 = Shi(2, 2)
        xiang11 = Xiang(1, 1)
        xiang21 = Xiang(2, 1)
        xiang12 = Xiang(1, 2)
        xiang22 = Xiang(2, 2)
        ma11 = Ma(1, 1)
        ma21 = Ma(2, 1)
        ma12 = Ma(1, 2)
        ma22 = Ma(2, 2)
        jv11 = Jv(1, 1)
        jv21 = Jv(2, 1)
        jv12 = Jv(1, 2)
        jv22 = Jv(2, 2)
        pao11 = Pao(1, 1)
        pao21 = Pao(2, 1)
        pao12 = Pao(1, 2)
        pao22 = Pao(2, 2)
        bing11 = Bing(1, 1)
        bing21 = Bing(2, 1)
        bing31 = Bing(3, 1)
        bing41 = Bing(4, 1)
        bing51 = Bing(5, 1)
        bing12 = Bing(1, 2)
        bing22 = Bing(2, 2)
        bing32 = Bing(3, 2)
        bing42 = Bing(4, 2)
        bing52 = Bing(5, 2)
        self.chess.append(shuai1)
        self.chess.append(shuai2)
        self.chess.append(shi11)
        self.chess.append(shi12)
        self.chess.append(shi21)
        self.chess.append(shi22)
        self.chess.append(xiang11)
        self.chess.append(xiang12)
        self.chess.append(xiang21)
        self.chess.append(xiang22)
        self.chess.append(ma11)
        self.chess.append(ma12)
        self.chess.append(ma21)
        self.chess.append(ma22)
        self.chess.append(jv11)
        self.chess.append(jv12)
        self.chess.append(jv21)
        self.chess.append(jv22)
        self.chess.append(pao11)
        self.chess.append(pao12)
        self.chess.append(pao21)
        self.chess.append(pao22)
        self.chess.append(bing11)
        self.chess.append(bing12)
        self.chess.append(bing21)
        self.chess.append(bing22)
        self.chess.append(bing31)
        self.chess.append(bing32)
        self.chess.append(bing41)
        self.chess.append(bing42)
        self.chess.append(bing51)
        self.chess.append(bing52)
        # print(str(len(self.chesses)) + "chesses added !")


if __name__ == "__main__":
    game = Game()

"""
    while 1:
        choices = game.findsteps()
        x, y, dx, dy = random.choice(choices)
        print("(" + str(x) + "," + str(y) + ")" + "->" + "(" + str(x + dx) + "," + str(y + dy) + ")")
        game.move(x, y, dx, dy)
        game.table.show()
        time.sleep(1)
"""

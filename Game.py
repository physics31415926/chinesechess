from Table import Table
from Chess import *
import time
import random


class Game(object):
    def __init__(self):
        print("start a new game !")
        self.win=0
        
        # init the chess
        self.chesses = []
        self.init_chesses()

        # init the table
        self.table = Table()
        self.table.show()

    def __del__(self):
        print("delete the game !")

    def findsteps(self, side=1):
        steps = []
        for chess in self.chesses:
            if chess.side == side:
                steps.extend(self.findstep(chess))
        return steps

    def findstep(self, chess):
        x = chess.x
        y = chess.y
        steps = []
        # shuai and shi and bing
        if chess.level == 1 or chess.level == 2 or chess.level == 7:
            for dx, dy in chess.moves:
                if (x + dx, y + dy) in chess.range:
                    s, t = self.table.qipan[x + dx][y + dy]
                    if s != chess.side:
                        steps.append((x, y, dx, dy))
        # xiang
        elif chess.level == 3:
            for dx, dy in chess.moves:
                if (x + dx, y + dy) in chess.range:
                    if self.table.qipan[(2 * x + dx) // 2][(2 * y + dy) // 2] != (0, 0):
                        # blocked
                        continue
                    s, t = self.table.qipan[x + dx][y + dy]
                    if s != chess.side:
                        steps.append((x, y, dx, dy))
        # ma
        elif chess.level == 4:
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
        elif chess.level == 5:
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
                        steps.append((x, y, ax - x,ay - y))
                        break
                    else:
                        break

        # pao
        elif chess.level == 6:
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
                for index, chess in enumerate(self.chesses):
                    if chess.position == (x + dx, y + dy):
                        print("eat!")
                        if chess.level==1:
                            if chess.side==1:
                                self.win=1
                            else:
                                self.win=2
                            break
                        self.chesses.pop(index)
                    if chess.position == (x, y):
                        chess.move(dx, dy)
                        if chess.level == 7:
                            self.crosstheriver(chess)
                self.table.qipan[x + dx][y + dy] = self.table.qipan[x][y]
                self.table.qipan[x][y] = (0, 0)
        except:
            self.table.show()
            print("something is wrong")


    def crosstheriver(self, chess):
        chess.moves = chess.range = [(-1, 0), (3 - 2 * chess.side, 0), (0, 1)]

    def init_chesses(self):
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
        self.chesses.append(shuai1)
        self.chesses.append(shuai2)
        self.chesses.append(shi11)
        self.chesses.append(shi12)
        self.chesses.append(shi21)
        self.chesses.append(shi22)
        self.chesses.append(xiang11)
        self.chesses.append(xiang12)
        self.chesses.append(xiang21)
        self.chesses.append(xiang22)
        self.chesses.append(ma11)
        self.chesses.append(ma12)
        self.chesses.append(ma21)
        self.chesses.append(ma22)
        self.chesses.append(jv11)
        self.chesses.append(jv12)
        self.chesses.append(jv21)
        self.chesses.append(jv22)
        self.chesses.append(pao11)
        self.chesses.append(pao12)
        self.chesses.append(pao21)
        self.chesses.append(pao22)
        self.chesses.append(bing11)
        self.chesses.append(bing12)
        self.chesses.append(bing21)
        self.chesses.append(bing22)
        self.chesses.append(bing31)
        self.chesses.append(bing32)
        self.chesses.append(bing41)
        self.chesses.append(bing42)
        self.chesses.append(bing51)
        self.chesses.append(bing52)
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

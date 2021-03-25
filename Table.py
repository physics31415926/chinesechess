side_empty = 0
side_red = 1
side_blue = 2

type_empty = 0
type_shuai = 1
type_shi = 2
type_xiang = 3
type_ma = 4
type_jv = 5
type_pao = 6
type_bing = 7


class Table(object):

    def __init__(self):
        print("creat a table !")
        self.step = 0
        self.qipan = []
        # 8x9 (side,type)
        self.have_chess = [(0, 0), (8, 0), (8, 9), (0, 9), (1, 0), (7, 0), (7, 9), (1, 9), (2, 0), (6, 0), (6, 9),
                           (2, 9), (3, 0), (5, 0), (5, 9), (3, 9), (4, 0), (4, 9), (0, 3), (8, 3), (8, 6), (0, 6),
                           (2, 3), (6, 3), (6, 6), (2, 6), (4, 3), (4, 6), (1, 2), (7, 2), (7, 7), (1, 7)]
        for i in range(9):
            a = []
            for j in range(10):
                a.append((side_empty, type_empty))
            self.qipan.append(a)
        for x, y in self.have_chess:
            self.init_chess(x, y)

    def __del__(self):
        print("delete the table !")

    def show(self):
        # print("show table !")
        for j in range(10):

            for i in range(9):
                (s, t) = self.qipan[i][9 - j]
                if t == type_empty:
                    if j == 4 or j == 5:
                        print("----", end="")
                    else:
                        print("-╋-", end="")
                elif t == type_shuai:
                    if s == side_red:
                        print("-帅-", end="")
                    else:
                        print("-将-", end="")
                elif t == type_shi:
                    if s == side_red:
                        print("-士-", end="")
                    else:
                        print("-仕-", end="")
                elif t == type_xiang:
                    if s == side_red:
                        print("-相-", end="")
                    else:
                        print("-象-", end="")
                elif t == type_ma:
                    if s == side_red:
                        print("-马-", end="")
                    else:
                        print("-馬-", end="")
                elif t == type_jv:
                    if s == side_red:
                        print("-车-", end="")
                    else:
                        print("-車-", end="")
                elif t == type_pao:
                    if s == side_red:
                        print("-炮-", end="")
                    else:
                        print("-砲-", end="")
                elif t == type_bing:
                    if s == side_red:
                        print("-兵-", end="")
                    else:
                        print("-卒-", end="")
            print("")
        print("\n")

    def init_chess(self, x, y):
        t = 0
        s = 0
        if x == 0 or x == 8:
            if y == 0 or y == 9:
                t = type_jv
            else:
                t = type_bing
        elif x == 1 or x == 7:
            if y == 0 or y == 9:
                t = type_ma
            else:
                t = type_pao
        elif x == 2 or x == 6:
            if y == 0 or y == 9:
                t = type_xiang
            else:
                t = type_bing
        elif x == 3 or x == 5:
            t = type_shi
        elif x == 4:
            if y == 0 or y == 9:
                t = type_shuai
            else:
                t = type_bing
        if y <= 4:
            s = side_red
        else:
            s = side_blue
        self.qipan[x][y] = (s, t)


if __name__ == '__main__':
    one = Table()
    one.show()

positions = []
for i in range(9):
    for j in range(10):
        positions.append((i, j))


class Chess(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = (0, 0)
        self.side = 0
        self.level = 0
        self.range = positions

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.position = (self.x,self.y)

class Shuai(Chess):

    def __init__(self, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 1
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if self.side == 1:
            self.x = 4
            self.y = 0
            self.position = (4, 0)
            self.range = [(4, 0), (3, 0), (5, 0), (3, 1), (4, 1), (5, 1), (3, 2), (4, 2), (5, 2)]
        else:
            self.x = 4
            self.y = 9
            self.position = (4, 9)
            self.range = [(4, 9), (3, 9), (5, 9), (3, 8), (4, 8), (5, 8), (3, 7), (4, 7), (5, 7)]


class Shi(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 2
        self.num = num
        self.moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        if self.side == 1:
            self.range = [(3, 0), (5, 0), (4, 1), (5, 2), (3, 2)]
            if self.num == 1:
                self.x = 3
                self.y = 0
                self.position = (3, 0)
            else:
                self.x = 5
                self.y = 0
                self.position = (5, 0)
        else:
            self.range = [(3, 9), (5, 9), (4, 8), (5, 7), (3, 7)]
            if self.num == 1:
                self.x = 3
                self.y = 9
                self.position = (3, 0)
            else:
                self.x = 5
                self.y = 9
                self.position = (5, 9)


class Xiang(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 3
        self.num = num
        self.moves = [(2, 2), (-2, -2), (2, -2), (-2, 2)]
        if self.side == 1:
            self.range = [(2, 0), (2, 4), (4, 2), (6, 0), (6, 4), (8, 2)]
            if self.num == 1:
                self.x = 2
                self.y = 0
                self.position = (2, 0)
            else:
                self.x = 6
                self.y = 0
                self.position = (6, 0)
        else:
            self.range = [(2, 9), (2, 5), (4, 7), (6, 9), (6, 5), (8, 7)]
            if self.num == 1:
                self.x = 2
                self.y = 9
                self.position = (2, 9)
            else:
                self.x = 6
                self.y = 9
                self.position = (6, 9)


class Ma(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 4
        self.num = num
        self.moves = [(1, 2), (1, -2), (2, -1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        if self.side == 1:
            if num == 1:
                self.x = 1
                self.y = 0
                self.position = (1, 0)
            else:
                self.x = 7
                self.y = 0
                self.position = (7, 0)
        else:
            if num == 1:
                self.x = 1
                self.y = 9
                self.position = (1, 9)
            else:
                self.x = 7
                self.y = 9
                self.position = (7, 9)


class Jv(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 5
        self.num = num
        if self.side == 1:
            if num == 1:
                self.x = 0
                self.y = 0
                self.position = (0, 0)
            else:
                self.x = 8
                self.y = 0
                self.position = (8, 0)
        else:
            if num == 1:
                self.x = 0
                self.y = 9
                self.position = (0, 9)
            else:
                self.x = 8
                self.y = 9
                self.position = (8, 9)


class Pao(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 6
        self.num = num
        if self.side == 1:
            if num == 1:
                self.x = 1
                self.y = 2
                self.position = (1, 2)
            else:
                self.x = 7
                self.y = 2
                self.position = (7, 2)
        else:
            if num == 1:
                self.x = 1
                self.y = 7
                self.position = (1, 7)
            else:
                self.x = 7
                self.y = 7
                self.position = (7, 7)


class Bing(Chess):

    def __init__(self, num, side=1):
        Chess.__init__(self)
        self.side = side
        self.level = 7
        self.num = num

        if side == 1:
            self.x = -2 + self.num * 2
            self.y = 3
            self.position = (self.x, self.y)
            self.range = [(self.x, self.y + 1)]
            self.moves = [(0, 1)]
        else:
            self.x = -2 + self.num * 2
            self.y = 6
            self.position = (self.x, self.y)
            self.range = [(self.x, self.y - 1)]
            self.moves = [(0, -1)]


if __name__ == "__main__":
    test = Chess()
    print("properties:" + str(test.x) + str(test.y) + str(test.position) + str(test.side))

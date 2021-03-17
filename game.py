from board import Board


class Game(object):
    def __int__(self):
        self.board = Board(10, 10)
        self.board.countNeighbords()
        self.board.printMatrix()


    def test(self):
        self.board.countNeighbords()
        """self.board.printMatrix()
        self.board.printmatrix2()"""


game = Game()
#game.board.printMatrix()

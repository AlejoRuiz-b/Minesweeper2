from board import Board


class Game(object):
    def __int__(self):
        self.board = Board(10, 10)
        self.board.countNeighbords()

    def mainDisplay(self):
        """ Print the Welcome message to the console """
        welcomeStr = "===================================\n" \
                     + "\t M I N E S W E E P E R\n" \
                     + "===================================="
        print(welcomeStr)

    def test(self):
        print("hey")
        self.mainDisplay()
        self.board.countNeighbords()
        self.board.printMatrix()
        self.board.printmatrix2()

    def askmove(self):
        while True:
            try:
                row = int(input("Please, select a row:  "))
                col = int(input("Please, select column: "))
                break
            except ValueError:
                print("\n\tOops!This is not a valid number.  Try again... /\n")
        return row, col

    def run(self):

        self.test()



'''game = Game()
game.__int__()
game.test()
index = game.askmove()

print(index[1])'''

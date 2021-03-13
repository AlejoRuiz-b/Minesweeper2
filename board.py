from cell import Cell
import numpy as np
from random import randint
import random



class Board(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # I have two options for creating a matrix:
        self.board = np.ndarray((self.rows, self.cols), dtype=Cell) # it works but I dont use it
        self.matrix = [[Cell(i, j, False, False) for j in range(cols)] for i in range(rows)]
        self.initializeboard() # If you use board, use this method. I dont use it since I'm using matrix
        self.generateMines()

# for the Board I have created an array object of Cell, however I need to initialize it
# def initialize helps me to put an object Cell in each [][] of the array
# I need to call it in the class constructor
    def initializeboard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = Cell(0, 0, 0, False)

    def printBoard(self):
        #print(self.board)
        #print(self.board[1][1].getValue())
        print(f"position: {self.matrix[1][0].positionx } {self.matrix[1][0].positiony }")

    def printMatrix(self):
        #print(np.reshape(self.matrix,(10,10)))
        #print(self.matrix[1][1].getValue())
        self.matrix[1][1].reveled=True
        self.matrix[9][9].reveled=True
        self.matrix[5][5].reveled = True

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j].reveled == False:
                    print('■ ', end=' ')

                else:
                    print(f"{self.matrix[i][j].getValue()} ", end=' ')
            print()

    def printmatrix2(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
               print(f"{self.matrix[i][j].getValue()} ", end=' ')
            print()



    def generateMines(self):
        '''for i in range(self.rows): # to put some values on the matrix
            for j in range(self.cols):
                self.matrix[i][j].value = 1
                self.board[i][j].value=1 # to make this work, board must be initialize first'''
        nbr_bomb = 0
        # while nbr_bomb <=20:
        for row in range (self.rows):
            for col in range (self.cols):
                if ( nbr_bomb <= 20):
                    i = randint(0, 9)
                    j = randint(0, 9)
                    self.matrix[i][j].value = "*"
                    nbr_bomb = nbr_bomb + 1

    def countNeighbords(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                n = 0
                if j <= 9 - 1 and self.matrix[i][j + 1].getValue() == '*':  # Droit
                    n = n + 1
                if i <= 9 - 1 and self.matrix[i + 1][j].getValue() == '*':  # au-dessous
                    n = n + 1
                if i > 0 and self.matrix[i - 1][j].getValue() == '*':  # au-dessus
                    n = n + 1
                if j > 0 and self.matrix[i][j - 1].getValue() == '*':  # gauche
                    n = n + 1
                if i <= 9 - 1 and j <= 9 - 1 and self.matrix[i + 1][j + 1].getValue() == '*':  # Diagonale inférieure droite
                    n = n + 1
                if i > 0 and j > 0 and self.matrix[i - 1][j - 1].getValue() == '*':  # Diagonale supérieure gauche
                    n = n + 1
                if i <= 9 - 1 and self.matrix[i + 1][j - 1].getValue() == '*':  # Diagonale inférieure gauche
                    n = n + 1
                if i > 0 and j <= 9 - 1 and self.matrix[i - 1][j + 1].getValue() == '*':  # Diagonale sup-droite
                    n = n + 1
                if not self.matrix[i][j].getValue() == '*':
                    #print("bombs: ",n," Position: ",self.matrix[i][j].getValue() )
                    self.matrix[i][j].setValue(n)




'''board = Board(10,10)
board.initializeboard()
board.countNeighbords()
board.printMatrix()
board.printmatrix2()'''


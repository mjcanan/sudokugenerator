import random
from random import randint
import copy

class SudNum:
    def __init__(self,num):
        self.num = num
        self.grid = -1

def getgrid(r,c):

    # tests to determine what block of the grid the number is located in, based on row and column values
    # top three grids are 0-2 left to right, then 3-5, then 6-8
    # TODO: optimize this test

    if r < 3:
        g = 0
    elif 3 <= r < 6:
        g = 3
    else:
        g = 6

    if c < 3:
        pass
    elif 3 <= c < 6:
        g = g + 1
    else:
        g = g + 2

    return g


def validnum(t,b,r,c):
    valid = True
    b[r][c].grid = t.grid

    # Search through columns to see if number already present, then see if number present in the current block

    for row in range(9):
        if t.num == b[row][c].num:
            valid = False
    if valid:
        for row in range(9):
            for col in range(9):
                if t.grid == b[row][col].grid and t.num == b[row][col].num:
                    valid = False

    return valid


def createboard(b):
    row = 0

    #.................GENERATE A COMPLETE BOARD....................#

    while row < 9:
        failed = False
        numbers = [1,2,3,4,5,6,7,8,9]

        for col in range(9):
            valid = False
            temp = SudNum(0)
            exclude = []

            # Choose a random number from numbers[] and get its grid value - eliminates need to check for values in row

            temp.num = random.choice(numbers)
            numbers.remove(temp.num)
            temp.grid = getgrid(row,col)

            while not valid:
                if validnum(temp,b,row,col):
                    b[row][col].num = temp.num
                    valid = True
                else:

                    # If the generator cannot finish a line, then the process starts over
                    # TODO: optimize clearing the board - function to generate new blank board?
                    # TODO: add iteration counter to figure out how many times this runs before it gives me a board
                    # For testing purposes

                    if not numbers:
                        failed = True
                        for r in range(9):
                            for c in range(9):
                                b[r][c].num = 0
                        break
                    else:
                        exclude.append(temp.num)
                        temp.num = random.choice(numbers)
                        numbers.remove(temp.num)
            for n in exclude:
                numbers.append(n)
            if failed:
                row = -1
                break
        row = row + 1

    #....................REMOVE NUMBERS FROM BOARD...................#

    # TODO: add Difficulty Settings
    solution = copy.deepcopy(b)
    for x in range(24):
        rowindex = randint(0,8)
        colindex = randint(0,8)
        while b[rowindex][colindex].num == "_" and b[8-rowindex][8-colindex].num == "_":
            rowindex = randint(0,8)
            colindex = randint(0,8)

        # Remove symmetrically to create common Sudoku-like configurations

        b[rowindex][colindex] = SudNum("_")
        b[8-rowindex][8-colindex] = SudNum("_")
        x = x + 1
    return solution

def printboard(b,v):
    str1 = "\n"
    line = " --------------------------------\n"
    for r in range(9):
        if r % 3 == 0:
            str1 = str1 + line
        for c in range(9):
            if c%3 == 0:
                str1 = str1 + "| "
            str1 = str1 + str(b[r][c].num) + "  "
        str1 = str1 + "|\n"
    str1 = str1 + line
    if (v):
       print(str1)
    else:
        f = open("sudoku.txt", "a")
        f.write(str1)
        f.close()




# Main Function

# TODO: put board into a function to make a blank board generator?  Sudoku class with getblank as method?

board = [
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)],
    [SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0), SudNum(0)]
    ]

sol = createboard(board)
printboard(board,1)

ans = input("Print to Text File? (Y/N): ").lower()
if ans == "y":
    (printboard(board,0))
else:
   pass

ans = input("Print Solution To Screen? (Y|N): ").lower()
if ans == "y":
    printboard(sol,1)
else:
    pass

ans = input("Print Solution To Text File? (Y|N): ").lower()
if ans == "y":
    printboard(sol,0)
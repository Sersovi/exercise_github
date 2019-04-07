import numpy as np


def board():
    size = int(input("Board size?"))
    h = 3*"-"
    v = "|"
    for i in range(size):
        print(size*(v + h)+v)


def board_shape():
    size = int(input("Board size?"))
    h = " ---"
    v = "|   "
    for i in range(size):
        print(size*(h))
        print((size+1)*(v))
    print(size*(h))


# board_shape()


"""
poss = size*[size*[None]]
"""


def create_board(size):
    board = np.random.randint(0,3,(size, size))
    print(board)
    print(3*"*")
    return board


def check_line(x):
    for i in range(3):
        if x[i][0] == x[i][1] == x[i][2]:
            if x[i][0] != 0:
                print(x[i][0], " wins bcs of line!")
                break
            else:
                continue
            break
    else:
        print("Not in lines")


def check_row(x):
    for i in range(3):
        if x[0][i] == x[1][i] == x[2][i]:
            if x[0][i] != 0:
                print(x[i][0], " wins bcs of row!")
                break
            else:
                continue
            break
    else:
        print("Not in rows.")



def check_diagonal(x):
    if x[0][0] == x[1][1] == x[2][2] or x[0][2] == x[1][1] == x[2][0]:
        if x[1][1] != 0:
            print(x[1][1], " wins bcs of diagonal!")
    else:
        print("Not in diagonal.")


def check_all(x):
    board = create_board(x)
    check_line(board)
    check_row(board)
    check_diagonal(board)


check_all(3)

'''
    for i, val1 in np.ndenumerate(poss):
        print(i[0], i[1])
        print(poss[][])


winner(3)

'''
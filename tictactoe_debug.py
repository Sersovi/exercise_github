from tictactoe import *

def check_all(x):
    board = create_board(x)
    check_line(board)
    check_row(board)
    check_diagonal(board)


#check_all(3)


def check_all2():
    board1 = np.array([[1, 2, 2], [0, 0, 2], [0, 1, 2]])
    board2 = np.array([[2, 0, 1], [1, 1, 1], [2, 2, 0]])

    #print(board1.shape, type(board1))
    #print(board2.shape, type(board2))
    #print(board1, "\n***")
    #print(board2, "\n***")

    check_line(board1)
    check_line(board2)
    check_diagonal(board1)
    check_diagonal(board2)


check_all2()
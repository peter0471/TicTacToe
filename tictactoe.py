"""
Tic Tac Toe Player
"""
import copy
import math

from numpy import Infinity


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0
    for row in board:
        for i in row:
            if i == X:
                count_X += 1
            elif i == O:
                count_O += 1
    if count_X > count_O:
        return O
    else :
        return X
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i,j))
    return actions
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != None:
        raise RuntimeError('Wrong Action')
    else:
        sym = player(board)
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = sym
        return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    check = [X,O]
    for i in range(3):
        if ((board[i][0] == board[i][1])and(board[i][1] == board[i][2])) :
            if (board[i][1] in check):
                return board[i][1]

        elif ((board[0][i] == board[1][i])and(board[1][i] == board[2][i])):
            if (board[0][i] in check):
                return board[0][i]

    if ((board[0][0] == board[1][1])and(board[1][1] == board[2][2])):
        if (board[0][0] in check):
            return board[0][0]

    elif ((board[2][0] == board[1][1])and(board[1][1] == board[0][2])):
        if (board[0][i] in check):
            return board[0][2]

    else :
        return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == None):
        if (EMPTY in board[0]) or (EMPTY in board[1]) or (EMPTY in board[2]):
            return False
        else :
            return True
    else :
        return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None :
        return 0
    #raise NotImplementedError

def min_val(board):
    A = Infinity
    if terminal(board):
        return utility(board)
    for action in actions(board):
        A = min(A,max_val(result(board,action)))
    return A

def max_val(board):
    B = -Infinity
    if terminal(board):
        return utility(board)
    for action in actions(board):
        B = max(B,min_val(result(board,action)))
    return B

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    u = []
    if player(board) == X:
        for action in actions(board):
            u.append(min_val(result(board,action)))

        return actions(board)[u.index(max(u))]

    elif player(board) == O:
        for action in actions(board):
            u.append(max_val(result(board,action))) 
        
        return actions(board)[u.index(min(u))]
    #raise NotImplementedError

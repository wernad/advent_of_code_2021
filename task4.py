import numpy as np

from utilities import get_draw_order_and_boards

draw_order, boards = get_draw_order_and_boards('4')

size = 5
boards_as_2d_arrays = [np.array(board).reshape(size, size) for board in boards]

treshold = 99999 #treshold for cells to be excluded in the winning board

def update_board(board, drawn_number):
    '''Updates the board with the drawn number. Afterward, checks if the board is the winning one.

    Args:
        board: 2D array
        drawn_number: integer
    Returns:
        True if the board is the winning one, False otherwise.
    '''
    max_value = 999999 # max value of a cell in the board to exclude in the winning board calculation
    
    for i in range(board.shape[0]):
        found_index = np.where(board[i] == drawn_number)
        if len(found_index[0]) == 1:
            board[i][found_index[0]] = max_value 
            break
    
    for i in range(board.shape[0]):
        if all(x > treshold for x in board[i]) or all(x > treshold for x in board[:, i]):
            return True
    
    return False

def find_winning_board(draw_order, boards):
    '''Replaces numbers from draw_order contained in boards with max value.

    Args:
        draw_order: list of integers
        boards: list of 2D arrays
    Returns:
        Winning boards index and last drawn number.
    '''
    
    winning_board = 0
    for number_idx, drawn_number in enumerate(draw_order):
        for board_idx, board in enumerate(boards):
            if update_board(board, drawn_number):
                return board_idx, number_idx
    return None, None

def calc_score(board, drawn_number):
    '''Calculate the score of a board.

    Args:
        board: 2D array
        drawn_number: integer
    Returns:
        Score of the board.
    '''
    # score = sum of all cells with value < max_value in the board multiplied by the drawn number
    return int(drawn_number * sum(np.concatenate([[cell for cell in row if cell < treshold] for row in board]).ravel()))

def find_last_winning_board(winning_board_index, last_number_index, draw_order, boards):
    '''Finds last winning board.
    
    Args:
        winning_board_index: integer
        last_number_index: integer
        draw_order: list of integers
        boards: list of 2D arrays
    Returns:
        Last winning boards index and last drawn number.
    '''
    del draw_order[0:last_number_index]
    
    while len(boards) > 1: # remove winning boards until there is only one left
        winning_board_index, drawn_number = find_winning_board(draw_order, boards)
        boards.pop(winning_board_index)
    winning_board_index, drawn_number = find_winning_board(draw_order, boards) # last winning board

    return winning_board_index, drawn_number



#Part 1
winning_board_index, last_number_index = find_winning_board(draw_order, boards_as_2d_arrays)
winning_board_score = calc_score(boards_as_2d_arrays[winning_board_index], draw_order[last_number_index])
print('Part 1:', winning_board_score)

#Part 2
winning_board_index, last_number_index = find_last_winning_board(winning_board_index, last_number_index, draw_order, boards_as_2d_arrays)
winning_board_score = calc_score(boards_as_2d_arrays[winning_board_index], draw_order[last_number_index])
print('Part 2:', winning_board_score)




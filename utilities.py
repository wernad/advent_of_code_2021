from itertools import groupby
import re

def get_file_name(name):
    '''Get path to the file from input.

    Args:
        name: string
    Returns:
        file path as string
    '''
    return 'input/input' + name + '.txt'

def get_2d_int_array(name):
    '''Get 2d array from file. Each line is a row.
    Args:
        name: string
    Returns:
        list of lists
    '''
    with open(get_file_name(name), 'r') as f:
        lines = [x.rstrip('\n') for x in f.readlines()]
        array = [list(map(int, list(line))) for line in lines]
    return array

def get_numbers(name):
    '''Open file and read numbers on 1st line.

    Args:
        name: string
    Returns:
        list of integers
    '''
    with open(get_file_name(name), 'r') as f:

        numbers = [int(x) for x in f.readline().split(',')]
    return numbers

def get_numbers_on_lines(name):
    '''Open file and read numbers on lines.

    Args:
        name: string
    Returns:
        list of integers
    '''
    with open(get_file_name(name), 'r') as f:

        numbers = [int(x) for x in f.readlines()]
    return numbers

def get_lines(name):
    '''Open file and read lines.

    Args:
        name: string
    Returns:
        list of strings
    '''
    with open(get_file_name(name), 'r') as f:
        lines = [x.rstrip('\n') for x in f.readlines()]
    return lines

def get_draw_order_and_boards(name):
    '''Open file and read first line and subsequent groups of lines.

    Args:
        name: string
    Returns:
        List of integers and list of 2D arrays
    '''
    with open(get_file_name(name), 'r') as f:
        lines = [x.rstrip('\n') for x in f.readlines()]
        draw_order, boards = lines[0], lines[1:]

        draw_order = [int(x) for x in draw_order.split(',')]

        boards = [list(g) for k, g in groupby(boards, key=bool) if k]

        new_boards = []
        for board in boards:
            rows = [[int(cell) for cell in row.split(' ') if cell] for row in board]
            new_boards.append(rows)
    
    return draw_order, new_boards

def get_lines_coordinates(name):
    '''Open file and get coordinates of lines.

    Args:
        name: string
    Returns:
        list of tuples
    '''

    with open(get_file_name(name), 'r') as f:
        lines = [x.rstrip('\n') for x in f.readlines()]
        coordinates = [(tuple(map(int, A.split(','))), tuple(map(int, B.split(',')))) for A, B in [line.split(' -> ') for line in lines]]

    return coordinates

def get_digits(name):
    '''Open file and read encoded digits.

    Args:
        name: string
    Returns:
        list of encoded digits
        list of decoded digits
    '''

    with open(get_file_name(name), 'r') as f:
        digits = [x.strip('\n').split(' | ') for x in f.readlines()]
    return digits

def get_file(name):
    '''Open file and read content as single line.

    Args:
        name: string
    Returns:
        string
    '''

    with open(get_file_name(name), 'r') as f:
        content = f.read()
    return content
from utilities import get_lines

puzzle_input = get_lines('1')
puzzle_input = [int(x) for x in puzzle_input]

def compare(values):
    '''Compare neighboring integers in a list and increment counter everytime the second integer is larger. 

    Args:
        values: list of integers
    Returns:
        count: number of increments
    '''
    count = 0

    for i in range(len(values)-1):
        if values[i] < values[i+1]:
            count += 1
    
    return count

def compare_window(values):
    '''Compare outputs of sliding_window function for two neighbouring integers. Increment counter everytime the second output is larger.
    
    Args:
        values: list of integers
    Returns:
        count: number of increments
    '''

    def get_window(values, i):
        '''Get sum of three integers from list. Starting from index i.
        '''
        return sum(values[i:i+3])

    count = 0

    for i in range(len(values)-2):
        if get_window(values, i) < get_window(values, i+1):
            count += 1
    
    return count

#Part 1
print('Part 1:', compare(puzzle_input))
#Part 2
print('Part 2:', compare_window(puzzle_input))
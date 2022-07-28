
import numpy as np
import collections as cl

from utilities import get_2d_int_array

puzzle_input = get_2d_int_array('3')
input_as_2d_array = np.array(puzzle_input, dtype=str)

def get_most_frequent_bit(array, column):
    '''Pick most numerous bit in a column in 2d array.

    Args:
        array: 2D array
        column: integer
    Returns:
        Most frequent bit.
    '''
    counts = cl.Counter((array[:, column])).most_common(2)
    if counts[0][1] == counts[1][1]:
        return '1'
    return counts[0][0]

def get_least_frequent_bit(array, column):
    '''Pick least frequent bit in a column in 2d array.

    Args:
        array: 2D array
    Returns:
        Least frequent bit.
    '''
    counts = cl.Counter((array[:, column])).most_common(2)
    if counts[0][1] == counts[1][1]:
        return '0'
    return counts[1][0]

def calc_gamma_rate(array):
    '''Create a binary number from most numerous bits and convert it to decimal.
    
    Args:
        array: 2D array
    Returns:
        integer
    '''
    return int(''.join([get_most_frequent_bit(array, i) for i in range(array.shape[1])]), 2)

def calc_epsilon_rate(array):
    '''Create a binary number from least numerous bits and convert it to decimal.

    Args:
        array: 2D array
    Returns:
        integer
    '''
    return int(''.join([get_least_frequent_bit(array, i) for i in range(array.shape[1])]), 2)

def calc_oxygen_generator_rating(array):
    '''Finds binary number that contains the most frequent bits.

    Args:
        array: 2D array
    Returns:
        integer
    '''

    current_array = array.copy()
    new_array = []
    for i in range(current_array.shape[1]):
        if len(current_array) == 1:
            break

        most_frequent_bit = get_most_frequent_bit(current_array, i)

        new_array = [x for x in current_array if x[i] == most_frequent_bit]
        current_array = np.array(new_array)

    return int(''.join(np.concatenate(current_array).ravel()), 2)
    
def calc_CO2_scrubber_rating(array):
    '''Finds binary number that contains the least frequent bits.
    
    Args:
        array: 2D array
    Returns:
        integer
    '''
    
    current_array = array.copy()
    new_array = []
    for i in range(current_array.shape[1]):
        if len(current_array) == 1:
            break
        
        least_frequent_bit = get_least_frequent_bit(current_array, i)

        new_array = [x for x in current_array if x[i] == least_frequent_bit]
        current_array = np.array(new_array)

    return int(''.join(np.concatenate(current_array).ravel()), 2)
        
#Part 1
print('Part 1:', calc_gamma_rate(input_as_2d_array) * calc_epsilon_rate(input_as_2d_array))
#Part 2
print('Part 2:', calc_oxygen_generator_rating(input_as_2d_array) * calc_CO2_scrubber_rating(input_as_2d_array))

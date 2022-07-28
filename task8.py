from collections import Counter
import re

from utilities import get_digits

puzzle_input = get_digits('8')
input_digits, output_digits = zip(*puzzle_input)

def count_unique(digits):
    '''Counts number of strings that are 2, 3, 4 or 7 characters long.

    Args:
        digits: list of strings, where each string contains multiple digits coded via characters
    Returns:
        Integer representing the total count.
    '''

    total_count = 0
    for entry in digits:
        total_count += sum([1 for digit in entry.split() if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7])

    return total_count
       
def get_unique_segment_digits(digit_entry):
    '''Finds segment representation of digits 1, 4, 7 and 8.

    Args:
        digit_entry: list of strings representing digits
    Returns:
        Dictionary with numbers as keys and corresponding strings (segments) as values
    '''

    digit_segments = {1: '', 4: '', 7: '', 8: ''}
    for digit in digit_entry:
        if len(digit) == 2:
            digit_segments[1] = digit
        elif len(digit) == 3:  
            digit_segments[7] = digit
        elif len(digit) == 4:
            digit_segments[4] = digit
        elif len(digit) == 7:
            digit_segments[8] = digit
    
    return digit_segments



def remove_segments(segments, pattern):
    '''Removes characters in pattern from segments.
    Args:
        segments: list of strings representing segments
        pattern: string representing characters to remove
    Returns:
        String after removal of pattern.
    '''
    
    for char in pattern:
        segments = segments.replace(char, '')
    return segments

def get_six_segment_digits(digit_entry, digit_four, digit_seven):
    '''Finds digits 0, 6 and 9 in digit_entry.

    Args:
        digit_entry: list of strings representing digits
    Returns:
        Dictionary with digits as keys and their segment representation as values.
    '''
    six_segment_digits = {0: '', 6: '', 9: ''}
    
    for digit in digit_entry:
        if len(remove_segments(digit, digit_four)) == 2:
            six_segment_digits[9] = digit
            continue
        if len(remove_segments(digit, digit_seven)) == 3:
            six_segment_digits[0] = digit
            continue
        else:
            six_segment_digits[6] = digit

    return six_segment_digits

def get_five_segment_digits(digit_entry, digit_one, digit_four):
    '''Finds digits 2, 3 and 5 in digit_entry.

    Args:
        digit_entry: list of strings representing digits
    Returns:
        Dictionary with digits as keys and their segment representation as values.
    '''
    six_segment_digits = {2: '', 3: '', 5: ''}
    
    for digit in digit_entry:
        if len(remove_segments(digit, digit_one)) == 3:
            six_segment_digits[3] = digit
            continue
        if len(remove_segments(digit, digit_four)) == 2:
            six_segment_digits[5] = digit
            continue
        else:
            six_segment_digits[2] = digit

    return six_segment_digits


def sum_decoded_digits(input_digits, output_digits):
    '''Decodes digits for each entry in puzzle_input and sums decoded output parts. Digits in output are concatenated into number before summing.

    Args:
        digits: list of digit entries, consiting of input digits and output digits.
    Return:
        Integer representing the sum of output digits.
    '''

    total_sum = 0
    for in_dig, out_dig in zip(input_digits, output_digits):
        decoded_digits = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''} 
        digits_combined = str(in_dig + ' ' + out_dig).split() # Combines input and output digits into single entry.
        
        digits_by_length = {5: [], 6: []} # Digits with non-unique segment lengths. Segment = single character.
        for digit in digits_combined:
            if len(digit) == 5:
                digits_by_length[5].append(digit)
            elif len(digit) == 6:
                digits_by_length[6].append(digit)

        decoded_digits.update(get_unique_segment_digits(digits_combined)) # 1, 4, 7, 8
        decoded_digits.update(get_six_segment_digits(digits_by_length[6], decoded_digits[4], decoded_digits[7])) # 0, 6, 9
        decoded_digits.update(get_five_segment_digits(digits_by_length[5], decoded_digits[1], decoded_digits[4])) # 2, 3, 5
        
        inverted_decoded_digits = {str(sorted(v)): k for k, v in decoded_digits.items()} # Inverting and sorting values and keys for easier processing on next line.

        total_sum += int(''.join(map(str, [inverted_decoded_digits[str(sorted(digit))] for digit in out_dig.split()])))
        
    return total_sum
    


# Part 1
print('Part 1:', count_unique(output_digits))

# Part 2
print('Part 2:', sum_decoded_digits(input_digits, output_digits))
import re
import numpy as np

from utilities import get_lines

puzzle_input = get_lines('13')
separator_idx = puzzle_input.index('')

dots = [re.search(r'\d*,\d*', x).group(0) for x in puzzle_input[:separator_idx]] # dot eg.: '3,4'
folding_rules = [re.search(r'fold along ((x|y)=\d*)', x).group(1) for x in puzzle_input[separator_idx + 1:]] # rule eg.: 'x=3'

max_x = max([int(x.split(',')[0]) for x in dots])
max_y = max([int(y.split(',')[1]) for y in dots])

paper_array = np.chararray((max_y + 1, max_x + 1), unicode=True)
paper_array[:] = '.'

# Fill array with dots (#)
for dot in dots:
    x, y = [int(x) for x in dot.split(',')]
    paper_array[y, x] = '#'

def fold(paper_array, folding_rules, first_step_only=False):
    '''Fold paper_array according to folding rules.

    x rules fold array around y axis.
    y rules fold array around x axis.
    Args:
        paper_array: numpy integer array. 1's represent dots.
        folding_rules: list of strings.
    Returns:
        Numpy integer array after folding.
    '''

    paper_array_copy = paper_array.copy()
    for folding_rule in folding_rules:
        if folding_rule.startswith('x='):
            x_fold_idx = int(folding_rule.split('=')[1])

            left_side = paper_array_copy[:, :x_fold_idx]
            right_side = paper_array_copy[:, x_fold_idx + 1:]
            right_side = np.flip(right_side, axis=1)
            
            paper_array_copy = left_side + right_side
            paper_array_copy[paper_array_copy.find('#') != -1] = '#'

        elif folding_rule.startswith('y='):
            y_fold_idx = int(folding_rule.split('=')[1])
            
            up_side = paper_array_copy[:y_fold_idx, :]
            bottom_side = paper_array_copy[y_fold_idx + 1:, :]
            bottom_side = np.flip(bottom_side, axis=0)
            
            paper_array_copy = bottom_side + up_side
            paper_array_copy[paper_array_copy.find('#') != -1] = '#'

        if first_step_only: # For part 1
            break

    return paper_array_copy

# Part 1
array_after_one_step = fold(paper_array, folding_rules, True)
print('Part 1:', np.count_nonzero(array_after_one_step == '#'))

# Part 2
paper_array = fold(paper_array, folding_rules)

paper_array[paper_array.find('.') != -1] = '.' # Remove excessive dots.

print('Part 2:')
print('\n'.join(''.join(' ' if character == '.' else character for character in line ) for line in paper_array))
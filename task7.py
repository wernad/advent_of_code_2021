from statistics import median, mean

from utilities import get_numbers

puzzle_input = get_numbers('7')

#Part 1
best_position = int(median(puzzle_input))

#Sum of distances between numbers in input and the best_position.
print('Part 1:', sum(map(lambda x: abs(x - best_position), puzzle_input)))

#Part 2
new_best_position = int(mean(puzzle_input))

#Sum of sums of ranges from 0 to distances between numbers in input and the best_position.
print('Part 2:', sum(map(lambda x: sum(range(1, abs(x - new_best_position) + 1)), puzzle_input)))
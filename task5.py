from collections import Counter, defaultdict

from utilities import get_lines_coordinates

coordinates = get_lines_coordinates('5')

all_x_values = [coord[0][0]  for coord in coordinates] + [coord[0][1] for coord in coordinates]
all_y_values = [coord[0][1]  for coord in coordinates] + [coord[1][1] for coord in coordinates]

max_x = max(all_x_values) + 1
max_y = max(all_y_values) + 1

def create_grid_no_diagonals(coordinates):
    '''Create dictionary with coordinates of horizontal and vertical lines.

    Args:
        coordinates: list of tuples with start and end coordinates
    Returns:
        Dictionary with coordinates as keys and their counts as values.
    '''

    grid = defaultdict(int)

    non_diag_coordinates = [coord for coord in coordinates if coord[0][0] == coord[1][0] or coord[0][1] == coord[1][1]]
    for coord in non_diag_coordinates:
        x_range, y_range = get_ranges(coord)
        
        for x in x_range:
            for y in y_range:
                grid[(x, y)] += 1
    
    return grid

def create_grid_only_diagonals(coordinates):
    '''Create dictionary with coordinates of diagonals lines only.

    Args:
        list of tuples with start and end coordinates
    Returns:
        Dictionary with coordinates as keys and their counts as values.
    '''
    
    grid = defaultdict(int)

    diag_coordinates = [coord for coord in coordinates if coord[0][0] != coord[1][0] and coord[0][1] != coord[1][1]]
    for coord in diag_coordinates:
        x_range, y_range = get_ranges(coord) 
        
        for x, y in zip(list(x_range),list(y_range)):
            grid[(x, y)] += 1
    
    return grid

def get_ranges(coordinates):
    '''Get ranges of x and y values from coordinates in correct format for diagonals.

    Args:
        coordinates: list of tuples with start and end coordinates
    Returns:
        Tuple with ranges of x and y values.
    '''

    if coordinates[0][0] <= coordinates[1][0]:
        x_range = range(coordinates[0][0], coordinates[1][0] + 1)
    else:
        x_range = range(coordinates[0][0], coordinates[1][0] - 1, -1)
    
    if coordinates[0][1] <= coordinates[1][1]:
        y_range = range(coordinates[0][1], coordinates[1][1] + 1)
    else:
        y_range = range(coordinates[0][1], coordinates[1][1] - 1, -1)
    
    return (x_range, y_range)    

#Part 1
no_diagonals_grid = create_grid_no_diagonals(coordinates)
print('Part 1:', len([x for x in no_diagonals_grid.values() if x > 1]))

#Part 2
diagonals_grid = create_grid_only_diagonals(coordinates)
count = sum((Counter(dict(x)) for x in [no_diagonals_grid, diagonals_grid]), Counter()) #Count all coordinate occurences from both dictionaries.
print('Part 2:', len([x for x in count.values() if x > 1]))
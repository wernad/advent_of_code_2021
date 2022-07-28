from utilities import get_2d_int_array

cave_system = get_2d_int_array('9')

max_row, max_col = len(cave_system), len(cave_system[0])

def get_corner(row, col):
    '''Tries to retrieve corner from dictionary based on coordinates. If not found, returns None.
    Args:
        row: int representing row
        col: int representing column
    Returns:
        int representing corner or None if not found
    '''
    corners = {(0, 0): 0, (0, max_col-1): 1, (max_row-1, 0): 2, (max_row-1, max_col-1): 3}
    
    return corners.get((row, col), None)

def get_side_point(row, col):
    '''Check if point is no the edge of cave system.
    Args:
        row: int representing row
        col: int representing column
    Returns:
        Boolean, True for edge, False for not.
    '''
    
    if row == 0 or row == max_row-1 or col == 0 or col == max_col-1:
        return True
    return False

def check_neighborhood(row, col):
        '''Check the neighborhood of a point that's in inner part of cave.
        Args:
            row: int representing row
            col: int representing column
        Returns:
            Boolean, True for lowest, False for not.
        '''
        current_point = cave_system[row][col]
        if (current_point < cave_system[row][col-1] and 
            current_point < cave_system[row][col+1] and 
            current_point < cave_system[row-1][col] and 
            current_point < cave_system[row+1][col]):
            return True
        return False

def check_corner_neighborhood(row, col, corner):
    '''Check the neighborhood of a point that's in a corner of cave.
    Args:
        row: int representing row
        col: int representing column
        corner: which corner point is in (0: top-left, 1: top-right, 2: bottom-left, 3: bottom-right)
    Returns:
        Boolean, True for lowest, False for not.
    '''

    current_point = cave_system[row][col]
    if corner == 0:
        if current_point < cave_system[row][col+1] and current_point < cave_system[row+1][col]:
            return True
    elif corner == 1:
        if current_point < cave_system[row][col-1] and current_point < cave_system[row+1][col]:
            return True
    elif corner == 2:
        if current_point < cave_system[row-1][col] and current_point < cave_system[row][col+1]:
            return True
    elif corner == 3:
        if current_point < cave_system[row-1][col] and current_point < cave_system[row][col-1]:
            return True
    return False

def check_edge_neighborhood(row, col):
    '''Check the neighborhood of a point that's on the edge of the cave.
    Args:
        row: int representing row
        col: int representing column
    Returns:
        Boolean, True for lowest, False for not.
    '''

    current_point = cave_system[row][col]
    if row == 0:
        if current_point < cave_system[row][col-1] and current_point < cave_system[row][col+1] and current_point < cave_system[row+1][col]:
            return True
    elif row == max_row-1:
        if current_point < cave_system[row][col-1] and current_point < cave_system[row][col+1] and current_point < cave_system[row-1][col]:
            return True
    elif col == 0:
        if current_point < cave_system[row][col+1] and current_point < cave_system[row-1][col] and current_point < cave_system[row+1][col]:
            return True
    elif col == max_col-1:
        if current_point < cave_system[row][col-1] and current_point < cave_system[row-1][col] and current_point < cave_system[row+1][col]:
            return True
    return False

def find_lowest_points(cave_system):
    '''Count the number numbers that are smallest in their neighborhood (top, down, left, right). 
    
    Args:
        cave_system: 2D array
    Returns:
        int
    '''

    lowest_points = []
    for row in range(max_row):
        for col in range(max_col):
            current_point = cave_system[row][col]
            
            corner = get_corner(row, col)
            
            if corner is not None:
                if check_corner_neighborhood(row, col, corner):
                    lowest_points.append((row, col))
            elif get_side_point(row, col):
                if check_edge_neighborhood(row, col):
                    lowest_points.append((row, col))
            else:
                if check_neighborhood(row, col):
                    lowest_points.append((row, col))

    return lowest_points

def bfs(start_row, start_col):
    '''Find size of basin from starting point. Only points whos value is higher by 1 from the current one are processed.
    
    Args:
        cave_system: 2D array
        start_row: int
        start_col: int
    Returns:
        Int representing number of cells that are part of basin.
    '''

    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        if (row, col) not in visited:
            visited.add((row, col))

            # Exceptions are used only to avoid indices larger than array size.
            try:
                if cave_system[row + 1][col] < 9:
                    queue.append((row + 1, col))
            except IndexError:
                pass

            try:
                if cave_system[row][col + 1] < 9:
                    queue.append((row, col + 1))
            except IndexError:
                pass
            
            if row - 1 >= 0 and cave_system[row - 1][col] < 9:
                queue.append((row - 1, col))
            
            if col - 1 >= 0 and cave_system[row][col - 1] < 9:
                queue.append((row, col - 1))
    
    return len(visited)

def calc_basins_size(lowest_points):
    '''Count the number of basins in the cave.
    
    Args:
        lowest_points: list of ints
    Returns:
        Int representing number of basins.
    '''
    
    basins_size = []
    for point in lowest_points:
        basins_size.append(bfs(point[0], point[1]))
    
    return basins_size
    
    
# Part 1
lowest_points = find_lowest_points(cave_system)
print('Part 1:', sum(map(lambda point: int(cave_system[point[0]][point[1]])+1, lowest_points)))

# Part 2
basin_sizes = sorted(calc_basins_size(lowest_points), reverse=True)
print('Part 2:', basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
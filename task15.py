from math import inf
from copy import deepcopy
from heapq import heappop, heappush

from utilities import get_2d_int_array

puzzle_input = get_2d_int_array('15')
max_row, max_col = len(puzzle_input), len(puzzle_input[0])

def dijkstra(arr, end_row, end_col):
    '''Finds path with lowest score from origin (0,0) to goal (end_row, end_col).
    
    Search is done via Dijkstra's algorithm.
    Args:
        arr: 2D array
        end_row: int
        end_col: int
    Returns:
        Int representing number of cells that are part of basin.
    '''

    start_node = (0, 0)
    end_node = (end_row, end_col)
    unvisited = [(0, start_node)]
    visited = set()
    
    risk_levels = {}
    for row in range(max_row):
        for col in range(max_col):
            risk_levels[(row, col)] = inf

    risk_levels[start_node] = 0

    while unvisited:
        node_risk_level, node = heappop(unvisited)
        visited.add(node)

        if node == end_node:
            return node_risk_level

        row = node[0]
        col = node[1]

        for neighbour in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            # Out of bounds check.
            if 0 <= neighbour[0] < max_row and 0 <= neighbour[1] < max_col:                
                
                # Given node risk level + current path risk level.
                neighbour_risk_level = arr[neighbour[0]][neighbour[1]] + node_risk_level
                
                if neighbour not in visited:
                    if risk_levels[neighbour] > neighbour_risk_level:
                        risk_levels[neighbour] = neighbour_risk_level
                        heappush(unvisited, (neighbour_risk_level, neighbour))
                        
    return node_risk_level

def increment_map(map_array):
    '''Increments all cells by one, if some goes above 9, sets it to 1.

    Args:
        map: 2D array
    Returns:
        2D array with incremented cells.
    '''
    global max_row, max_col

    for row in range(max_row):
        for col in range(max_col):
            map_array[row][col] = map_array[row][col] + 1 if map_array[row][col] < 9 else 1
    
    return map_array

def get_full_map(puzzle_input, max_row, max_col):
    '''Returns a 2D array representing the full map.
    
    Full map is 5 times larger in both dimensions. It's constructed by concatanating the original map 5 times. 
    Each new copy has risk levels increment by 1 then map above it or to left of it.
    Risk levels above 9 are set to back to 1.
    Args:
        puzzle_input: 2D array
        max_row: int
        max_col: int
    Returns:
        2D array
    '''
    max_size = 5
    full_map = deepcopy(puzzle_input)
    incremented_map = deepcopy(puzzle_input)
    
    # Construct first column of full map.
    for _ in range(max_size - 1):
        incremented_map = increment_map(deepcopy(incremented_map))
        full_map = full_map + incremented_map
    
    for row in range(len(full_map)):
        for i in range(4):
            full_map[row] += [cell + 1 if cell < 9 else 1 for cell in full_map[row][0 + max_row * i:max_col + max_col * i]]
    
    return full_map

# Part 1
print('Part 1:', dijkstra(puzzle_input, max_row - 1, max_col - 1))

# Part 2
full_map = get_full_map(puzzle_input, max_row, max_col)
max_row = len(full_map)
max_col = len(full_map[0])
print('Part 2:', dijkstra(full_map, max_row - 1, max_col - 1))
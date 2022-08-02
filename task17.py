import re
from math import inf

from utilities import get_file

puzzle_input = get_file('17')
puzzle_input = re.findall(r'x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)', puzzle_input)
x_ranges = (int(puzzle_input[0][0]), int(puzzle_input[0][1]))
y_ranges = (int(puzzle_input[0][2]), int(puzzle_input[0][3]))

def check_probe_position(x, y, goal_x, goal_y):
    '''Check if probe is in the goal zone.

    Args:
        coordinates: tuple of (x, y) coordinates.
        goal_x: x coordinate range of the goal.
        goal_y: y coordinate range of the goal.

    Returns:
        True if probe is in the goal zone, False otherwise.
    '''

    return x in range(goal_x[0], goal_x[1] + 1) and y in range(goal_y[0], goal_y[1] + 1)

def process_step(x, y, x_velocity, y_velocity):
    '''Process single step of probe's movement.

    Args:
        coordinates: tuple of (x, y) coordinates.

    Returns:
        tuple of (x, y) coordinates.
    '''

    x += x_velocity
    y += y_velocity

    if x_velocity > 0:
        x_velocity -= 1
    elif x_velocity < 0:
        x_velocity += 1

    y_velocity -= 1

    return (x, y, x_velocity, y_velocity)

def shoot_probe(goal_x, goal_y):
    '''Shoot probe to the goal and find all valid starting velocities.

    Velocity is valid if probe ends up in goal zone, which is a square area defined by goal_x and goal_y. 
    Function also keeps track of highest y coordinate achieved during shooting.
    Args:
        coordinates: tuple of (x, y) coordinates.
        goal_x: x coordinate range of the goal.
        goal_y: y coordinate range of the goal.

    Returns:
        Tuple, highest y coordinate and count of valid starting velocities.
    '''
        
    max_x_velocity = goal_x[1]
    min_y_velocity = goal_y[0]
    max_y_velocity = max_x_velocity * 2

    max_heights = []
    valid_velocitios = [] # That achieved the goal zone.
    
    for i in range(0, max_x_velocity + 1):
        for j in range(min_y_velocity, max_y_velocity):
            max_y = -inf
            x, y = 0, 0
            x_velocity, y_velocity = i, j
            while x <= goal_x[1] and y >= goal_y[0]:
                x, y, x_velocity, y_velocity = process_step(x, y, x_velocity, y_velocity)

                if y > max_y:
                    max_y = y
                
                if check_probe_position(x, y, goal_x, goal_y):                    
                    max_heights.append(max_y)
                    valid_velocitios.append((i, j))
                    break

        y_velocity += 1
    
    return max(max_heights), len(valid_velocitios)

max_height, velocities_count = shoot_probe(x_ranges, y_ranges)

# Part 1
print('Part 1:', max_height)

# Part 2
print('Part 2:', velocities_count)
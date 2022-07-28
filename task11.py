from copy import deepcopy

from utilities import get_2d_int_array

puzzle_input = get_2d_int_array('11')

def simulate_step(array):
    '''Simulates single step of simulation.

    Firstly, each cell is incremented. If cell's value is above threshold, it's neighbours are incremented as well. 
    Cells above threshold are set to 0 and can't be increment in given step anymore.

    Args:
        array: 2D array
    Returns:
        2D array with updated values and flash count in current step.
    '''

    flash_threshold = 9
    flashed_cells = set()
    can_flash = []

    for x in range(len(array)): # Increment all cells by 1.
        for y in range(len(array[0])):
            array[x][y] += 1
            
            if array[x][y] > flash_threshold:
                can_flash.append((x,y))

    while can_flash: # Increment neighbours of all cells that can flash (cell value > flash_threshold).
        x, y = can_flash.pop(0)
        
        if (x,y) in flashed_cells:
            continue

        array[x][y] = 0 
        flashed_cells.add((x,y))

        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i == x and j == y:
                    continue                    
                if i < 0 or i >= len(array):
                    continue
                if j < 0 or j >= len(array[i]):
                    continue
                
                if (i,j) not in flashed_cells:
                    array[i][j] += 1

                if array[i][j] > flash_threshold and (i,j) not in flashed_cells:
                    can_flash.append((i, j))       
    return len(flashed_cells), array

def simulate_with_max_steps(array, max_step):
    '''Simulates given number of steps. 
    
    Args:
        array: 2D array
    Returns:
        Count of flashes that occured throughout the all steps.
    '''

    total_flash_count = 0
    array_copy = deepcopy(array)
    for _ in range(max_step):
        step_flash_count, array = simulate_step(array_copy)
        total_flash_count += step_flash_count
       
    return total_flash_count

def simulate_till_all_flash(array):
    '''Simulates steps until all cells are 0.

    Args:
        array: 2D array
    Returns:
        Step at which all cells are 0. 
    '''
    
    step_count = 0
    while True:
        step_count += 1
        
        _, array = simulate_step(array)
        
        if all(cell == 0 for line in array for cell in line):
            return step_count

# Part 1
max_step = 100
print('Part 1:', simulate_with_max_steps(puzzle_input, max_step))

# Part 2
print('Part 2:', simulate_till_all_flash(puzzle_input))
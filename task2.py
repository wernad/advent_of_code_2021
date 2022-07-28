from utilities import get_lines

puzzle_input = get_lines('2')

def get_instruction(line):
    '''Get instruction and values from line.'''
    return line.split(' ')


def update_position(lines):
    '''Move based on input instructions. 

    Args:  
        lines: list of strings
    Returns:
        position: integer which represents the horizontal position
        depth: integer which represents the depth
    '''

    position = 0
    depth = 0
    for line in lines:
        instruction = get_instruction(line)
        if instruction[0] == 'up': #decrement depth
            depth -= int(instruction[1])
        elif instruction[0] == 'down': #increment depth
            depth += int(instruction[1])
        elif instruction[0] == 'forward': #move forward
            position += int(instruction[1]) 
    
    return position, depth

def update_position_with_aim(lines):
    '''Move based on input instructions. 

    Args:  
        lines: list of strings
    Returns:
        position: integer which represents the horizontal position
        depth: integer which represents the depth
    '''
    
    position = 0
    depth = 0
    aim = 0
    for line in lines:
        instruction = get_instruction(line)
        if instruction[0] == 'up': #decrement aim
            aim -= int(instruction[1])
        elif instruction[0] == 'down':# increment aim
            aim += int(instruction[1])
        elif instruction[0] == 'forward':#calc depth based on aim and increment position
            depth += int(instruction[1]) * aim
            position += int(instruction[1])
    
    return position, depth

#Part 1
position, depth = update_position(puzzle_input)
print('Part 1:', position * depth)

#Part 2
position, depth = update_position_with_aim(puzzle_input)
print('Part 2:', position * depth)
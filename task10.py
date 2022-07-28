from utilities import get_lines

puzzle_input = get_lines('10')

error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_scores = {')': 1, ']': 2, '}': 3, '>': 4}
brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}

def check_line_syntax(line):
    '''Checks if all brackets are closed. If not, return the error score.
    
    Args:
        line: string of brackets
    Returns: 
        Integer for error score or 0 if no error occured and brackets still on stack.
    '''

    stack = []
    for char in line:
        if char in brackets.keys():
            stack.append(char)
        elif char != brackets[stack.pop()]:
            return error_scores[char], None
    else:
        return 0, stack

def check_lines(lines):
    '''Checks lines for errors. Removes lines with errors.
    
    Args:
        lines: list of strings
    Returns: sum of error scores and list of stacks for each line.
    '''

    score = 0
    lines_to_remove = []
    stacks = []
    for idx in range(len(lines)):
        line_score, stack = check_line_syntax(lines[idx])
        if line_score > 0:
            score += line_score
            lines_to_remove.append(idx)
        elif len(stack) > 0:
            stacks.append(stack)
    
    return score, stacks

def calc_stack_scores(stacks):
    '''Calculate new scores for uncompleted lines, based on opening brackets on their stacks.
    Args:
        stacks: list of stacks
    Returns:
        list of new scores
    '''

    scores = []
    new_score = 0
    for stack in stacks:
        while stack:
            bracket = stack.pop()
            new_score *= 5
            new_score += completion_scores[brackets[bracket]]
        scores.append(new_score)
        new_score = 0

    return scores

# Part 1
score, stacks = check_lines(puzzle_input)
print('Part 1:', score)

# Part 2
line_scores = sorted(calc_stack_scores(stacks))
print('Part 2:', line_scores[len(line_scores)//2])
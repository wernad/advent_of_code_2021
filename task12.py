from collections import Counter

from utilities import get_lines

puzzle_input = get_lines('12')

class Node:
    name = None
    connections = set()
    
    def __init__(self, name):
        self.name = name
    
    def add_connection(self, node):
        self.connections.add(node)

def build_path_dict(puzzle_input):
    '''Builds a dictionary of caves. Keys are names of caves and values are names of connected caves. Separator is a dash '-'.

    Args:
        puzzle_input: list of strings
    Returns:
        path_dict: dictionary
    '''
    path_dict = {}
    for line in puzzle_input:
        left, right = line.split('-')
        
        if left not in path_dict:
            path_dict[left] = []
        
        if right not in path_dict:
            path_dict[right] = []

        path_dict[left].append(right)
        path_dict[right].append(left)

    return path_dict

def dfs(paths, start_node, end_node):
    '''Finds all paths between start_node and end_node. Lowercase nodes can be visited only once.

    Args:
        paths: dictionary of paths
        start_node: string
        end_node: string
    Returns:
        list of lists containing cave names
    '''
    stack = [[start_node]]

    possible_paths = []
    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]
        
        if current_node == end_node:
            possible_paths.append(current_path)
            continue

        for connection in paths[current_node]:
            if connection.lower() == connection and connection in current_path:
                continue

            new_branch = current_path.copy()
            new_branch.append(connection)
            stack.append(new_branch)

    return possible_paths

def dfs_permissive(paths, start_node, end_node):
    '''Finds all paths between start_node and end_node. Single lowercase node can be visited only once, the rest only once.

    Args:
        paths: dictionary of paths
        start_node: string
        end_node: string
    Returns:
        list of lists containing cave names
    '''
    # Boolean represents if some node has been visited twice.
    stack = [[False, start_node]]

    possible_paths = []
    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]
        
        if current_node == end_node:
            possible_paths.append(current_path)
            continue

        for connection in paths[current_node]:
            if connection == start_node:
                continue
            
            new_branch = current_path.copy()

            # First lowercase node can be visited twice, others only once
            if connection.lower() == connection:
                visits = new_branch.count(connection)

                if visits == 2:
                    continue
                elif visits == 1: 
                    if new_branch[0]:
                        continue
                    else:
                        new_branch[0] = True

            new_branch.append(connection)
            stack.append(new_branch)

    return possible_paths

# Part 1
paths = build_path_dict(puzzle_input)
paths_to_end = dfs(paths, 'start', 'end')
print('Part 1:', len(paths_to_end))

# Part 2
paths_to_end = dfs_permissive(paths, 'start', 'end')
print('Part 1:', len(paths_to_end))
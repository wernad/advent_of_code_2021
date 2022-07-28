from collections import Counter, defaultdict

from utilities import get_lines

puzzle_input = get_lines('14')

template = puzzle_input[0]
reaction_rules = {rule[0]: rule[1] for rule in [x.split(' -> ') for x in puzzle_input[2:]]}

def apply_reactions(template, reaction_rules, max_step):
    '''Create a new string from template by applying reaction rules to given template.
    
    Uses list to store template.
    Args:
        template: string with which function starts
        reaction_rules: list of strings
    Returns:
        New string after applying reaction rules.
    '''
    
    for _ in range(max_step):        
        i = 0
        while i < len(template):
            if template[i:i+2] in reaction_rules.keys():
                template = template[:i+1] + reaction_rules[template[i:i+2]] + template[i+1:]
                i += 1
            i += 1
    return template

def subtract_far_ends(template):
    '''Subtracts most and least common letter in template.

    Args: 
        template: string with which function starts
    Returns:
        Difference between most and least common letter in template.
    '''

    counter = Counter(template)
    most_common = counter.most_common(1)[0][1]
    least_common = counter.most_common()[-1][1]
    
    return most_common - least_common

def apply_reactions_efficient(template, reaction_rules, max_step):
    '''Create a new string from template by applying reaction rules.
    
    Keeps count of possible reactions in dictionary for faster lookup. Letter count is updated when a reaction rule is applied.
    Args:
        template: string with which function starts
        reaction_rules: list of strings
    Returns:
        Dictionary with letters as keys and their count as values.
    '''

    letter_count = defaultdict(int)
    for letter in template:
        letter_count[letter] += 1

    template_pairwise = [template[i:i+2] for i in range(len(template)-1)]

    pair_count = defaultdict(int)    
    for pair in template_pairwise:
        pair_count[pair] += 1

    for g in range(max_step):        
        new_pair_count = defaultdict(int)
        
        for pair in pair_count.keys():
            if pair in reaction_rules.keys():
                current_count = pair_count[pair]
                new_pair_count[pair[0] + reaction_rules[pair]] += current_count
                new_pair_count[reaction_rules[pair] + pair[1]] += current_count

                letter_count[reaction_rules[pair]] += current_count
                
                if pair_count[pair] - current_count > 0:
                    new_pair_count[pair] = pair_count[pair] - current_count
        
        pair_count = new_pair_count
        
    return letter_count 


# Part 1
new_template = apply_reactions(template, reaction_rules, 10)
print('Part 1:', subtract_far_ends(new_template))

# Part 2
letter_count = apply_reactions_efficient(template, reaction_rules, 40)
print('Part 2:', max(letter_count.values()) - min(letter_count.values()))
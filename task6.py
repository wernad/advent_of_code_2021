import math

from utilities import get_numbers

puzzle_input = get_numbers('6')
pop_init = len(puzzle_input)

def simulate_day(fish):
    '''Simulate one day of fish.
    Args:
        fish: integer representing days left before end of cycle.
    Return:
        Integer representing days left decremented by one. If at zero, return 6 (new cycle).
    '''
    if fish == 0:
        return 6
    else:
        return fish - 1

def simulation_bruteforce(puzzle_input, days_left):
    '''Simulate each fish's cycle.
    Args:
        fish_days: list of integers representing days left in a cycle of each fish.
        days: integer representing number of days to simulate.
    Returns:
        Integer representing number of fish remaining.
    '''
    fish_days = puzzle_input.copy()
    for _ in range(days_left):
        new_fish_count = 0
        for i in range(len(fish_days)):
            current_fish = fish_days[i]
            if current_fish == 0:
                new_fish_count += 1

            fish_days[i] = simulate_day(current_fish)
        
        if new_fish_count != 0:
            fish_days.extend([8] * new_fish_count)

    return len(fish_days)

def simulation(fish_days, days_left):
    '''Simulate each day by keeping the count of fish for each day.

    Args:
        fish_days: list of integers representing days left in a cycle of each fish.
        days: integer representing number of days to simulate.
    Returns:
        Integer representing number of fish remaining.
    '''
    
    days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for x in fish_days:
        days[x] += 1

    for _ in range(days_left):
        temp = days[0]
            
        for i in range(0, 8):
            days[i] = days[i+1]
        days[6] += temp

        days[8] = 0
        
        if temp > 0:
            days[8] = temp


    return sum(days.values())

#Part 1
part_one_days = 80
print('Part 1:', simulation_bruteforce(puzzle_input, part_one_days))

#Part 2
part_two_days = 256
print('Part 2:', simulation(puzzle_input, part_two_days))
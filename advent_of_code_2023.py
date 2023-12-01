import day_1

'''
Something is wrong with global snow production, and you've been selected to take a look. 
The Elves have even given you a map; on it, they've used stars to mark the top fifty 
locations that are likely to be having problems. You've been doing this long enough to know 
that to restore snow operations, you need to check all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent 
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
'''

def get_solution(day):
    if not isinstance(day, int) or day < 1 or day > 31:
        return f"Error: \"day\" must be integer between 1 and 31"

    output = f"Day {day} Solution:\n"
    if day == 1:
        output += f"-- Part 1: {day_1.part_1()}\n-- Part 2: {day_1.part_2()}"
    else:
        output += f"-- (solution not yet available)"

    return output
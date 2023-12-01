from day_1_solutions import *

'''
Something is wrong with global snow production, and you've been selected to take a look. 
The Elves have even given you a map; on it, they've used stars to mark the top fifty 
locations that are likely to be having problems. You've been doing this long enough to know 
that to restore snow operations, you need to check all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent 
calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
'''

# Set this value to control which solution to run
run_solution_day = 1

solutions = {
    1: Day1Solutions(),
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
    10: None,
    11: None,
    12: None,
    13: None,
    14: None,
    15: None,
    16: None,
    17: None,
    18: None,
    19: None,
    20: None,
    21: None,
    22: None,
    23: None,
    24: None,
    25: None,
    26: None,
    27: None,
    28: None,
    29: None,
    30: None,
    31: None
}

for (day_number, solution) in solutions.items():
    if solution is not None:
        solution.run_solutions()
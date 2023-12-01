from log import *
import time
import day_1

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

# { Day Number: [ Part 1 Solution Method, Part 2 Solution Method ] }
solutions = {
    1: [day_1.part_1, day_1.part_2],
    2: [None, None],
    3: [None, None],
    4: [None, None],
    5: [None, None],
    6: [None, None],
    7: [None, None],
    8: [None, None],
    9: [None, None],
    10: [None, None],
    11: [None, None],
    12: [None, None],
    13: [None, None],
    14: [None, None],
    15: [None, None],
    16: [None, None],
    17: [None, None],
    18: [None, None],
    19: [None, None],
    20: [None, None],
    21: [None, None],
    22: [None, None],
    23: [None, None],
    24: [None, None],
    25: [None, None],
    26: [None, None],
    27: [None, None],
    28: [None, None],
    29: [None, None],
    30: [None, None],
    31: [None, None]
}

def run_solution(day):
    if not isinstance(day, int) or day < 1 or day > 31:
        log_error(f"\"day\" must be integer between 1 and 31")

    log_info(f"Day {day} Solutions:")
    for part, solution_method in enumerate(solutions[day]):    
        solution = "(N/A)"
        elapsed_time = 0
        if solution_method is not None:
            start_time = time.time()
            solution = solution_method()
            elapsed_time = (time.time() - start_time) / 1000
        
        log_info(f"-- Pt. {part+1}: {solution} ({elapsed_time:.5f}ms)")

run_solution(day = run_solution_day)

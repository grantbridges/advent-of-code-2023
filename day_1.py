from utils import utils
from log import *

'''
https://adventofcode.com/2023/day/1

--- Day 1: Trebuchet?! ---

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you 
("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you 
just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already 
loading you into a trebuchet ("please hold still, we need to strap you in"). As they're making the final adjustments, 
they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently 
just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration 
value that the Elves now need to recover. On each line, the calibration value can be found by combining the 
first digit and the last digit (in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
Consider your entire calibration document. What is the sum of all of the calibration values?
'''

#solutions
input_file = 'inputs/day_1.txt'

def part_1():
    numbers = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            first_val = utils.first_int_in_list(line)
            last_val = utils.last_int_in_list(line)

            numbers.append(int(f'{first_val}{last_val}'))
    
    return sum(numbers)

'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

def part_2():
    string_int_mapping = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five", 
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    numbers = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.replace('\n', '')

            log_debug(f"Line:\t{line}")

            # keep track of occurrences of each number by tracking which indices it shows up at
            occurrences = {}
            for (numeric, written) in string_int_mapping.items():
                # find all instances of string-form integer (e.g. "eight")
                numeric_indices = utils.find_all_substrings(line, numeric)
                # find all instances of number-form integer (e.g. "8")
                written_indices = utils.find_all_substrings(line, written)

                indices = (numeric_indices + written_indices)
                indices.sort()
                occurrences[numeric] = indices

            # now find the number entries with the minimum and maximum indices
            min_index, min_index_value = -1, ''
            max_index, max_index_value = -1, ''
            for (value, indices) in occurrences.items():
                if len(indices) > 0:
                    temp_min_index = min(indices)
                    if min_index == -1 or temp_min_index < min_index:
                        min_index = temp_min_index
                        min_index_value = value

                    temp_max_index = max(indices)
                    if max_index == -1 or temp_max_index > max_index:
                        max_index = temp_max_index
                        max_index_value = value

            output = int(f'{min_index_value}{max_index_value}')
            log_debug(f"Output:\t{output}")

            numbers.append(output)
    
    return sum(numbers)

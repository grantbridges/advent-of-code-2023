from base_aoc_day_solutions import *

# https://adventofcode.com/2023/day/1

class Day1Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 1)

        self.input_file_part_1 = 'inputs/day_1.txt'
        self.input_file_part_2 = 'inputs/day_1.txt'

    def part_1(self):
        numbers = []
        with open(self.input_file_part_1, 'r') as f:
            for line in f.readlines():
                first_val = utils.first_int_in_list(line)
                last_val = utils.last_int_in_list(line)

                numbers.append(int(f'{first_val}{last_val}'))
        
        return sum(numbers)

    def part_2(self):
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
        with open(self.input_file_part_2, 'r') as f:
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
    
Day1Solutions().run_solutions()
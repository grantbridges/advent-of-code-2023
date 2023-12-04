from base_aoc_day_solutions import *

# https://adventofcode.com/2023/day/3

class Schematic:
    def __init__(self, input_data):
        self.data = []
        self.symbols = set()
        
        for row in input_data:
            row = row.replace('\n', '')
            self.data.append(row)
        
        self.compute_symbols()

    def compute_symbols(self):
        self.symbols = set()
        for row in self.data:
            for val in row:
                if not utils.is_int(val) and val != '.':
                    self.symbols.add(val)

    def compute_sum(self):
        sum = 0
        rows = self.data
        y = 0
        while y < len(rows):
            row = rows[y]
            x = 0
            while x < len(row):
                val = row[x]
                if utils.is_int(val):
                    # Stop here! See how far rightward the numbers go
                    current_val = val
                    val_start_x = x
                    val_end_x = x
                    while val_end_x + 1 < len(row) and utils.is_int(row[val_end_x + 1]):
                        val_end_x += 1
                        current_val += row[val_end_x]

                    # So we have the full number and where it starts and stops

                    check_x_min = max(0, val_start_x - 1)
                    check_x_max = min(len(row) - 1, val_end_x + 1)

                    found_symbol = False

                    prev_row = ''
                    if y > 0:
                        # check top row for a symbol
                        prev_row = rows[y-1]
                        for i in range(check_x_min, check_x_max + 1):
                            if self.is_symbol(prev_row[i]):
                                found_symbol = True
                            
                    next_row = ''
                    if y < len(rows) - 1:
                        # check bottom row for a symbol
                        next_row = rows[y+1]
                        for i in range(check_x_min, check_x_max + 1):
                            if self.is_symbol(next_row[i]):
                                found_symbol = True
                            
                    if check_x_min != val_start_x:
                        # check space to the left
                        if self.is_symbol(row[check_x_min]):
                            found_symbol = True

                    if check_x_max != val_end_x:
                        # check space to the right
                        if self.is_symbol(row[check_x_max]):
                            found_symbol = True

                    if found_symbol:
                        sum += int(current_val)

                    log_debug(f'Prev: {prev_row}')
                    log_debug(f'Curr: {row}')
                    log_debug(f'Next: {next_row}')
                    log_debug(f'      -- Determined {current_val} {"is NOT" if not found_symbol else "IS"} a symbol --')
                    log_debug(f'      -- New sum: {sum}')


                    # Before continuing on, scoot x up to the end of the current value
                    x = val_end_x + 1
                else:
                    x += 1

            y += 1
        
        return sum

    def is_symbol(self, val):
        return val in self.symbols

class Day3Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 3)

    def part_1(self):
        with open(self.input_file, 'r') as f:
            schematic = Schematic(f.readlines())
            return schematic.compute_sum()

    def part_2(self):
        return 0
    
Day3Solutions().run_solutions()
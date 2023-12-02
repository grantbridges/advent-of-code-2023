from base_aoc_day_solutions import *

# https://adventofcode.com/2023/day/2

class Handful():
    def __init__(self, handful_count):
        self.handful_count = handful_count
        self.color_counts = {}

    def parse(self, handful_data):
        # each comma separates a different dice count
        dice_splits = handful_data.split(',')

        # check for each color, remove the label, and store the number
        colors_to_check = ['red', 'blue', 'green']
        for dice_count in dice_splits:
            for color_name in colors_to_check:
                if color_name in dice_count:
                    number_only = dice_count.replace(color_name, '')
                    self.color_counts[color_name] = int(number_only)
        
    def check_pass_cube_limit(self, cube_limits):
        for (color, count) in cube_limits.items():
            # see if I even have this color in my handful...
            if color in self.color_counts:
                if self.color_counts[color] > count:
                    # I have more counts of this color in this handful than allowed - failed check
                    return False
        
        # handful is safe
        return True

    def log_debug(self):
        entries = []
        for (color, count) in self.color_counts.items():
            entries.append(f'{count} {color}')
        
        log_debug(f'Handful {self.handful_count}: {", ".join(entries)}')

class Game():
    def __init__(self):
        self.id = -1
        self.original_input_line = ''
        self.handfuls = []

    def parse_line(self, line):
        self.original_input_line = line

        # example: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        splits = line.split(':')
        
        # first handle "Game #" label on lhs
        self.id = int(splits[0].split(' ')[1]) # (the part after the space)

        # now handle the data portion, the rhs
        data_split = splits[1]
        data_split = data_split.replace(' ', '')

        # each semicolon separates a handful
        handful_splits = data_split.split(';')
        for (index, handful_data) in enumerate(handful_splits):
            handful = Handful(handful_count=index+1)
            handful.parse(handful_data)

            self.handfuls.append(handful)

        self.log_debug()

    def check_handfuls_pass_cube_limit(self, cube_limits):
        for h in self.handfuls:
            if h.check_pass_cube_limit(cube_limits) == False:
                # one failed - whole game is impossible
                return False
        
        # all handfuls passed, game is valid
        return True
    
    def get_min_color_reqs_power(self):
        min_color_reqs = {'red': 0, 'green': 0, 'blue': 0}

        for h in self.handfuls:
            for (color, count) in h.color_counts.items():
                if min_color_reqs[color] < count:
                    min_color_reqs[color] = count

        power = 1
        for (color, count) in min_color_reqs.items():
            power *= count 

        return power

    def log_debug(self):
        log_debug(f'Input line: {self.original_input_line}')
        log_debug(f'Game {self.id} Output:')
        for h in self.handfuls:
            h.log_debug()

class Day2Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 2)

        self.input_file_part_1 = 'inputs/day_2.txt'
        self.input_file_part_2 = 'inputs/day_2.txt'

    def part_1(self):
        games = []
        with open(self.input_file_part_1, 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '')

                game = Game()
                game.parse_line(line)
                games.append(game)

        color_counts = {'red': 12, 'green': 13, 'blue': 14}
        passed_games = []
        for g in games:
            if g.check_handfuls_pass_cube_limit(color_counts):
                passed_games.append(g)
            
        sum = 0
        for g in passed_games:
            sum += g.id
        
        return sum

    def part_2(self):
        games = []
        with open(self.input_file_part_1, 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '')

                game = Game()
                game.parse_line(line)
                games.append(game)
        
        powers = []
        for g in games:
            powers.append(g.get_min_color_reqs_power())
        
        return sum(powers)
    
Day2Solutions().run_solutions()
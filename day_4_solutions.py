from base_aoc_day_solutions import *

# https://adventofcode.com/2023/day/4

class Card:
    def __init__(self):
        self.id = -1
        self.winning_numbers = []
        self.my_numbers = []

    def parse_line(self, line: str):
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

        # replace all multiple spaces with single spaces for easier parsing
        line = utils.remove_multi_whitespace(line)

        first_split = line.split(':')
        id_split = first_split[0].split(' ')
        self.id = int(id_split[1])

        numbers = first_split[1]
        numbers_split = numbers.split('|')
        winners_vals = numbers_split[0].strip()
        my_vals = numbers_split[1].strip()

        for val in winners_vals.split(' '):
            self.winning_numbers.append(int(val))
        
        for val in my_vals.split(' '):
            self.my_numbers.append(int(val))

        log_debug(f'Input:  {line}')
        log_debug(f'Output: Card {self.id}: {" ".join(map(str, self.winning_numbers))} | {" ".join(map(str, self.my_numbers))}')

    def get_num_winning_matches(self):
        num = 0
        for val in self.my_numbers:
            if val in self.winning_numbers:
                num += 1
        return num

    def get_score(self):
        score = 0
        for val in self.my_numbers:
            if val in self.winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        return score


class Day4Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 4)

    def part_1(self):
        total_score = 0
        with open(self.input_file, 'r') as f:
            cards = []
            for line in f.readlines():
                line = line.replace('\n', '')

                card = Card()
                card.parse_line(line)
                cards.append(card)
            
            for card in cards:
                total_score += card.get_score()

        return total_score

    def part_2(self):
        total_score = 0
        with open(self.input_file, 'r') as f:
            cards = []
            copy_cards = []
            for line in f.readlines():
                line = line.replace('\n', '')

                card = Card()
                card.parse_line(line)
                cards.append(card)
            
            for i in range(0, len(cards)):
                card = cards[i]
                matches = card.get_num_winning_matches()
                for j in range(i+1, i+1+matches):
                    if j < len(cards):
                        copy_cards.append(cards[j])
                
            for card in copy_cards:
                total_score += card.get_score()

        return total_score
    
Day4Solutions().run_solutions()
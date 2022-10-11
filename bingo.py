from typing import Dict, Tuple, List, Set, Optional, IO
import random
from beautifultable import BeautifulTable

""" This class purpose is to create a bingo game where the bingo cards can play. It generates random numbers that
can be stamped from the bingo card. It will contain a pattern that the bingo cards must match to be winner of bingo"""


class Bingo:
    def __init__(self) -> None:
        self.cards = []
        self.pattern = []
        self.pattern_matches = 0
        self.numbers = []
        self.history = []
        self.status = "In progress"

    def generate_numbers(self) -> None:
        """ Generate numbers to be use to match with the BINGO card. """
        self.numbers = random.sample(range(0, 76), 75)

    def generate_pattern(self) -> None:
        """ Generate the pattern that needs to be match by the BINGO card in order to win. """
        num = random.randint(0, 2)
        if num == 0:
            self.pattern = [["B", "X", "X", "X", "X", "X"],
                            ["I", "X", "X", "X", "X", "X"],
                            ["N", "X", "X", "X", "X", "X"],
                            ["G", "X", "X", "X", "X", "X"],
                            ["O", "X", "X", "X", "X", "X"]]
            self.pattern_matches = 25
        if num == 1:
            self.pattern = [["B", "X", "O", "O", "O", "O"],
                            ["I", "X", "O", "O", "O", "O"],
                            ["N", "X", "X", "X", "X", "X"],
                            ["G", "X", "O", "O", "O", "O"],
                            ["O", "X", "O", "O", "O", "O"]]
            self.pattern_matches = 9
        if num == 2:
            self.pattern = [["B", "X", "X", "X", "X", "X"],
                            ["I", "X", "O", "O", "O", "X"],
                            ["N", "X", "O", "X", "O", "X"],
                            ["G", "X", "O", "O", "O", "X"],
                            ["O", "X", "X", "X", "X", "X"]]
            self.pattern_matches = 17
        if num == 3:
            self.pattern = [["X", "O", "O", "O", "O", "O"],
                            ["X", "O", "O", "O", "O", "O"],
                            ["X", "O", "O", "X", "O", "O"],
                            ["X", "O", "O", "O", "O", "O"],
                            ["X", "O", "O", "O", "O", "O"]]
            self.pattern_matches = 6

    def display_pattern(self) -> str:
        """ Displays the pattern on the console required to win the BINGO game. """
        temp = BeautifulTable()
        for i in range(5):
            temp.columns.insert(i, self.pattern[i])
        return str(temp)

    def add_card(self, card: list) -> None:
        """ Add a BINGO card to participate in the BINGO game. """
        self.cards.append(card)

    def generate_number(self) -> int:
        """ Generate a number to be cleared off the BINGO card. """
        return self.numbers.pop(0)

    @staticmethod
    def helper_check(self, num: int) -> int:
        """ Return value base on whether the given number belongs to a specified column. (0 = B, 1 = I, 2 = N,
        3 = G, 4 = O). Specifically use to assist with check function to delegate work required to find the specified
        column of the associated number. """
        if num < 16:
            return 0
        elif num < 31:
            return 1
        elif num < 46:
            return 2
        elif num < 61:
            return 3
        else:
            return 4

    def check(self) -> None:
        """ Generates the number to be match on the BINGO card. Checks to see if the cards on the BINGO game matches
        the number. If a BINGO card matches the number its pattern is check off and add number of matching pattern."""
        num = self.generate_number()
        self.history.append(num)
        x = self.helper_check(self, num)
        for card in self.cards:
            # could shorten code or improve readability by breaking down steps for each individual cards instead
            # check_card(self, x)
            for y in range(1, 6):
                if card.card[x][y] == num:
                    card.matches[x][y] = "X"
                    card.card[x][y] = "(" + str(card.card[x][y]) + ")"
                    card.num_matches += 1
                    break

    def pattern_check(self, card) -> bool:
        actual_matches = 0
        for i in range(0, 5):
            for j in range(0, 6):
                if self.pattern[i][j] == "X" and self.pattern[i][j] == card.matches[i][j]:
                    actual_matches += 1
        if actual_matches == self.pattern_matches:
            return True
        return False

    def pattern_checks(self) -> None:
        for card in self.cards:
            if card.num_matches >= self.pattern_matches:
                if self.pattern_check(card):
                    card.status = "Winner"

    def declare_winner(self) -> list:
        """ Displays the winner/s of the BINGO game"""
        winners = []
        for card in self.cards:
            if card.status == "Winner":
                winners.append(card)
        if len(winners) > 0:
            self.status = "Ended"
            return winners

    def regular_game(self) -> None:
        self.generate_numbers()
        self.generate_pattern()
        n = 0
        print(self.display_pattern())
        before_check_num = self.pattern_matches - 6
        while self.status != "Ended":
            self.check()
            n += 1
            if n > before_check_num:
                self.pattern_checks()
                x = self.declare_winner()
                if x is not None:
                    print(75 - len(self.numbers))
                    print(self.history)
                    for winner in x:
                        print(winner)


if __name__ == '__main__':
    a = Bingo()


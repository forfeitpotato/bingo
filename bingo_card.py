from typing import Dict, Tuple, List, Set, Optional, IO
import random
from beautifultable import BeautifulTable

""" A BINGO card is a 5x6 grid that contains the letter B, I, N, G, O at the top of the card. Numbers in the same
column corresponds that this number belong to this letter. B goes from (1-15), I (16-30), N(31-45), G(46-60), O(61-75)
The purpose of this class is to create a BINGO card this will act as an abstract class for other bingo card variants.
"""


class BingoCard:
    """Abstract class for types of BINGO card to be created

    === Private Attributes ===
    _card: contains the values found in the card.
    """
    def __init__(self) -> None:
        """Initialize a new Bingo Card"""
        self.card = [["B"], ["I"], ["N"], ["G"], ["O"]]
        self.matches = [["X", "O", "O", "O", "O", "O"],
                        ["X", "O", "O", "O", "O", "O"],
                        ["X", "O", "O", "X", "O", "O"],
                        ["X", "O", "O", "O", "O", "O"],
                        ["X", "O", "O", "O", "O", "O"]]
        self.num_matches = 6
        self.status = "In progress"

    def __str__(self) -> str:
        temp = BeautifulTable()
        for i in range(len(self.card)):
            temp.columns.insert(i, self.card[i])
        return str(temp)


class RegularBingoCard(BingoCard):
    """Creates a regular BINGO card with randomize values going in there required space"""

    def __init__(self) -> None:
        BingoCard.__init__(self)
        for i in range(5):
            list_nums = random.sample(range(1 + (i * 15), 16 + (i * 15)), 5)
            if i == 2:
                list_nums[2] = "FREE"
            self.card[i] += list_nums


if __name__ == '__main__':
    a = RegularBingoCard()










from bingo import Bingo
from bingo_card import BingoCard, RegularBingoCard

"""  """

if __name__ == '__main__':
    bingo = Bingo()
    for i in range(0, 100):
        bingo.add_card(RegularBingoCard())

    bingo.regular_game()


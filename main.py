from tic_tac_toe import TicTacToeGame
from board import TicTacToeBoard


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == "__main__":
    main()

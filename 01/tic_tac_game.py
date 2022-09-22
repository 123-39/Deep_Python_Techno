""" tic-tac-toe class """
import numpy as np


class TicTacGame:
    """
    Implementation of the game of tic-tac-toe
    """

    def __init__(self):

        # Generating a field
        self.board = np.array([['_' for _ in range(3)] for _ in range(3)])
        # Move counter
        self.numb_of_moves = 0
        # Input validation checker
        self.checking_range = tuple(range(1, 4))
        # Players
        self.first = 0
        self.second = 0

    def show_board(self):

        """ Show the game board """

        print("--1-2-3--")
        print("~" * 9)
        for i in range(3):
            raw = "| "
            for j in range(3):
                raw += f"{self.board[i][j]} "
            raw += f"| {i+1}"
            print(raw)
            if i < 2:
                print('-' * 9)
        print("=" * 9)

    def check_input(self, x_y):

        """ Check correcting input data """

        try:
            raw, col = tuple(map(int, x_y))
        except ValueError:
            return (False, None, None)

        return (True, raw, col) if (raw in self.checking_range) &\
            (col in self.checking_range) else (False, None, None)

    def validate_input(self, player, i, j):

        """ Cell busy check """

        if self.board[i - 1][j - 1] == '_':
            self.board[i - 1][j - 1] = player
            self.numb_of_moves += 1
            return True
        return False

    def start_game(self):

        """ Start game function """

        # Кто начинает первый
        rand_numb = np.random.randint(0, 2)
        self.first = str(rand_numb).replace('1', 'X')
        self.second = str(1 - rand_numb).replace('1', 'X')
        print(f"First start: {self.first}")

        # Игра с проверкой на выигрыш
        while True:
            for player in (self.first, self.second):
                self.show_board()
                print(f"{player}-move. Where? ")
                if self.one_move(player):
                    self.show_board()
                    print(f"{player}-player win!")
                    return True
                if self.numb_of_moves == 9:
                    print("Dead heat")
                    return True

    def input_data(self):

        """ Input data function for tests """

        return input("raw, col: ").split(',')

    def input_data_2(self):

        """ Input data function for tests """

        return input("raw, col: ").split(',')

    def input_data_3(self):

        """ Input data function for tests """

        return input("raw, col: ").split(',')

    def one_move(self, player):

        """ Player move and board display """

        checking, i, j = self.check_input(self.input_data())
        while True:
            if not checking:
                print("Select correct cell")
                checking, i, j = self.check_input(self.input_data_2())
                continue
            if self.validate_input(player, i, j):
                break
            print("Select another cell")
            checking, i, j = self.check_input(self.input_data_3())

        return self.check_winner()

    def check_winner(self):

        """ Check winner player"""

        # You can't win in less than 5 moves
        if self.numb_of_moves < 5:
            return False

        # Checking the combination diagonally
        diag_seq = [self.board[i, i] for i in range(3)]
        check_diag_seq = (len(diag_seq) == diag_seq.count(diag_seq[0])) \
            and (diag_seq[0] != '_')
        if check_diag_seq:
            return check_diag_seq

        # Проверка комбинации по побочной диагонали
        inv_diag_seq = [self.board[i, -i-1] for i in range(3)]
        check_inv_diag_seq = (len(inv_diag_seq) == inv_diag_seq.count(
            inv_diag_seq[0])) and (inv_diag_seq[0] != '_')
        if check_inv_diag_seq:
            return check_inv_diag_seq

        # Проверка комбинации по строке и столбцу
        check_raw_seq, check_col_seq = [], []
        for i in range(3):
            raw_seq = [self.board[i, j] for j in range(3)]
            check_raw_seq.append((len(raw_seq) == raw_seq.count(
                raw_seq[0])) and (raw_seq[0] != '_'))

            col_seq = [self.board[j, i] for j in range(3)]
            check_col_seq.append((len(col_seq) == col_seq.count(
                col_seq[0])) and (col_seq[0] != '_'))

        if any(check_raw_seq):
            return True
        if any(check_col_seq):
            return True
        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()

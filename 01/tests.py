""" tic-tac-toe class tests """
import unittest
from unittest.mock import patch

from tic_tac_game import TicTacGame


class TestGameMethods(unittest.TestCase):
    """
    Implementation of the tic-tac-toe class tests
    """

    # =================INPUT CHECKING=================

    def test_check_correct_input(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("1,2".split(',')), (True, 1, 2))

    def test_check_incorrect_input_comma(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("1 2".split(',')),
                                              (False, None, None))

    def test_check_incorrect_right_outrange_input(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("1,4".split(',')),
                                              (False, None, None))

    def test_check_incorrect_left_outrange_input(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("0,2".split(',')),
                                              (False, None, None))

    def test_check_incorrect_letter_input(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("a b".split(',')),
                                              (False, None, None))

    def test_check_incorrect_big_input(self):

        game = TicTacGame()
        self.assertTupleEqual(game.check_input("1 2 3".split(',')),
                                              (False, None, None))

    def test_check_bad_input(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        self.assertFalse(game.validate_input('0', 1, 1))

    def test_check_good_input(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        self.assertTrue(game.validate_input('0', 1, 2))

    @patch('tic_tac_game.TicTacGame.input_data')
    def test_full_move(self, mock_input):
        game = TicTacGame()
        mock_input.return_value = ['1', '1']
        self.assertFalse(game.one_move('X'))

    # =================WINNER CHECKING=================

    def test_check_init_winner(self):

        game = TicTacGame()
        self.assertFalse(game.check_winner())

    def test_check_not_winner(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        game.validate_input('0', 1, 2)
        game.validate_input('X', 2, 2)
        game.validate_input('0', 1, 3)
        game.validate_input('X', 2, 3)
        self.assertFalse(game.check_winner())

    def test_check_not_winner_empt_raw(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        game.validate_input('0', 1, 2)
        game.validate_input('X', 1, 3)
        game.validate_input('0', 2, 1)
        game.validate_input('X', 2, 2)
        game.validate_input('0', 2, 3)
        self.assertFalse(game.check_winner())

    def test_check_diag_winner(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        game.validate_input('0', 1, 2)
        game.validate_input('X', 2, 2)
        game.validate_input('0', 1, 3)
        game.validate_input('X', 3, 3)
        self.assertTrue(game.check_winner())

    def test_check_col_winner(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        game.validate_input('0', 1, 2)
        game.validate_input('X', 2, 1)
        game.validate_input('0', 1, 3)
        game.validate_input('X', 3, 1)
        self.assertTrue(game.check_winner())

    def test_check_raw_winner(self):

        game = TicTacGame()
        game.validate_input('X', 1, 1)
        game.validate_input('0', 2, 1)
        game.validate_input('X', 1, 2)
        game.validate_input('0', 2, 3)
        game.validate_input('X', 1, 3)
        self.assertTrue(game.check_winner())

    def test_check_inv_diag_winner(self):

        game = TicTacGame()
        game.validate_input('0', 1, 3)
        game.validate_input('X', 1, 2)
        game.validate_input('0', 2, 2)
        game.validate_input('X', 3, 2)
        game.validate_input('0', 3, 1)
        self.assertTrue(game.check_winner())


if __name__ == "__main__":

    unittest.main()

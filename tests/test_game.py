import unittest as test
import app.game

class TestGame(test.TestCase):
    def setUp(self):
        self.test_case = app.game.GameBoard()
        self.test_case.build_play_board(6)
        self.test_case.set_ship(3)

    def test_game_setup(self):
        self.assertEqual(len(self.test_case.get_play_board()), 6)
        self.assertEqual(len(self.test_case.get_ship_board()), 6)

    def test_check_for_hit(self):
        hit_result = self.test_case.check_for_hit(0,0)
        self.assertIs(type(hit_result), bool)
"""
Test cases for the BowlingGame class.

These tests cover various scenarios, including gutter games, all ones, one spare, one strike, perfect game, and more.

Changes:
    - Renamed the `rolls` method to `roll` to match the `BowlingGame` class.
    - Removed the duplicate `testOneSpare` method.
    - Improved docstrings for better readability and understanding.
"""

import unittest
from BowlingGame import BowlingGame  # Import the BowlingGame class

class TestBowlingGame(unittest.TestCase):
    """
    Test cases for the BowlingGame class.
    """

    def setUp(self):
        """
        Initializes a new game of bowling before each test.
        """
        self.game = BowlingGame()  # Initialize the BowlingGame instance

    def testGutterGame(self):
        """
        Test a gutter game (all zeros).

        Rolls 20 zeros and verifies the score is 0.
        """
        for i in range(20):
            self.game.roll(0)  # Use the roll method instead of rolls
        assert self.game.score() == 0

    def testAllOnes(self):
        """
        Test a game with all ones.

        Rolls 20 ones and verifies the score is 20.
        """
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        """
        Test a game with one spare.

        Rolls a spare and verifies the score is correct.
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        """
        Test a game with one strike.

        Rolls a strike and verifies the score is correct.
        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        """
        Test a perfect game (all strikes).

        Rolls 12 strikes and verifies the score is 300.
        """
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testOneSpareWith21Rolls(self):
        """
        Test a game with one spare and 21 rolls.

        Rolls a spare and 21 rolls and verifies the score is correct.
        """
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        """
        Rolls the ball multiple times.

        Args:
            pins (int): The number of pins knocked down.
            rolls (int): The number of rolls.
        """
        for i in range(rolls):
            self.game.roll(pins)  # Use the roll method instead of rolls

if __name__ == '__main__':
    unittest.main()
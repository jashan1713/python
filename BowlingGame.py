class BowlingGame:
    """
    A class representing a game of bowling.

    Attributes:
        rolls (list): A list of rolls made in the game.

    Methods:
        roll(pins): Rolls the ball, adding the pins knocked down to the game.
        score(): Calculates the total score of the game.
        isStrike(rollIndex): Checks if a roll is a strike.
        isSpare(rollIndex): Checks if a roll is a spare.
        strikeScore(rollIndex): Calculates the score for a strike.
        spareScore(rollIndex): Calculates the score for a spare.
        frameScore(rollIndex): Calculates the score for a regular frame.
    """

    def __init__(self):
        """
        Initializes a new game of bowling.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Rolls the ball, adding the pins knocked down to the game.

        Args:
            pins (int): The number of pins knocked down.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score of the game.

        Returns:
            int: The total score of the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Checks if a roll is a strike.

        Args:
            rollIndex (int): The index of the roll.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Checks if a roll is a spare.

        Args:
            rollIndex (int): The index of the roll.

        Returns:
            bool: True if the roll is a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """
        Calculates the score for a strike.

        Args:
            rollIndex (int): The index of the roll.

        Returns:
            int: The score for the strike.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculates the score for a spare.

        Args:
            rollIndex (int): The index of the roll.

        Returns:
            int: The score for the spare.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for a regular frame.

        Args:
            rollIndex (int): The index of the roll.

        Returns:
            int: The score for the frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
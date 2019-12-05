from src.Board import *
from random import *

class Player:
    """
    This class represents the human player of ShootyBoats.

    === Public Attributes ===
    board:
        The board that this player is playing on.
    """
    def __init__(self, board: Board):
        """
        Initializes a Player in ShootyBoats
        """
        self.board = board
        self.enemy_ships_sunk = 0

    def ask_for_coordinates(self) -> tuple:
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to place your ships:")
        x = input("Enter an x coordinate to:")
        y = input("Enter a y coordinate:")
        return x, y

    def get_random_coordinates(self) -> tuple:
        """
        Generates a random coordinate for the cpu player to place a ship or
        shoot a shot.
        """
        random_x = randint(0, 10)
        random_y = randint(0, 10)
        return random_x, random_y

    def place_ships(self):
        """
        Places all 5 ships on the board according to player's input.
        """
        for i in range(5):
            point = self.ask_for_coordinates()
            self.board.put_boat(point[0], point[1])

    def place_ships_randomly(self):
        """
        Places all 5 ships on the board randomly.
        """
        for i in range(5):
            point = self.get_random_coordinates()
            self.board.put_boat(point[0], point[1])

    def select_target(self) -> tuple:
        """
        Asks the human player for coordinates.
        """
        print("Enter the coordinates where you want to shoot:")
        x = input("Enter an x coordinate to:")
        y = input("Enter a y coordinate:")
        return x, y

    def make_move(self):
        """
        Makes a move by consulting a human.
        """
        move = self.ask_for_coordinates()
        self.board.register_hit(move[0], move[1])

    def make_random_move(self):
        """
        Makes random move.
        """
        move = self.get_random_coordinates()
        self.board.register_hit(move[0], move[1])




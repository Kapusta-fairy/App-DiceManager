from random import randint


class Dice(object):

    def __init__(self, sides: int):
        self.sides: int = sides

    def throw(self) -> int:
        return randint(1, self.sides)

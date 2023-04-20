from random import randint


class Dice(object):

    def __init__(self, sides: int):
        self._sides: int = sides

    def throw(self) -> int:
        return randint(1, self._sides)


class Wound(object):

    def __init__(self, count: int):
        self._count: float = count

    def __len__(self):
        return self._count

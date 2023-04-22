from random import randint


class Dice(object):
    """Dice that you can throw.

    Methods:
    throw()

    :param sides: faces of dice
    """
    def __init__(self, sides: int):
        self._sides: int = sides
        self._last_throw: int = 0

    def throw(self) -> int:
        """Produce a dice roll.

        :return: the result of the throw
        """
        return randint(1, self._sides)

    def __str__(self):
        return f'd{self._sides}'


class Wound(object):
    """An object for working with wounds

    len() return count

    Methods:
    calculate_wounds()

    :param count: count of wounds
    """
    def __init__(self, count: int = 0):
        _wounds_file_path = 'wounds.txt'

        self._count: float = count
        self._wounds_list: list = self._create_wounds_list(_wounds_file_path)

    def calculate_wounds(self, dices_result: list) -> float:
        """Set wounds for dices_result.

        :return: count of wounds
        """
        for dice_result in dices_result:
            if len(self._wounds_list) - 1 > dice_result:
                self._count += self._wounds_list[dice_result]
            else:
                self._count += self._wounds_list[len(self._wounds_list) - 1]
        return self._count

    def _create_wounds_list(self, path) -> list:
        wounds: dict = self._parse_values_file(path)
        list_of_result: list = []
        temp_value: float = 0.0

        for index in range(max(wounds) + 1):
            if index in wounds:
                temp_value: float = wounds.get(index)
            list_of_result.append(temp_value)

        return list_of_result

    @staticmethod
    def _parse_values_file(path: str) -> dict:
        file_woulds: dict = {}

        with open(path, 'r', encoding='utf8') as file_obj:
            file: str = file_obj.read()

        for string in file.split('\n'):
            key_value: list = string.split('=')
            file_woulds[int(key_value[0].strip())] = float(key_value[1].strip())

        return file_woulds

    def __len__(self):
        return self._count

    def __str__(self):
        return f'{self._count} ранений'

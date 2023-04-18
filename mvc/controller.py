from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice


class Container(MDBoxLayout):

    def view_throws(self):
        sides: str = self.sides_input.text
        count: str = self.count_input.text
        if sides.isdigit() and count.isdigit() \
                and sides != '0' and count != '0':
            dice: Dice = Dice(int(sides))
            result = sum([dice.throw() for _ in range(int(count))])
        else:
            result = 0
        self.result.text = f'{result}'
        return self.result.text

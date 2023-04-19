from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice


class DicePanel(MDBoxLayout):

    def remove(self):
        self.parent.remove_widget(self)


class Container(MDBoxLayout):

    def view_throws(self):
        sides: str = self.sides_input.text
        count: str = self.count_input.text
        if sides not in ['', '0'] and count not in ['', '0']:
            dice: Dice = Dice(int(sides))
            result = sum([dice.throw() for _ in range(int(count))])
        else:
            result = 0
        self.result.text = f'{result}'
        return self.result.text

    def add_dice(self):
        self.add_widget(DicePanel(), index=3)

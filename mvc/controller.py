from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice


class DicePanel(MDBoxLayout):

    def remove(self):
        Container.dices.remove(self)
        self.parent.remove_widget(self)


class Container(MDBoxLayout):
    dices = list()

    def view_throws(self):
        result = 0
        for dice_panel in self.dices:
            sides: str = dice_panel.ids.sides_input.text
            count: str = dice_panel.ids.count_input.text
            if sides not in ['', '0'] and count not in ['', '0']:
                dice: Dice = Dice(int(sides))
                result += sum([dice.throw() for _ in range(int(count))])
            self.result.text = f'{result}'
        return result

    def add_dice(self):
        new_dice = DicePanel()
        self.dices.append(new_dice)
        self.add_widget(new_dice, index=3)

from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice, Wound


class DicePanel(MDBoxLayout):

    def remove(self) -> bool:
        Container.dices.remove(self)
        self.parent.remove_widget(self)

        return True


class Container(MDBoxLayout):
    dices = list()

    def __init__(self):
        super().__init__()
        self.wound = None

    def view_throws(self) -> str:
        self.wound = Wound()
        dices_result: list = []

        for dice_panel in self.dices:
            sides: str = dice_panel.ids.sides_input.text
            count: str = dice_panel.ids.count_input.text
            if sides not in ['', '0'] and count not in ['', '0']:
                dice: Dice = Dice(int(sides))
                [dices_result.append(dice.throw()) for _ in range(int(count))]

        self.wound.calculate_wounds(dices_result)
        self.result.text = f'{self.wound}'
        return f'{self.result.text}'

    def add_dice(self) -> Dice:
        new_dice = DicePanel()
        self.dices.append(new_dice)
        self.add_widget(new_dice, index=3)

        return new_dice

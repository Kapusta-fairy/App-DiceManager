from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice, Wound


class DicePanel(MDBoxLayout):

    def remove(self) -> bool:
        Container().remove_dice_panel(self)
        self.parent.remove_widget(self)

        return True


class Container(MDBoxLayout):
    _dice_panels = list()

    def __init__(self):
        super().__init__()
        self.add_dice_panel()
        self.wound = None

    def remove_dice_panel(self, dice_panel: DicePanel) -> bool:
        self._dice_panels.remove(dice_panel)

        return True

    def view_throws(self) -> str:
        self.wound = Wound()
        dices_result: list = []

        for dice_panel in self._dice_panels:
            sides: str = dice_panel.ids.sides_input.text
            count: str = dice_panel.ids.count_input.text
            if sides not in ['', '0'] and count not in ['', '0']:
                dice: Dice = Dice(int(sides))
                [dices_result.append(dice.throw()) for _ in range(int(count))]

        self.wound.calculate_wounds(dices_result)
        self.result.text = f'{self.wound}'
        return f'{self.result.text}'

    def add_dice_panel(self) -> Dice:
        new_dice_panel = DicePanel()
        self._dice_panels.append(new_dice_panel)
        self.add_widget(new_dice_panel, index=3)

        return new_dice_panel

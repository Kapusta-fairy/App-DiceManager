from kivymd.uix.boxlayout import MDBoxLayout

from mvc.model import Dice


class DicePanel(MDBoxLayout):

    def remove(self):
        Container.dices.remove(self)
        self.parent.remove_widget(self)


class Container(MDBoxLayout):
    dices = list()

    def __init__(self):
        super().__init__()
        self.injured = self.__parse_injured()

    def view_throws(self) -> str:
        result = 0

        for dice_panel in self.dices:
            sides: str = dice_panel.ids.sides_input.text
            count: str = dice_panel.ids.count_input.text
            if sides not in ['', '0'] and count not in ['', '0']:
                dice: Dice = Dice(int(sides))
                result += sum([dice.throw() for _ in range(int(count))])

        self.result.text = self.create_result_string(result)
        return self.result.text

    def add_dice(self):
        new_dice = DicePanel()
        self.dices.append(new_dice)
        self.add_widget(new_dice, index=3)

    def create_result_string(self, result) -> str:
        if len(self.injured) - 1 > result:
            inj = self.injured[result]
        else:
            inj = self.injured[len(self.injured) - 1]
        return f'{inj}({result})'

    @staticmethod
    def __parse_injured():
        injured_dict = dict()
        with open('injured.txt', 'r') as file:
            injured = file.read()
        for i in injured.split('\n'):
            i = i.split('=')
            injured_dict[int(i[0].strip())] = i[1].strip()

        temp_list = []
        temp_value = 'Нет результата'
        for index in range(max(injured_dict) + 1):
            if index in injured_dict:
                temp_value = injured_dict.get(index)
            temp_list.append(temp_value)

        return temp_list

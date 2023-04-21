import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
from random import randint

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout


class DicePanel(MDBoxLayout):

    def remove(self) -> bool:
        Container().remove_dice_panel(self)
        self.parent.remove_widget(self)

        return True


class Dice(object):

    def __init__(self, sides: int):
        self._sides: int = sides
        self._last_throw: int = 0

    def throw(self) -> int:
        return randint(1, self._sides)

    def __str__(self):
        return f'd{self._sides}'


class Wound(object):

    def __init__(self, count: int = 0):
        _wounds_file_path = 'wounds.txt'

        self._count: float = count
        self._wounds_list: list = self._create_wounds_list(_wounds_file_path)

    def calculate_wounds(self, dices_result: list) -> float:
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
            file_woulds[int(key_value[0].strip())] = float(
                key_value[1].strip())

        return file_woulds

    def __len__(self):
        return self._count

    def __str__(self):
        return f'{self._count} ранений'


class Container(MDBoxLayout):
    _dice_panels = list()

    def __init__(self):
        super().__init__()
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


class MainApp(MDApp):
    title = 'Калькулятор ранений'

    def __init__(self):
        super().__init__()
        Builder.load_string('''
<DicePanel>:
    spacing: 10

    MDIconButton:
        icon: 'dice-d20'

    MDTextField:
        id: count_input
        text: '1'
        multiline: False
        input_type: 'number'
        input_filter: 'int'

    MDIconButton:
        icon: 'alpha-d'

    MDTextField:
        id: sides_input
        multiline: False
        input_type: 'number'
        input_filter: 'int'

    MDRectangleFlatIconButton:
        icon: 'minus'
        size_hint: 1, None
        text: 'удалить'

        on_release:
            root.remove()


<Container>:
    font_size: 25
    orientation: "vertical"
    spacing: 20
    padding: 20

    result: result

    MDRectangleFlatIconButton:
        icon: "plus"
        size_hint: 1, None
        text: 'добавить'

        on_release:
            root.add_dice_panel()

    MDRectangleFlatIconButton:
        icon: "equal"
        size_hint: 1, None
        text: 'результат'

        on_release:
            root.view_throws()


    MDLabel:
        id: result
        text: ''

        ''')
        Window.size = (420, 360)
        Window.minimum_width = 420
        Window.minimum_height = 260

    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

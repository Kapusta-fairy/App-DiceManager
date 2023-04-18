from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class Dice(object):
    ...


class Container(MDBoxLayout):
    ...


class MainApp(MDApp):
    title = 'Калькулятор дайсов'

    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

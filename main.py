from kivy.config import Config
Config.set('graphics', 'width', '420')
Config.set('graphics', 'height', '260')
Config.set('graphics', 'minimum_width', '420')
Config.set('graphics', 'minimum_height', '260')

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class Dice(object):
    ...


class Container(MDBoxLayout):
    ...


class MainApp(MDApp):
    title = 'Калькулятор ранений'

    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

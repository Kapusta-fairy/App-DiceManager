from kivy.config import Config
Config.set('graphics', 'width', '420')
Config.set('graphics', 'height', '360')
Config.set('graphics', 'minimum_width', '420')
Config.set('graphics', 'minimum_height', '260')

from kivy.lang import Builder
from kivymd.app import MDApp

from mvc.controller import Container


class MainApp(MDApp):
    title = 'Калькулятор ранений'

    def __init__(self):
        super().__init__()
        Builder.load_file('mvc/view.kv')

    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from mvc.controller import Container


class MainApp(MDApp):
    title = 'Калькулятор ранений'

    def __init__(self):
        super().__init__()
        Builder.load_file('mvc/view.kv')
        Window.size = (420, 360)
        Window.minimum_width = 420
        Window.minimum_height = 260

    def build(self):
        return Container()


if __name__ == '__main__':
    MainApp().run()

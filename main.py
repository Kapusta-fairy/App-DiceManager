from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from mvc.controller import Container


class MainApp(MDApp):
    title = 'Калькулятор ранений'

    def build(self):
        Window.size = (420, 360)
        Window.minimum_width = 420
        Window.minimum_height = 260

        Builder.load_file('mvc/view.kv')
        self.icon = 'icon.png'
        self.theme_cls.primary_palette = "Gray"

        return Container()


if __name__ == '__main__':
    MainApp().run()

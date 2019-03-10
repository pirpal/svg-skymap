#!usr/bin/env python3
# coding: utf8

try:
    from kivy.app import App
    from kivy.graphics import *
    from kivy.graphics.context_instructions import Color
    from kivy.uix.widget import Widget
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.gridlayout import GridLayout
except ModuleNotFoundError as e:
    print(e)


class SkyMapCanvas(Widget):
    def __init__(self, **kwargs):
        super(SkyMapCanvas, self).__init__(**kwargs)
        with self.canvas:
            # add your instruction for main canvas here
            Color(1, 0.8, .4, mode='rgb')
            Rectangle(pos=(10, 10), size=(50, 50))
            Rectangle(pos=(100, 30), size=(20, 20))

        with self.canvas.before:
            # you can use this to add instructions rendered before
            pass
        with self.canvas.after:
            # you can use this to add instructions rendered after
            pass


    def drawConstellation():
        pass

class TestApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        canvas = SkyMapCanvas()
        layout.add_widget(canvas)
        return layout


if __name__ == "__main__":
    TestApp().run()

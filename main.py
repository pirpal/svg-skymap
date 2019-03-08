#!usr/bin/env python3
# coding: utf8

try:
    from kivy.app import App
    from kivy.uix.button import Button
except ModuleNotFoundError as e:
    print(f"!e> {e}")

class TestApp(App):
    def build(self):
        return Button(text="Hello World!")


if __name__ == "__main__":
    TestApp().run()

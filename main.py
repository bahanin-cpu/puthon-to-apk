import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    return get_display(arabic_reshaper.reshape(text))


def find_font():
    for path in (
        "/system/fonts/NotoNaskhArabic-Regular.ttf",
        "/system/fonts/NotoNaskhArabicUI-Regular.ttf",
        "/system/fonts/DroidSansArabic.ttf",
    ):
        if os.path.exists(path):
            return path
    return "Roboto"


class MyApp(App):
    def build(self):
        font = find_font()
        numbers = [13, 7, 3, 5]
        total = sum(numbers)
        average = total / len(numbers)

        box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        box.add_widget(Label(text=fa("سلام خوبی"), font_name=font, font_size=32))
        box.add_widget(Label(text=f"Sum of 13 and 7 and 3 and 5 is {total}", font_size=24))
        box.add_widget(Label(text=f"Average of them is {average:g}", font_size=24))
        box.add_widget(Label(text=fa("خدانگهدار"), font_name=font, font_size=32))
        return box


MyApp().run()

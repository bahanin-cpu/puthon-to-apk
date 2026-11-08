from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(
            text="سلام خوبی\n\n"
                 "Sum of 13 and 7 and 3 and 5 is 28\n\n"
                 "خدانگهدار",
            font_size=24
        )

MyApp().run()
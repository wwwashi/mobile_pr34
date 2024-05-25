from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# define colors and their corresponding hex codes
COLORS = {
    "#ff0000": "Красный",
    "#ff8800": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#00ffff": "Голубой",
    "#0000ff": "Синий",
    "#ff00ff": "Фиолетовый"
}

class RainbowApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.code_label = Label(text="")
        self.name_label = Label(text="")
        layout.add_widget(self.code_label)
        layout.add_widget(self.name_label)

        for hex_code, color_name in COLORS.items():
            button = Button(text=color_name, background_color=[int(hex_code.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4)])
            button.bind(on_press=lambda button, h=hex_code, n=color_name: self.on_button_click(h, n))
            layout.add_widget(button)

        return layout

    def on_button_click(self, hex_code, color_name):
        self.code_label.text = hex_code
        self.name_label.text = color_name

if __name__ == '__main__':
    RainbowApp().run()
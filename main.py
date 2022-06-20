from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '450')


class MainApp(App):
    def build(self):
        self.title = 'Calculator'
        self.key = True
        self.formula = '0'
        box = BoxLayout(orientation='vertical', padding=25)

        self.label = Label(text='0', font_size=40, size_hint=(1, .3), halign='right', valign='center',
                           text_size=(350 - 50, 450 * 0.3 - 50))
        grid = GridLayout(cols=4, spacing=3, size_hint=(1, .7))

        grid.add_widget(Button(text='7', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='8', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='9', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='X', font_size=20, on_press=self.add_operation))

        grid.add_widget(Button(text='4', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='5', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='6', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='-', font_size=20, on_press=self.add_operation))

        grid.add_widget(Button(text='1', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='2', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='3', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='+', font_size=20, on_press=self.add_operation))

        grid.add_widget(Button(text='C', font_size=20, on_press=self.clear_label))
        grid.add_widget(Button(text='0', font_size=20, on_press=self.add_number))
        grid.add_widget(Button(text='.', font_size=20, on_press=self.add_point))
        grid.add_widget(Button(text='=', font_size=20, on_press=self.result))

        box.add_widget(self.label)
        box.add_widget(grid)

        return box

    def add_number(self, instance):
        self.key = True
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_point(self, instance):
        if self.key == True:

            if self.formula == '0':
                self.formula = ''

            self.formula += str(instance.text)
            self.update_label()
            self.key = False
        else:
            print('service Error!')

    def add_operation(self, instance):
        if self.key == True:
            if (str(instance.text).lower() == 'x'):
                self.formula += '*'
            else:
                self.formula += str(instance.text)

            self.update_label()
            self.key = False

        else:
            print('service error!')

    def result(self, instance):
        self.label.text = str(eval(self.label.text))

    def clear_label(self, instance):
        self.formula = '0'
        self.update_label()

    def update_label(self):
        self.label.text = self.formula


if __name__ == '__main__':
    MainApp().run()

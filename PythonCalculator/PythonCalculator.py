from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
import kivy

Window.size = (640, 700)

kivy.require('1.9.0')

#got_result = BooleanProperty(False)
INVALID_INPUT = '''Can't divide by 0'''

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
        self.calculator_field.text = '0'

    def calculator_symbol(self, symbol):
        if INVALID_INPUT in self.calculator_field.text or self.calculator_field.text == '0':
            self.calculator_field.text = ''
        
        self.calculator_field.text += symbol

    def clear(self):
        self.calculator_field.text = '0'

    def get_result(self):
        #put boolean set to true to clear when number is inputed after a result is given
        try:
            self.calculator_field.text = str(eval(self.calculator_field.text))
        except :
            self.calculator_field.text = INVALID_INPUT

    def delete(self):
        new_calculator_field = self.calculator_field.text[:-1]
        self.calculator_field.text = new_calculator_field

class Calculator(App):
    def build(self):
        return MyRoot()

calculator = Calculator()
calculator.run()
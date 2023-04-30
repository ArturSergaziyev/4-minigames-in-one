from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

from pong import *

#######COLORS_LABELS########
hx_lbl = "#99FF99"

#######COLORS_BUTTONS########
hx_btn = "#4542f5"

class mainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text = 'Тестовый приложение',
                          color = "#99FF99",
                          font_size = 15)
        self.button = Button(text = 'Далее',
                            size_hint=(0.3, 0), 
                            pos_hint={'center_x': 0.5})
        self.button.on_press = self.next
        
        vl = BoxLayout(orientation = 'vertical')
        
        vl.add_widget(self.title)
        vl.add_widget(self.button)
        self.add_widget(vl)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'win1'

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = Label(text = 'Второй экран',
                          color = "#99FF99",
                          font_size = 15)
        self.button = Button(text = 'Далее',
                            size_hint=(0.3, 0), 
                            pos_hint={'center_x': 0.5})
        self.button.on_press = self.next
        
        vl = BoxLayout(orientation = 'vertical')
        
        vl.add_widget(self.title)
        vl.add_widget(self.button)
        self.add_widget(vl)

    def next(self):
        print('next screen')

class MainCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainScr(name='main'))
        sm.add_widget(FirstScr(name='win1'))
        return sm

app = MainCheck()
app.run()

# Создание и запуск приложения, программирование интерфейса экранов и действий на них

# Здесь должен быть твой код
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from seconds import Seconds
from ruffier import *
from instructions import *
from scrollLabel import ScrollLabel

p1, p2, p3 = 0, 0, 0
name = ''
age = 7
def check_int(value):
    try:
        return int(value)
    except:
        return False

class InitScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext = txt_instruction)

        l1 = Label(text = "Введите имя:")
        self.name_input = TextInput()

        l2 = Label(text = "Введите возраст. Он должен быть больше 7-ми лет:")
        self.age_input = TextInput()

        self.btn = Button(text="Начать")
        self.btn.background_color = (0, 0.5, 0.5, 1)
        self.btn.on_press = self.next

        line1 = BoxLayout(orientation = "vertical", size_hint = (1, None), height = '60sp')        
        line1.add_widget(l1)
        line1.add_widget(self.name_input)


        line2 = BoxLayout(orientation = "vertical", size_hint = (1, None), height = '60sp')        
        line2.add_widget(l2)  
        line2.add_widget(self.age_input) 

        linemain = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        linemain.add_widget(instr)
        linemain.add_widget(line1)
        linemain.add_widget(line2)   
        linemain.add_widget(self.btn)                  

        self.add_widget(linemain)

    def next(self):
        global age, name
        name = self.name_input.text
        age = check_int(self.age_input.text)
        if name != '' and age != False and age >= 7:
            self.manager.current = "test"


class TestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext = txt_test1)
        self.ltimer = Seconds(15)
        self.ltimer.bind(done = self.timer_end)

        l1 = Label(text = "Запишите результат")
        self.test1_input = TextInput(text = "0")
        self.test1_input.set_disabled(True)

        line1 = BoxLayout(orientation = "vertical", size_hint = (1, None), height = '60sp')        
        line1.add_widget(l1)
        line1.add_widget(self.test1_input)

        self.btn = Button(text="Нажми, если ты живой.")
        self.btn.background_color = (0, 0.5, 0.5, 1)
        self.btn.on_press = self.next
        self.btn.set_disabled(True)

        linemain = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        linemain.add_widget(instr)
        linemain.add_widget(self.ltimer)
        linemain.add_widget(line1)   
        linemain.add_widget(self.btn) 

        self.add_widget(linemain)

    def on_enter(self):
        self.ltimer.start()

    def timer_end(self, *args):
        self.test1_input.set_disabled(False)
        self.btn.set_disabled(False)

    def next(self):
        global p1 
        p1 = check_int (self.test1_input.text)
        if p1 != False and p1 > 0:
            self.manager.current = "sitting"

class SittingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext = txt_sitting)

        self.ltimer = Seconds(45)
        self.ltimer.bind(done = self.timer_end)


        self.btn = Button(text="Нажми, если ты живой.")
        self.btn.background_color = (0, 0.5, 0.5, 1)
        self.btn.on_press = self.next
        self.btn.set_disabled(True)

        linemain = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        linemain.add_widget(instr)
        linemain.add_widget(self.ltimer)
        linemain.add_widget(self.btn) 

        self.add_widget(linemain)

    def on_enter(self):
        self.ltimer.start()

    def timer_end(self, *args):
        self.btn.set_disabled(False)

    def next(self):
        self.manager.current = "test_result"

class Test2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = ScrollLabel(ltext = txt_test2)

        self.t1 = Seconds(15)
        self.t2 = Seconds(45)
        self.t3 = Seconds(15)
        self.t1.bind(done = self.t1_end)
        self.t2.bind(done = self.t2_end)
        self.t3.bind(done = self.t3_end)


        l1 = Label(text = "Результат после приседаний:")
        self.test2_input = TextInput()
        self.test2_input.set_disabled(True)

        l2 = Label(text = "Результат после отдыха:")
        self.test3_input = TextInput()
        self.test3_input.set_disabled(True)

        self.btn = Button(text="Нажми, если ты живой")
        self.btn.background_color = (0, 0.5, 0.5, 1)
        self.btn.on_press = self.next
        self.btn.set_disabled(True)

        line1 = BoxLayout(orientation = "vertical", size_hint = (1, None), height = '60sp')        
        line1.add_widget(l1)
        line1.add_widget(self.test2_input)


        line2 = BoxLayout(orientation = "vertical", size_hint = (1, None), height = '60sp')        
        line2.add_widget(l2)  
        line2.add_widget(self.test3_input) 

        linemain = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        linemain.add_widget(instr)
        linemain.add_widget(line1)
        linemain.add_widget(line2)   
        linemain.add_widget(self.btn)                  

        self.add_widget(linemain)

    def on_enter(self):
        self.t1.start()
        self.t2.start()

    def t1_end(self, *args):
        self.test2_input.set_disabled(False)

    def t2_end(self, *args):
        self.t3.start()

    def t3_end(self, *args):
        self.test3_input.set_disabled(False)
        self.btn.set_disabled(False)

    def next(self):
        global p2, p3
        p2 = check_int(self.test2_input.text)
        p3 = check_int(self.test3_input.text)
        if p2 != False and p2 > 0 and p3 != False and p3 > 0:
            self.manager.current = "result"

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.l = ScrollLabel(ltext = '')
        self.add_widget(self.l)



    def on_enter(self):
        index = ruffier_index(p1,p2,p3)
        self.l.label.text = '\nВаш индекс чо-то там равен ' + str(index)


class CheckHeart(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InitScreen(name="main"))        
        sm.add_widget(TestScreen(name="test"))
        sm.add_widget(SittingScreen(name="sitting"))
        sm.add_widget(Test2Screen(name="test_result"))
        sm.add_widget(ResultScreen(name = "result"))
        return sm

app = CheckHeart()
app.run()
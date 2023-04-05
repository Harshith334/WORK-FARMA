from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.label import MDLabel
from screens import screen_helper
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
Window.size=(350,600)
class MenuScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
class SignupScreen1(Screen):
    pass
class Workers_list(Screen):
    """workers"""
class Worker_profile(Screen):
    pass
class checkout(Screen):
    pass
sm=ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
class FARMA(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.theme_style="Dark"
        screen = Builder.load_string(screen_helper)

        return screen

FARMA().run()

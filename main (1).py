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
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
import sqlite3

Window.size=(350,600)
sm=ScreenManager()

db_name = "database.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (
                                        name TEXT,
                                        aadhar integer,
                                        phone integer,
                                        state text,
                                        city text)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS validData (
                                        Uname TEXT,
                                        pass1 TEXT,
                                        pass2 TEXT)''')
conn.commit()
class MenuScreen(Screen):
    pass
class LoginScreen(Screen):
    def get_data(self):
        n1=self.ids.name1.text
        p1=self.ids.password.text
        cursor.execute('SELECT * FROM validData WHERE Uname=? AND pass1=?',(n1,p1))
        valid_user=cursor.fetchone()
        if valid_user:
            app = MDApp.get_running_app()
            app.screen.current='worker'
        else:
            alert_box = MDDialog(title="Error", text="Invalid username/password")
            alert_box.open()
class SignupScreen(Screen):
    def get_info(self):
        self.Name_sign=self.ids.name_sign.text
        self.Aadhar_no=self.ids.aadhar_no.text
        self.Phone_no=self.ids.phone_no.text
        self.State_name=self.ids.state_name.text
        self.City_name=self.ids.city_name.text
        cursor.execute('INSERT INTO mytable VALUES(:name, :aadhar, :phone, :state, :city)',
                       {'name':self.Name_sign, 'aadhar':self.Aadhar_no, 'phone':self.Phone_no, 'state':self.State_name, 'city':self.City_name})
        app = MDApp.get_running_app()
        app.screen.current='signup1'
class SignupScreen1(Screen):
    def get_Udata(self):
        if self.ids.pass1.text == self.ids.pass2.text :
            self.uname_sign=self.ids.UName.text
            self.pass_1=self.ids.pass1.text
            self.pass_2=self.ids.pass2.text
            cursor.execute('INSERT INTO validData VALUES(:Uname, :pass1, :pass2)',
                           {'Uname':self.uname_sign, 'pass1':self.pass_1, 'pass2':self.pass_2})
            print("data updated")
            app = MDApp.get_running_app()
            app.screen.current='login'
            
        else:
            alert_box1 = MDDialog(title="Error", text="Passwords did not match")
            alert_box1.open()
class Workers_list(Screen):
    """workers"""
class Worker_profile(Screen):
    pass
class Adavnced_techinologies(Screen):
    pass
class Rent_Machinery(Screen):
    pass
class Pesticides(Screen):
    pass
class Godown_Rent(Screen):
    pass
class help_desk(Screen):
    pass
sm=ScreenManager()

sm.add_widget(MenuScreen(name='menu'))
class FARMA(MDApp):
    def checkout(self):
        
        pop_up=MDDialog(title='Booking Success',text='Thanks for choosing WorkFarma')
        pop_up.open()
    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.theme_style="Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen
    def  on_stop(self):
        conn.commit()
        conn.close()

FARMA().run()

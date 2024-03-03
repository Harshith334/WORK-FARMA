screen_helper = """
ScreenManager:
    MenuScreen
    LoginScreen
    SignupScreen
    SignupScreen1
    Workers_list
    Worker_profile
    Adavnced_techinologies
    Rent_Machinery
    Pesticides
    Godown_Rent
    help_desk
    

<MenuScreen>
    name:"menu"
    MDLabel:
        text:"FARMA-DEMO"
        halign:'center'
        theme_text_color:'Primary'
        font_style:'H4'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        theme_style:'Dark'
    MDRaisedButton:
        text:"LOGIN"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_press:root.manager.current='login'
    MDRaisedButton:
        text:"SIGN-UP"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        on_press:root.manager.current='signup'
    
    
<LoginScreen>
    name:"login"
    MDLabel:
        text:"FARMA-LOGO"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        font_style:'H4'
        
    MDTextField:
        id:name1
        hint_text:"Enter Username"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id:password
        password:True
        hint_text:"Enter Password"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"LOGIN"
        pos_hint:{'center_x':0.7,'center_y':0.2}
        on_press:root.get_data()
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.2}
        on_press:root.manager.current="menu"
        
    
<SignupScreen>
    name:"signup"
    MDLabel:
        text:"WELCOME TO SIGN-UP PAGE"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.9}
        font_style:'H4'
        theme_text_color:'Primary'
    MDTextField:
        id:name_sign
        hint_text:"Enter Name"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDTextField:
        id:aadhar_no
        hint_text:"Enter Aadhar Number"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id:phone_no
        hint_text:"Enter PhoneNumber"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDTextField:
        id:state_name
        hint_text:"Enter State"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDTextField:
        id:city_name
        hint_text:"Enter City/Village"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"Next"
        pos_hint:{'center_x':0.7,'center_y':0.1}
        on_press:root.get_info()
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.1}
        on_press:root.manager.current="menu"
<SignupScreen1>
    name:'signup1'
    MDLabel:
        text:"WELCOME TO SIGN-UP PAGE"
        halign:"center"
        pos_hint:{'center_x':0.5,'center_y':0.9}
        font_style:'H4'
        theme_text_color:'Primary'
    MDTextField:
        id:UName
        hint_text:"Enter User-Name"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300   
    MDTextField:
        id:pass1
        hint_text:"Enter Password"
        password:True
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDTextField:
        id:pass2
        hint_text:"Re-Enter Password"
        password:True
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDRaisedButton:
        text:"SUBMIT"
        pos_hint:{'center_x':0.7,'center_y':0.3}
        on_press:root.get_Udata()
    MDRaisedButton:
        text:"BACK"
        pos_hint:{'center_x':0.2,'center_y':0.3}
        on_press:root.manager.current="signup"
<Adavnced_techinologies>
    name:'Advancedtechnology'
    MDNavigationLayout:
        md_bg_color: [0.749, 0.722, 0.678, 1]
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: [26/255, 255/255, 163/255, 1]
                MDRaisedButton:
                    text:"BACK"
                    pos_hint:{'center_x':0.3,'center_y':0.1}
                    on_press:root.manager.current="worker"
                    md_bg_color: [0, 0.8, 0, 1]
                    
                
            
                MDCard:
                    size_hint: (0.6 * 1.2, 0.3 * 1.2) 
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: [0/255, 204/255, 255/255, 1]

                    BoxLayout:
                        orientation: 'vertical'

                        Image:
                            source: 'drone.jpg'  
                            size_hint_y: None
                            height: dp(200 * 0.8) 

                        MDLabel:
                            text: 'Drones'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Rent: $60/hour'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Price: $6000'
                            theme_text_color: 'Primary'
                            halign: 'center'

                    
<Pesticides>
    name:'Pesticides'
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: [26/255, 255/255, 163/255, 1]
                MDRaisedButton:
                    text:"BACK"
                    pos_hint:{'center_x':0.3,'center_y':0.1}
                    on_press:root.manager.current="worker"
                    md_bg_color: [0, 0.8, 0, 1]
                    
                
            
                MDCard:
                    size_hint: (0.6 * 1.2, 0.3 * 1.2) 
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: [0/255, 204/255, 255/255, 1]  

                    BoxLayout:
                        orientation: 'vertical'

                        Image:
                            source: 'pesticide2.jpeg'
                            size_hint_y: None
                            height: dp(200 * 0.8)

                        MDLabel:
                            text: 'Pesticides'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Rent: $80/hour'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Price: $9000'
                            theme_text_color: 'Primary'
                            halign: 'center'

                    
                    
            
                    
<Rent_Machinery>
    name:'RentMachinery'
    MDNavigationLayout:
        ScreenManager:
       
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: [26/255, 255/255, 163/255, 1]
                MDRaisedButton:
                    text:"BACK"
                    md_bg_color: [0, 0.8, 0, 1]
                    pos_hint:{'center_x':0.3,'center_y':0.1}
                    on_press:root.manager.current="worker"
                    
                    
               
            
                MDCard:
                    size_hint: (0.6 * 1.2, 0.3 * 1.2) 
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: [0/255, 204/255, 255/255, 1]  
                    

                    BoxLayout:
                        orientation: 'vertical'

                        Image:
                            source: 'tractor.jpg'  
                            size_hint_y: None
                            height: dp(200 * 0.8)  

                        MDLabel:
                            text: 'Tractors'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Rent: $10/hour' 
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Price: $8000'
                            theme_text_color: 'Primary'
                            halign: 'center'
<Godown_Rent>
    name:'GodownRent'
    MDNavigationLayout:
        ScreenManager:
            MDScreen:
               
                MDBoxLayout:
                    orientation: 'vertical'
                    md_bg_color: [26/255, 255/255, 163/255, 1]
                MDRaisedButton:
                    text:"BACK"
                    md_bg_color: [0, 0.8, 0, 1]
                    pos_hint:{'center_x':0.3,'center_y':0.1}
                    on_press:root.manager.current="worker"
                    
            
                MDCard:
                    size_hint: (0.6 * 1.2, 0.3 * 1.2) 
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    md_bg_color: [0/255, 204/255, 255/255, 1] 
                 

                    BoxLayout:
                        orientation: 'vertical'

                        Image:
                            source: 'godown.jpg'  
                            size_hint_y: None
                            height: dp(200 * 0.8) 

                        MDLabel:
                            text: 'Godown'
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Rent: $10/hour'  
                            theme_text_color: 'Primary'
                            halign: 'center'

                        MDLabel:
                            text: 'Price: $11000' 
                            theme_text_color: 'Primary'
                            halign: 'center'

        
<workers_list>
    name:'worker'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Demo'
                        elevation: 4
                        left_action_items: [['menu', lambda x: nav_draw.set_state('open')]]
                        md_bg_color:[153/255,136/255,136/255,1]
                      
                    MDCard:
                        size_hint:(1,.9)
                        pos_hint:{'center_x':.5,'center_y':.39}
                        md_bg_color:[102/255,255/255,153/255, 1]
                        radius:[15]
                        ScrollView:
                            MDList:
                                ThreeLineAvatarListItem:
                                    on_release:root.manager.current='worker_profile'
                                    text:'Thripurari Venkata srikar'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:20yr'
                                    tertiary_text:'paddy'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                    
                                    
                    
                                ThreeLineAvatarListItem:
                                    text:'Vamsi'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:21'
                                    tertiary_text:'Transplantation'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Harshith'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:20'
                                    tertiary_text:'Cotton-picking'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Mohan'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:19'
                                    tertiary_text:'paddy'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Yashwanth'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:22'
                                    tertiary_text:'Transplantation'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                    
                                ThreeLineAvatarListItem:
                                    text:'Aravind'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:21'
                                    tertiary_text:'cotton-picking'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Vishnu'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:30'
                                    tertiary_text:'cultivation'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'
                                ThreeLineAvatarListItem:
                                    text:'Manikanta'
                                    theme_text_color: 'Error'
                                    secondary_theme_text_color: 'Error'
                                    tertiary_theme_text_color: 'Error'
                                    secondary_text:'Age:40'
                                    tertiary_text:'Paddy'
                                    ImageLeftWidget:
                                        source:'blank_person.jpg'  
                MDFloatingActionButton:
                    icon: "help-circle"
                    md_bg_color: app.theme_cls.primary_color  # Use the primary color of the theme
                    pos_hint: {'center_x': 0.8, 'center_y': 0.1}
                    on_press:root.manager.current="helpdesk"
                                
        MDNavigationDrawer:
            id:nav_draw
            BoxLayout:
                orientation: 'vertical'
                spacing:'8dp'
                padding:'8dp'
                Image:
                    source:'paddy.jpg'
                    size_hint_y:None
                    allow_stretch:True
                MDLabel:
                    text:"               Welcome to WorkFarma"
                    
                    size_hint_y:None
                    height:self.texture_size[1]
            
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            id:click 
                            text:'Filter'
                            IconLeftWidget:
                                icon:'filter'
                        OneLineIconListItem:
                            id:click 
                            text:'Adavnced techinologies'
                            on_press:root.manager.current="Advancedtechnology"

                            IconLeftWidget:
                                icon:'notebook-multiple'
                            
                        OneLineIconListItem:
                            id:click 
                            text:'Rent Machinery'
                            on_press:root.manager.current="RentMachinery"
                            IconLeftWidget:
                                icon:'podcast'

                        OneLineIconListItem:
                            id:click 
                            text:'Pesticides'
                            on_press:root.manager.current="Pesticides"
                            IconLeftWidget:
                                icon:'camera'
                        OneLineIconListItem:
                            id:click 
                            text:'Godown Rent'
                            on_press:root.manager.current="GodownRent"
                            IconLeftWidget:
                                icon:'relation-only-one-to-zero-or-one'
                        
                        MDRaisedButton:
                            text:"LOGOUT"
                            size_hint:(1,.9)
                            pos_hint:{'center_x':.9,'center_y':.8}
                            elevation:10
                            on_press:root.manager.current="login"
                        
<help_desk>
    name:'helpdesk'
    MDLabel:
        text:"Contact our toll-free number :+91 7893312xxx"                
<Worker_profile>
    name:'worker_profile'
    Image:
        source:'blank_person.jpg'
        pos_hint:{'center_x':0.2002,'center_y':0.8}
        size_hint:(0.3,0.5)
    MDLabel:
        text:"NAME:Tripurari venkata srikar"
        halign:'center'
        pos_hint:{'center_x':0.7,'center_y':0.9}
    MDLabel:
        text:"AGE:21"
        halign:'center'
        pos_hint:{'center_x':0.6,'center_y':0.8}
        
    MDLabel:
        text:"EXPERIENCE:2yrs"
        halign:'center'
        pos_hint:{'center_x':0.7,'center_y':0.7}
    MDLabel:
        text:"Tripurari venkata srikar is a very talented person and very hardworking.Very Humble and soft natured --Sathvik"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.5}
    MDLabel:
        text:"Tripurari venkata srikar has rating 4.58/5"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.4}
    MDLabel:
        text:"Preffered Work Timings:12PM-8PM"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.3}
    MDLabel:
        text:"Locality:Zaheerabad"
        halign:'center'
        pos_hint:{'center_x':0.5,'center_y':0.2}
    
    MDRaisedButton:
        text:"Book-Now!"
        pos_hint:{'center_x':0.8,'center_y':0.1}
        on_release:app.checkout()
    MDRaisedButton:
        text:"Back"
        pos_hint:{'center_x':0.15,'center_y':0.1}
        on_press:root.manager.current="worker"
            
"""
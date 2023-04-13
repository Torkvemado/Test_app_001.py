from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_string("""
<MenuScreen>
    BoxLayout:
        orientation: 'vertical'
        spacing: "5"
        pos_hint: {"center_x": .5, "center_y": .8}

        MDRaisedButton:
            text: "Калькулятор Качества"
            md_bg_color: "green" 
            pos_hint: {"center_x": .5}
            on_press: root.manager.current = 'QualityCalculator'

        MDRaisedButton:
            text: "     Счетчик Ресурсов      "
            md_bg_color: 'green'
            pos_hint: {"center_x": .5}
            on_press: root.manager.current = 'ResourceCounter'

        MDRaisedButton:
            text: "               PvE Билд               "
            md_bg_color: 'green'
            pos_hint: {"center_x": .5}
            on_press: root.manager.current = 'PvEBuild'

        MDRaisedButton:
            text: "               PvP Билд               "
            md_bg_color: 'green'
            pos_hint:{"center_x": .5}
            on_press: root.manager.current = 'PvPBuild'

        MDRaisedButton:
            text: "  Билд Характеристик   "
            md_bg_color: 'green'
            pos_hint: {"center_x": .5}
            on_press: root.manager.current = 'BuildMainStat'

        MDRaisedButton:
            text: "             Настройки             "
            md_bg_color: 'green'
            pos_hint:{"center_x": .5}
            on_press: root.manager.current = 'Settings'

        MDRaisedButton:
            text: "  Поддержать Автора   "
            md_bg_color: 'green'
            pos_hint:{ "center_x": .5}
            on_press: root.manager.current = 'Donate'

<QualityCalculatorScreen>            
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.5, 'center_y': 1.2}
        padding: 10,10,10,10
        MDRelativeLayout:
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            
            size_hint: None , None
            size: 275, 75
            
            
        
            MDScrollView:
                size: (300, 100)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
            
                MDList:
                    
                
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Еб1  учий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    OneLineAvatarIconListItem:
                        text: "Ебучий Виджет не понятный"
                    
        
    BoxLayout:
        orientation: 'vertical'    
    
        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'

<ResourceCounterScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'

<PvEBuildScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'

<PvPBuildScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'            


<BuildMainStatScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'

<SettingsScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'

<DonateScreen>
    BoxLayout:
        orientation: 'vertical'

        MDRaisedButton:
            text: "Назад"
            on_press: root.manager.current = 'MainMenu'


""")


class MenuScreen(Screen):
    pass


class QualityCalculatorScreen(Screen):
    pass


class ResourceCounterScreen(Screen):
    pass


class PvEBuildScreen(Screen):
    pass


class PvPBuildScreen(Screen):
    pass


class BuildMainStatScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class DonateScreen(Screen):
    pass


class LifHelperMDApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='MainMenu'))
        sm.add_widget(QualityCalculatorScreen(name='QualityCalculator'))
        sm.add_widget(ResourceCounterScreen(name='ResourceCounter'))
        sm.add_widget(PvEBuildScreen(name='PvEBuild'))
        sm.add_widget(PvPBuildScreen(name='PvPBuild'))
        sm.add_widget(BuildMainStatScreen(name='BuildMainStat'))
        sm.add_widget(SettingsScreen(name="Settings"))
        sm.add_widget(DonateScreen(name="Donate"))



        return sm








if __name__ == '__main__':
    LifHelperMDApp().run()
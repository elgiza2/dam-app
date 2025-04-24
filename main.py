from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from plyer import storagepath, vibrator
from android.permissions import request_permissions, Permission
import requests
import os


Window.fullscreen = 'auto'
Window.show_cursor = False

theme_font_styles.append('arabic')
MDApp.fonts['arabic'] = 'assets/arabic_font.ttf'

class PermissionScreen(Screen):
    def request_permissions(self):
        permissions = [
            Permission.INTERNET,
            Permission.ACCESS_NETWORK_STATE,
            Permission.WRITE_EXTERNAL_STORAGE
        ]
        request_permissions(permissions, self.check_permissions)
    
    def check_permissions(self, perms, results):
        if all(results):
            self.manager.current = 'splash'
        else:
            vibrator.vibrate(0.5)  

class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.check_connection, 3)
    
    def check_connection(self, dt):
        try:
            requests.get('https://google.com', timeout=3)
            self.manager.current = 'webview'
        except:
            self.manager.current = 'error'

class WebViewScreen(Screen):
    def on_enter(self):
        self.ids.webview.url = 'https://dam-masry-home.lovable.app'
    
    def reload(self):
        self.ids.webview.reload()
        vibrator.vibrate(0.1) 

class ErrorScreen(Screen):
    def retry(self):
        self.manager.current = 'splash'

class DamApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.font_styles['arabic'] = ['arabic', 16, False, 0.15]
        
        sm = ScreenManager()
        sm.add_widget(PermissionScreen(name='permission'))
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(WebViewScreen(name='webview'))
        sm.add_widget(ErrorScreen(name='error'))
        
        return sm
    
    def on_start(self):
        if not os.path.exists('assets'):
            os.makedirs('assets')
        self.root.current = 'permission'

if __name__ == '__main__':
    DamApp().run()
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder

KV = '''
ScreenManager:
    SplashScreen:
    MainScreen:

<SplashScreen>:
    name: "splash"
    FloatLayout:
        Image:
            id: splash_image  # ✅ Fixed ID issue
            source: "topbarlogo.png"  # Replace with your image
            size_hint: (1, 1)
            allow_stretch: True
            opacity: 0  # Start invisible

<MainScreen>:
    name: "main"
    FloatLayout:
        Image:
            source: "topbarlogo.png"  # Replace with your main screen image
            size_hint: (1, 1)
            allow_stretch: True
'''

class SplashScreen(Screen):
    def on_enter(self, *args):
        # ✅ Ensure the ID is accessible
        image = self.ids.splash_image
        
        # ✅ Create fade-in & fade-out animation
        anim = Animation(opacity=1, duration=1.5) + Animation(opacity=0, duration=1.5)
        anim.bind(on_complete=lambda *x: self.switch_to_main())  # Switch to main after animation
        anim.start(image)

    def switch_to_main(self):
        self.manager.current = "main"

class MainScreen(Screen):
    pass  # We define MainScreen in KV file

class MyApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    MyApp().run()

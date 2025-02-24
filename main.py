from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class MyApp(App):

    def build(self):
        self.window = GridLayout()

        return self.window
    
if __name__ == '__main__':
    app = MyApp()
    app.run()
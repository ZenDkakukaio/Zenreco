from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

from control.layout import MyLayout


import json as js

with open("media/media.json") as f:
    data = js.load(f)





class MyApp(MDApp):
    def build(self):
        self.title = "ZEN RECOGNITION"
        self.load_file_kv()
        self.icon = data["logo"]["media1"]
        return MyLayout()



    def load_file_kv(self):
        Builder.load_file("view/layout1.kv")





if __name__ == "__main__":
    obj_app = MyApp()
    obj_app.run()


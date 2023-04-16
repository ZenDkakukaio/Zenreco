from kivy.uix.screenmanager import ScreenManager
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.core.audio import SoundLoader


import json as js

from reco_system_gesture import ZenReco



with open("media/media.json") as f:
    data = js.load(f)



obj_app = MDApp()



class MyLayout(ScreenManager):
    data_logo = data["logo"]["media1"]
    data_text = data["text"]["media2"]
    data_menu = data["menu"]["media3"]
    data_click_sound = data["click"]["media4"]
    list_entity = ["DESACTIVATION DES LAMPES", "ACTIVATION DES LAMPES"]
    def __init__(self):
        super(MyLayout, self).__init__()







    def open_menu(self):
        self.push_sound_click()
        bs = MDGridBottomSheet()
        data = {
            "Code Source" : "github",
            "Quitter" : "location-exit",
            "Rétablir" : "arrow-collapse-horizontal"
        }
        for item in data.items():
            bs.add_item(
                item[0],
                lambda x, y=item[0]: self.callback_for_menu_items(y),
                icon_src=item[1],

            )
        bs.open()



    def push_sound_click(self):
        c = SoundLoader.load(self.data_click_sound)
        if c:
            c.play()



    def callback_for_menu_items(self, y):
        if y == "Code Source":
            self.push_sound_click()
            toast("acces au repository du programme...")

        elif y == "Quitter":
            self.push_sound_click()
            obj_app.stop()

        elif y == "Rétablir":
            self.push_sound_click()
            anim_gesture = Animation(duration=2, opacity=1, size=(1, 1), pos_hint={"center_x": .5, "center_y": .42})
            anim_gesture += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": .25, "center_y": .42})
            anim_gesture.start(self.ids.id_icon_button_gesture)

            anim_voice = Animation(duration=2, opacity=1, size=(1, 1), pos_hint={"center_x": .5, "center_y": .42})
            anim_voice += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": .75, "center_y": .42})
            anim_voice.start(self.ids.id_icon_button_voice)








    def send_gesture(self, g):
        self.push_sound_click()
        anim_gesture = Animation(duration=2, opacity=1, size=(1, 1), pos_hint={"center_x": .75, "center_y": .42})
        anim_gesture += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": .42})
        anim_gesture.start(g)

        self.push_gesture_system()






    def send_voice(self, v):
        self.push_sound_click()
        anim_gesture = Animation(duration=2, opacity=1, size=(1, 1), pos_hint={"center_x": .25, "center_y": .42})
        anim_gesture += Animation(duration=1, opacity=1, size=(40, 40), pos_hint={"center_x": .5, "center_y": .42})
        anim_gesture.start(v)

        self.push_voice_system()









    def push_gesture_system(self):
        obj_control = ZenReco()
        obj_control.start_recognition()

        # if entity_command == self.list_entity[0]:
        #     toast(self.list_entity[0])
        # elif entity_command == self.list_entity[1]:
        #     toast(self.list_entity[1])










    def push_voice_system(self):
        pass
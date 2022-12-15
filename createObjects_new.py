from tkinter import Button, CENTER, Label, Entry, Checkbutton, PhotoImage
from tkinter.ttk import Combobox
from functions import COMMANDS, COLLOR0, COLLOR1, MAIN_COLLOR
from functools import partial
from classes import Objects, _Button, _ImgButton, _Combobox, _Label
from pprint import pprint


ANCHOR = {
    'CENTER': CENTER,
}


def gp(input_dict:dict, user_dict:dict, item='', custom='') -> str | int | float | list: # get parametrs on dict
    if user_dict.get(item) is not None:
        return user_dict(item)
    else:
        return input_dict.get(item, custom)


class CreateObjects:

    def __init__(self, root) -> None:
        self.root = root
        self.on_what = {
            'root': self.root,
        }

    def create_objects(self, objects:dict, config_user:dict) -> None:
        for item, value in objects.items():
            match item:
                case 'buttons':
                    self.created_objects[item] = self.create_button(buttons=value, config_user=config_user.get(item))
                case 'labels':
                    self.created_objects[item] = self.create_label(labels=value, config_user=config_user.get(item))
                case 'entrys':
                    self.created_objects[item] = self.create_entry(entrys=value, config_user=config_user.get(item))
                case 'checkbuttons':
                    self.created_objects[item] = self.create_checkbutton(checkbuttons=value, config_user=config_user.get(item))
                case 'img_buttons':
                    self.created_objects[item] = self.create_picture_button(img_buttons=value, config_user=config_user.get(item))
                case 'comboboxs':
                    self.created_objects[item] = self.create_combobox(comboboxs=value, config_user=config_user.get(item))
        Objects.objects_on_the_panel = self.created_objects

    def create_button(self, buttons:dict, config_user:dict={}) -> dict:
        buttons_dict = dict()
        for name, pr in buttons.items(): 
            ud = config_user.get('buttons', {}).get(name, {}) # user dict
            collors:list = gp(pr, ud, 'collors', 'red, green').split(',')
            interaction:str = gp(pr, ud, 'interaction', 'None')
            on_what:str = gp(pr, ud, 'on_what', 'root')
            bg:str = gp(pr, ud, 'bg', 'gray')
            font:str = gp(pr, ud, 'font', 'Curier 9')
            width:int = int(gp(pr, ud, 'width', 10))
            bd:int = int(gp(pr, ud, 'bd', 4))
            relief:str = gp(pr, ud, 'relief', 'raised')
            text_swich:list = gp(pr, ud, 'text_swich', 'STATUS OFF,STATUS ON').split(',')
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.25))
            command:str = gp(pr, ud, 'command', 'change_collor') 
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            button = _Button(
                object_=Button(
                    self.on_what[on_what],
                    bg=bg,
                    text=text_swich[0],
                    font=font,
                    width=width,
                    bd=bd,
                    relief=relief,
                    command=partial(COMMANDS[command], self.on_what[on_what], name, 'buttons')
                    ),
                interaction=interaction,
                on_what=on_what,
                bg=bg,
                font=font,
                width=width,
                bd=bd,
                relief=relief,
                name=name,
                text_swich=text_swich,
                relx=relx,
                rely=rely,
                command=command,
                collors=collors,
                anchor=anchor
            )
            button.object_.pack(pady=5)
            button.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            buttons_dict[name] = button
        return(buttons_dict)

    def create_label(self, labels:dict, config_user:dict={}) -> dict:
        labels_dict = dict()
        for name, pr in labels.items():
            ud = config_user.get('buttons', {}).get(name, {}) # user dict
            text:str = gp(pr, ud, 'text', '')
            interaction:str = gp(pr, ud, 'interaction', 'None')
            on_what:str = gp(pr, ud, 'on_what', 'root')
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.20))
            background:str = gp(pr, ud, 'background', 'gray')
            highlightthickness: int = gp(pr, ud, 'highlightthickness', 0)
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            label = _Label(
                object_=Label(
                    self.on_what[on_what],
                    text=text,
                    background=background,
                    highlightthickness=highlightthickness
                ),
                name=name,
                text=text,
                interaction=interaction,
                on_what=on_what,
                background=background,
                highlightthickness=highlightthickness,
                relx=relx,
                rely=rely,
                anchor=anchor
            )
            label.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            labels_dict[name] = label
        return(labels_dict)

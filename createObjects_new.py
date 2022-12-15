from tkinter import Button, CENTER, Label, Entry, Checkbutton, PhotoImage
from tkinter.ttk import Combobox
from functions import COMMANDS, COLLOR0, COLLOR1, MAIN_COLLOR
from functools import partial
from classes import Objects, _Button, _ImgButton, _Combobox, _Label, _Entry
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
            ud = config_user.get(name, {}) # user dict
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
            ud = config_user.get(name, {}) # user dict
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

    def create_entry(self, entrys:dict, config_user:dict={}) -> dict:
        entrys_dict =dict()
        for name, pr in entrys.items():
            ud = config_user.get(name, {}) # user dict
            text:str = gp(pr, ud, 'text', '')
            on_what:str = gp(pr, ud, 'on_what', 'root')
            weidth:int = int(gp(pr, ud, 'weidth', 10))
            heigth:int = int(gp(pr, ud, 'heigth', 5))
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.10))
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            entry = _Entry(
                object_= Entry(self.on_what[on_what], width=weidth),
                name=name,
                text=text,
                on_what=on_what,
                weidth=weidth,
                heigth=heigth,
                relx=relx,
                rely=rely,
                anchor=anchor
                )
            if text:
                entry.object_.insert(0, text)
            entry.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            entrys_dict[name] = entry
        return(entrys_dict)

    def create_picture_button(self, img_buttons:dict, config_user:dict={}) -> dict:
        img_buttons_dict = {}
        for name, pr in img_buttons.items():
            ud = config_user.get(name, {}) # user dict
            interaction:str = gp(pr, ud, 'interaction', 'None')
            on_what:str  = gp(pr, ud, 'on_what', 'root')
            bd:int = int(gp(pr, ud, 'bd', 0))
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.20))
            command:str = gp(pr, ud, 'command', 'change_checkbutton_position') 
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            activate:str = gp(pr, ud, 'activate', 'None')
            type_:str = gp(pr, ud, 'type', 'check')
            image:str = gp(pr, ud, 'image', 'yes')
            images:list = gp(pr, ud, 'images', 'yes,no,null').split(',') 
            highlightthickness:int = int(gp(pr, ud, 'highlightthickness', 0))
            activebackground:str = gp(pr, ud, 'activebackground', 'gray')
            bg:str = gp(pr, ud, 'bg', 'gray') 
            subsample:int = int(gp(pr, ud, 'subsample', 6))
            out_button = PhotoImage(file=f'buttons/{activate}.png')
            out_button = out_button.subsample(subsample, subsample)
            img_button = _ImgButton(
                object_=Button(
                    self.on_what[on_what],
                    image=out_button,
                    command=partial(command, self.on_what[on_what], name, 'img_buttons'),
                    bd=bd,
                    highlightthickness=highlightthickness,
                    activebackground=activebackground,
                    bg=bg
                ),
                interaction=interaction,
                on_what=on_what,
                bd=bd,
                name=name,
                relx=relx,
                rely=rely,
                command=command,
                anchor=anchor,
                activate=activate,
                type_=type_,
                image=image,
                images=images,
                highlightthickness=highlightthickness,
                activebackground=activebackground,
                bg=bg,
                subsample=subsample
            )
            img_button.object_.image = out_button
            img_button.object_.pack(pady=5)
            img_button.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            img_buttons_dict[name] = img_button
        return(img_buttons_dict)
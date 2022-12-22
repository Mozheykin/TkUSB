from tkinter import Button, CENTER, Label, Entry, Checkbutton, PhotoImage, BOTH, Frame
from tkinter.ttk import Combobox, Notebook 
from functions_new import COMMANDS
from functools import partial
from classes import Objects, _Button, _ImgButton, _Combobox, _Label, _Entry, _Checkbutton, _Notebook
from pprint import pprint


ANCHOR = {
    'CENTER': CENTER,
}

FILL = {
    'BOTH': BOTH,
}


def gp(input_dict:dict, user_dict:dict, item='', custom='') -> str | int | float | list: # get parametrs on dict
    if user_dict.get(item) is not None:
        return user_dict.get(item)
    else:
        return input_dict.get(item, custom)


class CreateObjects:

    def __init__(self, root) -> None:
        self.root = root
        self.on_what = {
            'root': self.root,
        }
        self.created_objects = {}

    def create_objects(self, objects:dict, config_user:dict) -> None:
        for item, value in objects.items():
            match item:
                case 'buttons':
                    self.created_objects[item] = self.create_button(buttons=value, config_user=config_user.get(item, {}))
                case 'labels':
                    self.created_objects[item] = self.create_label(labels=value, config_user=config_user.get(item, {}))
                case 'entrys':
                    self.created_objects[item] = self.create_entry(entrys=value, config_user=config_user.get(item, {}))
                case 'checkbuttons':
                    self.created_objects[item] = self.create_checkbutton(checkbuttons=value, config_user=config_user.get(item, {}))
                case 'img_buttons':
                    self.created_objects[item] = self.create_picture_button(img_buttons=value, config_user=config_user.get(item, {}))
                case 'comboboxs':
                    self.created_objects[item] = self.create_combobox(comboboxs=value, config_user=config_user.get(item, {}))
                case 'notebooks':
                    self.created_objects[item] = self.create_notebook(notebooks=value, config_user=config_user.get(item, {}))
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
            saved:str = gp(pr, ud, 'saved', 'Name')
            text_swich:list = gp(pr, ud, 'text_swich', 'STATUS OFF,STATUS ON').split(',')
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.25))
            command:str = gp(pr, ud, 'command', 'change_collor') 
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            activate:int = int(gp(pr, ud, 'activate', 0))
            button = _Button(
                object_=Button(
                    self.on_what[on_what],
                    bg=collors[activate],
                    text=text_swich[activate],
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
                saved=saved,
                text_swich=text_swich,
                relx=relx,
                rely=rely,
                command=command,
                collors=collors,
                anchor=anchor,
                activate=activate
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
            activate:str = gp(pr, ud, 'activate', 'check-yes')
            type_:str = gp(pr, ud, 'type', 'check')
            image:str = gp(pr, ud, 'image', 'yes')
            images:list = gp(pr, ud, 'images', 'yes,no,null').split(',') 
            highlightthickness:int = int(gp(pr, ud, 'highlightthickness', 0))
            activebackground:str = gp(pr, ud, 'activebackground', 'gray')
            bg:str = gp(pr, ud, 'bg', 'gray') 
            subsample:int = int(gp(pr, ud, 'subsample', 6))
            act:int = int(gp(pr, ud, 'act', 0))
            out_button = PhotoImage(file=f'buttons/{activate}.png')
            out_button = out_button.subsample(subsample, subsample)
            img_button = _ImgButton(
                object_=Button(
                    self.on_what[on_what],
                    image=out_button,
                    command=partial(COMMANDS[command], self.on_what[on_what], name, 'img_buttons'),
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
                subsample=subsample,
                act=act
            )
            img_button.object_.image = out_button
            img_button.object_.pack(pady=5)
            img_button.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            img_buttons_dict[name] = img_button
        return(img_buttons_dict)

    def create_checkbutton(self, checkbuttons:dict, config_user:dict={}) -> dict:
        checkbutton_dict =dict()
        for name, pr in checkbuttons.items():
            ud = config_user.get(name, {}) # user dict
            interaction:str = gp(pr, ud, 'interaction', 'None')
            on_what:str = gp(pr, ud, 'on_what', 'root')
            width:int = int(gp(pr, ud, 'width', 10))
            text:str = gp(pr, ud, 'text', 'None')
            background:str = gp(pr, ud, 'background', 'gray')
            relx:float = float(gp(pr, ud, 'relx', 0.15))
            rely:float = float(gp(pr, ud, 'rely', 0.15))
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')
            checkbutton = _Checkbutton(
                object_=Checkbutton(
                    self.on_what[on_what],
                    width=width,
                    text=text,
                    background=background
                ),
                interaction=interaction,
                on_what=on_what,
                name=name,
                width=width,
                text=text,
                background=background,
                relx=relx,
                rely=rely,
                anchor=anchor
            )
            checkbutton.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            checkbutton_dict[name] = checkbutton
        return(checkbutton_dict)
    
    def create_combobox(self, comboboxs:dict, config_user:dict={}) -> dict:
        combobox_dict = {}
        Objects.devices = Objects.dll.update_all_devices()
        print(Objects.devices)
        for name, pr in comboboxs.items():
            _obj = Objects.devices
            if  _obj is not None:
                values = [f"{ind}:{value['serNum']}:{value['devType']}:{value['devCnt']}" for ind, value in _obj.items()]
            else:
                values = ['None']
            ud = config_user.get(name, {}) # user dict
            interaction:str = gp(pr, ud, 'interaction', 'None')
            on_what:str = gp(pr, ud, 'on_what', 'root')
            selected_serNum:str | None = gp(pr, ud, 'selected_serNum', None)
            operation:str = gp(pr, ud, 'operation', 'Input')
            width:int = int(gp(pr, ud, 'width', 10))
            height:int = int(gp(pr, ud, 'height', 5))
            values:list = values
            textvariable:str = gp(pr, ud, 'textvariable', 'Select device')
            relx:float = gp(pr, ud, 'relx', 0.20)
            rely:float = gp(pr, ud, 'rely', 0.15)
            anchor:str = gp(pr, ud, 'anchor', 'CENTER')

            combobox = _Combobox(
                object_=Combobox(
                    self.on_what[on_what],
                    textvariable=textvariable,
                    values=values,
                    width=width,
                    height=height
                ),
                interaction=interaction,
                on_what=on_what,
                name=name,
                selected_serNum=selected_serNum,
                operation=operation,
                width=width,
                height=height,
                textvariable=textvariable,
                anchor=anchor,
                values=values,
                relx=relx,
                rely=rely
            )
            combobox.object_.place(relx=relx, rely=rely, anchor=ANCHOR[anchor])
            combobox_dict[name] = combobox#[combobox, gp(pr, 'operation')]
        return combobox_dict


    def create_notebook(self, notebooks:dict, config_user:dict={}) -> dict:
        notebook_dict = {}
        for name, pr in notebooks.items():
            ud = config_user.get(name, {})
            on_what = gp(pr, ud, 'on_what', 'root')
            interaction:str = gp(pr, ud, 'interaction', 'None')
            expand:bool = bool(gp(pr, ud, 'expand', True))
            fill:str = gp(pr, ud, 'fill', 'BOTH')
            frames:list = gp(pr, ud, 'frames', 'List1,List2,List3').split(',')
            names_frames:list = gp(pr, ud, 'names_frames', 'L1,L2,L3').split(',')
            width:int = int(gp(pr, ud, 'width', 20))
            height:int = int(gp(pr, ud, 'height', 10))
            padding:int = int(gp(pr, ud, 'padding', 0))
            relx:float = float(gp(pr, ud, 'relx', 0.1))
            rely:float = float(gp(pr, ud, 'rely', 0.1))
            x:int = int(gp(pr, ud, 'x', 0))
            y:int = int(gp(pr, ud, 'y', 0))

            main_object = Notebook(
                self.on_what[on_what],
                width=width,
                height=height,
                padding=padding
                )
            main_object.pack(fill=FILL[fill], expand=expand)
            #main_object.place(relx=relx, rely=rely)
            main_object.place(x=x, y=y)
            sub_objects = {name:{'frame':Frame(main_object, bg='gray'), 'text':text} for name, text in zip(names_frames, frames)}

            for name, frame in sub_objects.items():
                frame['frame'].pack(fill=FILL[fill], expand=expand)
                main_object.add(frame['frame'], text=frame['text'])
                self.on_what[name] = frame['frame']

            notebook = _Notebook(
                object_=main_object,
                frames_objects_=sub_objects,
                interaction=interaction,
                on_what=on_what,
                name=name,
                expand=expand,
                fill=fill,
                frames=frames,
                names_frames=names_frames,
                width=width,
                height=height,
                padding=padding,
                relx=relx,
                rely=rely,
                x=x,
                y=y
            )
            notebook_dict[name] = notebook
        return notebook_dict
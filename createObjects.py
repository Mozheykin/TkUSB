from tkinter import Button, CENTER, Label, Entry, Checkbutton, PhotoImage, StringVar
from tkinter.ttk import Combobox
from functions import COMMANDS, COLLOR0, COLLOR1, MAIN_COLLOR
from functools import partial



anchor = {
    'CENTER': CENTER,
}


def gp(input_dict:dict, item='', custom='') -> str | int | float: # get parametrs on dict
    return input_dict.get(item, custom)


class CreateObjects:
    Objects = {}

    def __init__(self, root, dll=None, heigth:int=0, width:int=0) -> None:
        self.root = root
        self.dll = dll
        self.created_objects = {}

    def create_objects(self, objects:dict, config_user:dict) -> dict:
        self.created_objects['DLL'] = self.dll
        for item, value in objects.items():
            match item:
                case 'buttons':
                    self.created_objects[item] = self.create_button(buttons=value, config_user=config_user.get('buttons', {}))
                case 'labels':
                    self.created_objects[item] = self.create_label(labels=value)
                case 'entrys':
                    self.created_objects[item] = self.create_entry(entrys=value)
                case 'checkbuttons':
                    self.created_objects[item] = self.create_checkbutton(checkbuttons=value)
                case 'img_buttons':
                    self.created_objects[item] = self.create_picture_button(img_buttons=value)
                case 'comboboxs':
                    self.created_objects[item] = self.create_combobox(comboboxs=value)
        CreateObjects.Objects = self.created_objects
        return self.created_objects

    def get_parametrs_activate(self, config_user:dict, pr:dict, name:str) -> str:
        activate_user = config_user.get(name)
        if activate_user:
            if int(activate_user.get('activate', 0)) == 1:
                return COLLOR1
            else:
                return COLLOR0
        return gp(pr, 'bg')
        

    def create_button(self, buttons:dict, config_user:dict) -> dict:
        '''Create buttons, PIN buttons names is "PIN_3" use function change_collor'''
        buttons_dict = dict()
        for name, pr in buttons.items(): #pr - parametrs dict
            collor = self.get_parametrs_activate(config_user=config_user, pr=pr, name=name)
            button = Button(self.root, bg=collor, text=gp(pr,'text'), font=gp(pr,'font'), 
                            width=gp(pr,'width',10), bd=gp(pr,'bd',4), relief=gp(pr,'relief'), 
                            command=partial(COMMANDS[gp(pr,'command')],self.root, name,'buttons'))
            button.pack(pady=5)
            button.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor')])
            
            buttons_dict[name] = button
        return(buttons_dict)
    
    def create_label(self, labels:dict) -> dict:
        labels_dict = dict()
        for name, pr in labels.items():
            label = Label(text=gp(pr,'text'), background=MAIN_COLLOR, highlightthickness=0)
            label.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor')])
            labels_dict[name] = label
        return(labels_dict)
    
    def create_entry(self, entrys:dict) -> dict:
        entrys_dict =dict()
        for name, pr in entrys.items():
            entry = Entry(width=gp(pr,'width', 10))
            entry.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor','CENTER')])
            entrys_dict[name] = entry
        return(entrys_dict)
    
    def create_checkbutton(self, checkbuttons:dict) -> dict:
        checkbutton_dict =dict()
        for name, pr in checkbuttons.items():
            checkbutton = Checkbutton(width=gp(pr,'width', 10), text=gp(pr,'text'), background=MAIN_COLLOR)
            checkbutton.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor','CENTER')])
            checkbutton_dict[name] = checkbutton
        return(checkbutton_dict)
    
    def create_picture_button(self, img_buttons:dict) -> dict:
        img_buttons_dict = {}
        for name, pr in img_buttons.items():
            name_button = f"{gp(pr, 'type', 'check')}-{gp(pr, 'image', 'yes')}"
            out_button = PhotoImage(file=f'buttons/{name_button}.png')
            subsample = int(gp(pr, 'subsample', 6))
            out_button = out_button.subsample(subsample, subsample)
            img_button = Button(self.root, image=out_button, command=partial(COMMANDS[gp(pr,'command')],self.root, name,'img_buttons'), bd=gp(pr, 'bd', 0), highlightthickness=gp(pr, 'highlightthickness', 0), activebackground=gp(pr, 'activebackground', MAIN_COLLOR), bg=gp(pr, 'bg', MAIN_COLLOR))
            img_button.image = out_button
            img_button.pack(pady=5)
            img_button.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor')])
            img_buttons_dict[name] = [img_button, gp(pr, 'image', 'yes'), gp(pr, 'type', 'check')]
        return(img_buttons_dict)
    
    def create_combobox(self, comboboxs:dict) -> dict:
        combobox_dict = {}
        for name, pr in comboboxs.items():
            combobox = Combobox(self.root, textvariable='Select device', values=['test', 'test1'], width=gp(pr, 'width', 10), height=gp(pr, 'height', 5))
            combobox.place(relx=gp(pr,'relx',0.15), rely=gp(pr,'rely',0.10), anchor=anchor[gp(pr,'anchor')])
            combobox_dict[name] = combobox
        return combobox_dict


def creator(root, objects:dict, config_user:dict, heigth:int, width:int) -> dict:
    co = CreateObjects(root=root, heigth=heigth, width=width)
    result = co.create_objects(objects=objects, config_user=config_user)
    return result

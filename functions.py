from classes import Objects
from tkinter import PhotoImage, Button, CENTER
from functools import partial
from pprint import pprint


def all_on(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    on_what = object_.on_what
    for name, object_ in objects_.items():
        if object_.on_what == on_what:
            object_ = object_._replace(activate = 1)
            object_.object_['bg'] = object_.collors[1]
            object_.object_['text'] = object_.text_swich[1]
            Objects.objects_on_the_panel[_type][name] = object_


def all_off(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    on_what = object_.on_what
    for name, object_ in objects_.items():
        if object_.on_what == on_what:
            object_ = object_._replace(activate = 0)
            object_.object_['bg'] = object_.collors[0]
            object_.object_['text'] = object_.text_swich[0]
            Objects.objects_on_the_panel[_type][name] = object_


def change_collor(root, name:str, _type:str, collor:str=None) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    state = {0:1, 1:0}
    object_ = object_._replace(activate=state[object_.activate])
    object_.object_['bg'] = object_.collors[object_.activate]
    object_.object_['text'] = object_.text_swich[object_.activate]
    interaction = Objects.objects_on_the_panel['comboboxs'].get(object_.interaction)
    if interaction:
        select_value = interaction.object_.get()
        if select_value:
            ind, serNum, devType, devCnt = select_value.split(':')
            pin_val = Objects.dll.get_pin_param(serNum=serNum, PIN=object_.saved)
            if pin_val != object_.activate:
                Objects.dll.set_pin_param(serNum=serNum, PIN=object_.saved, value=object_.activate)
    for any_name, any_object_ in objects_.items():
        if object_.saved == any_object_.saved:
            any_object_ = any_object_._replace(activate = object_.activate)
            any_object_.object_['bg'] = object_.collors[object_.activate]
            any_object_.object_['text'] = object_.text_swich[object_.activate]
            Objects.objects_on_the_panel[_type][any_name] = any_object_
    Objects.objects_on_the_panel[_type][name] = object_


def change_checkbutton_position(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    state = {0:1,1:2,2:0}
    act = state[object_.act]
    object_ = object_._replace(act=act)
    images = object_.images
    activate=f'{object_.type_}-{images[act]}'
    object_ = object_._replace(activate=activate)
    img_button = get_picture(object_.activate, object_.subsample, object_.subsample)
    x, y = get_position_object(object_.object_)
    object_.object_.destroy()
    object_ = object_._replace(object_ = Button(
        root,
        image=img_button,
        command=partial(COMMANDS[object_.command], root, name, 'img_buttons'),
        bd=object_.bd,
        highlightthickness=object_.highlightthickness,
        activebackground=object_.activebackground,
        bg=object_.bg
    ))
    object_.object_.image = img_button
    object_.object_.pack(pady=5)
    object_.object_.place(relx=object_.relx, rely=object_.rely, anchor=CENTER)
    Objects.objects_on_the_panel[_type][name] = object_


def get_picture(name_button:str, change_x:int, change_y:int) -> PhotoImage:
    img = PhotoImage(file=f'buttons/{name_button}.png')
    img = img.subsample(change_x, change_y)
    return img

def get_position_object(_object):
    return _object.winfo_x(), _object.winfo_y()

COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
    'change_checkbutton_position': change_checkbutton_position,
}
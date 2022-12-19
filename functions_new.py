from classes import Objects
from tkinter import PhotoImage, Button, CENTER
from functools import partial


def all_on(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    # TODO set dll parametrs
    on_what = object_.on_what
    for name, object_ in objects_.items():
        if object_.on_what == on_what:
            object_._replace(activate = 1)
            object_.object_['bg'] = object_.collors[1]
            object_.object_['text'] = object_.text_swich[1]
            Objects.objects_on_the_panel[_type][name] = object_


def all_off(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    # TODO set dll parametrs
    on_what = object_.on_what
    for name, object_ in objects_.items():
        if object_.on_what == on_what:
            object_._replace(activate = 0)
            object_.object_['bg'] = object_.collors[0]
            object_.object_['text'] = object_.text_swich[0]
            Objects.objects_on_the_panel[_type][name] = object_


def change_collor(root, name:str, _type:str, collor:str=None) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    state = {0:1, 1:0}
    # TODO set dll
    activate = state[object_.activate]
    object_._replace(activate = 1)
    object_.object_['bg'] = object_.collors[activate]
    object_.object_['text'] = object_.text_swich[activate]
    Objects.objects_on_the_panel[_type][name] = object_


def change_checkbutton_position(root, name:str, _type:str) -> None:
    objects_ = Objects.objects_on_the_panel.get(_type)
    object_ = objects_.get(name)
    state = {0:1,1:2,2:0}
    act = state[object_.act]
    object_._replace(act=act)
    images = object_.images
    activate=f'{object_.type_}-{images[act]}'
    object_._replace(activate=activate)
    img_button = get_picture(object_.activate, object_.subsample, object_.subsample)
    object_.object_.destroy()
    object_._replace(object_ = Button(
        Objects.objects_on_the_panel['notebooks'].get(object_.on_what),
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

COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
    'change_checkbutton_position': change_checkbutton_position,
}
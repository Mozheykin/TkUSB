import createObjects
from tkinter import PhotoImage, Button, CENTER
from functools import partial


COLLOR0, COLLOR1 = 'red', 'green'


def all_on(root, name:str, _type:str):
    buttons = createObjects.CreateObjects.Objects.get('buttons')
    for button in buttons.values():
        button.config(bg=COLLOR1)


def all_off(root, name:str, _type:str):
    buttons = createObjects.CreateObjects.Objects.get('buttons')
    for button in buttons.values():
        button.config(bg=COLLOR0)


def change_collor(root, name:str, _type:str, collor:str=None) -> None:
    type_object = createObjects.CreateObjects.Objects.get(_type)
    _object = type_object.get(name)
    if not collor:
        if _object['bg'] == COLLOR0:
            _object.config(bg=COLLOR1)
        else:
            _object.config(bg=COLLOR0)
    else:
        _object.config(bg=collor)


def get_picture(name_button:str, change_x:int, change_y:int) -> PhotoImage:
    img = PhotoImage(file=f'buttons/{name_button}.png')
    img = img.subsample(change_x, change_y)
    return img


def get_position_object(_object):
    return _object.winfo_x(), _object.winfo_y()


def change_checkbutton_position(root, name:str, _type:str) -> None:
    type_object = createObjects.CreateObjects.Objects.get(_type)
    _object = type_object.get(name)[0]
    actuall_button = None
    match type_object.get(name)[1]:
        case 'yes':
            img = get_picture(f'{type_object.get(name)[2]}-no', 6, 6)
            actuall_button = 'no'
        case 'no':
            img = get_picture(f'{type_object.get(name)[2]}-null', 6, 6)
            actuall_button = 'null'
        case 'null':
            actuall_button = 'yes'
            img = get_picture(f'{type_object.get(name)[2]}-yes', 6, 6)
    img_button = Button(root, image=img, command=partial(COMMANDS['change_checkbutton_position'],root, name,_type), bd=0, highlightthickness=0, 
    activebackground='gray', bg='gray')
    x, y = get_position_object(_object)
    _object.destroy()
    img_button.image = img
    img_button.pack(pady=5)
    img_button.place(x=x, y=y)
    createObjects.CreateObjects.Objects[_type][name] = [img_button, actuall_button, type_object.get(name)[2]]



COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
    'change_checkbutton_position': change_checkbutton_position,
}
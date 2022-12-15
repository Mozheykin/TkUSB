from tkinter import PhotoImage, Button 
from functools import partial
from loadConfiguration import save_configurations
from classes import Objects, _Combobox
from loguru import logger


COLLOR0, COLLOR1 = 'red', 'green'
MAIN_COLLOR = 'gray'


def all_on(root, name:str, _type:str):
    buttons = Objects.objects_on_the_panel.get('buttons')
    for button in buttons.values():
        button[0].config(bg=COLLOR1)


def all_off(root, name:str, _type:str):
    buttons = Objects.objects_on_the_panel.get('buttons')
    for button in buttons.values():
        button[0].config(bg=COLLOR0)


def change_collor(root, name:str, _type:str, operation:str='',collor:str=None) -> None:
    combobox:_Combobox = Objects.objects_on_the_panel['comboboxs'].get('CB1')
    # TODO get parametrs with class _Button in parametr interaction
    select_value = ''
    serNum = ''
    if combobox:
        select_value = combobox.object_.get()
        for value in combobox.values:
            if value[1] == select_value:
                serNum = value[0]
    logger.info('change_collor()'.center(75, '='))
    logger.info(f'dll: {Objects.dll}')
    logger.info(f'Objects {Objects.objects_on_the_panel}')
    logger.info(f'Select_value: {select_value}, serNum: {serNum}')
    type_object = Objects.objects_on_the_panel.get(_type)
    _object = type_object.get(name)
    if not collor:
        if _object[0]['bg'] == COLLOR0:
            logger.info(f'set_pin_param -> Enable: {Objects.dll.set_pin_param(serNum=serNum,PIN=name,value=1)}')
            _object[0].config(bg=COLLOR1)
        else:
            logger.info(f'set_pin_param -> Disable: {Objects.dll.set_pin_param(serNum=serNum,PIN=name,value=0)}')
            _object[0].config(bg=COLLOR0)
    else:
        _object[0].config(bg=collor)


def get_picture(name_button:str, change_x:int, change_y:int) -> PhotoImage:
    img = PhotoImage(file=f'buttons/{name_button}.png')
    img = img.subsample(change_x, change_y)
    return img


def get_position_object(_object):
    return _object.winfo_x(), _object.winfo_y()


def change_checkbutton_position(root, name:str, _type:str) -> None:
    type_object = Objects.objects_on_the_panel.get(_type)
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
    Objects.objects_on_the_panel[_type][name] = [img_button, actuall_button, type_object.get(name)[2]]


logger.add('functions.log', format='{time} {level} {message}', level='INFO')

COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
    'change_checkbutton_position': change_checkbutton_position,
}
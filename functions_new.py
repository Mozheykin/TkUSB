

def all_on(root, name:str, _type:str) -> None:
    pass

def all_off(root, name:str, _type:str) -> None:
    pass

def change_collor(root, name:str, _type:str, collor:str=None) -> None:
    pass

def change_checkbutton_position(root, name:str, _type:str) -> None:
    pass

COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
    'change_checkbutton_position': change_checkbutton_position,
}
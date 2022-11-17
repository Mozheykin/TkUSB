import createObjects

COLLOR0, COLLOR1 = 'red', 'green'


def all_on(name:str, _type:str):
    print(f'{name} {_type}all on')

def all_off(name:str, _type:str):
    print('all off')

def change_collor(name:str, _type:str) -> None:
    type_object = createObjects.CreateObjects.Objects.get(_type)
    _object = type_object.get(name)
    if _object['bg'] == COLLOR0:
        _object.config(bg=COLLOR1)
    else:
        _object.config(bg=COLLOR0)


COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
    'change_collor': change_collor,
}
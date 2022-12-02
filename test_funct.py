from tkinter import Tk
from loadConfiguration import load_configurations, save_configurations
from createObjects import creator, CreateObjects
from pprint import pprint
from errors import NotConfirationsOnFile
from other_sync import Sync
from functions import MAIN_COLLOR, COLLOR1
from functools import partial

GEOMETRY = '350x350'
TITLE = 'New app'
path_user_config = "user_config.xml"
path_configs = "configs.xml"


def on_exit(root, dll):
    _objects = CreateObjects.Objects
    data = {
        'buttons': {},
        'img_buttons': {},
    }
    for _object_group, _object_pr in _objects.items():
        if type(_object_pr) == dict:
            for name, _object in _object_pr.items():
                match _object_group:
                    case 'buttons': 
                        if _object['bg'] == COLLOR1:
                            data[_object_group][name] = '1'
                        else:
                            data[_object_group][name] = '0'
                    case 'img_buttons':
                        data[_object_group][name] = f'{_object[2]}-{_object[1]}'
    save_configurations(path_user=path_user_config, objects=data)
    #dll.close()
    root.destroy()


def init_tk() -> None:
    root = Tk()
    root.config(bg=MAIN_COLLOR)
    config, config_user = load_configurations(path_user=path_user_config, path_configs=path_configs)
    objects = {item: value for item, value in config['TkUSB'].items() if not item in ['title', 'geometry']}
    heigth, width = config['TkUSB']['geometry'].split('x')
    dll = Sync(root=root)
    objects = creator(root=root, dll=dll, objects=objects, config_user=config_user['TkUSB'], heigth=int(heigth), width=int(width))
    #pprint(sync(root, dll, objects['buttons']))
    root.title(config['TkUSB']['title'])
    root.geometry(config['TkUSB']['geometry'])
    root.protocol('WM_DELETE_WINDOW', partial(on_exit, root, dll))
    root.mainloop()
    


def main():
    try:
        init_tk()
    except NotConfirationsOnFile:
        exit('Configuration file not found.')
    except ValueError:
        exit('Configuration file is not correct')
    except KeyError:
        exit('Confiration file not accept main values')


if __name__ == "__main__":
    main()
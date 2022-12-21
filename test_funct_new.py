from tkinter import Tk
from loadConfiguration import load_configurations, save_configurations
from other_sync import Sync
from classes import Objects
from createObjects_new import CreateObjects
from functools import partial
from pprint import pprint

GEOMETRY = '350x350'
TITLE = 'New app'
path_user_config = "user_config_new.xml"
path_configs = "configs_new.xml"


def on_exit(root):
    _objects = Objects.objects_on_the_panel
    data = {
        'buttons': {},
        'img_buttons': {},
    }
    for _object_group, _object_pr in _objects.items():
        if type(_object_pr) == dict:
            for name, _object in _object_pr.items():
                match _object_group:
                    case 'buttons': 
                        if _object.object_['bg'] == _object.collors[1]:
                            data[_object_group][name] = '1'
                        else:
                            data[_object_group][name] = '0'
                    case 'img_buttons':
                        data[_object_group][name] = f'{_object.activate}'
    save_configurations(path=path_configs,path_user=path_user_config, objects=data)
    #dll.close()
    root.destroy()


def init_tk() -> None:
    root = Tk()
    root.config(bg='gray')
    config, config_user = load_configurations(path_user=path_user_config, path_configs=path_configs)
    objects = {item: value for item, value in config['TkUSB'].items() if not item in ['title', 'geometry']}
    heigth, width = config['TkUSB']['geometry'].split('x')
    dll = Sync()
    Objects.dll = dll
    CreatObj = CreateObjects(root=root)
    CreatObj.create_objects(objects=objects, config_user=config_user.get('TkUSB', {}))
    #pprint(sync(root, dll, objects['buttons']))
    root.title(config['TkUSB']['title'])
    root.geometry(config['TkUSB']['geometry'])
    root.protocol('WM_DELETE_WINDOW', partial(on_exit, root))
    root.mainloop()

def main():
    init_tk()


if __name__ == '__main__':
    main()
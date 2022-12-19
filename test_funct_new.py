from tkinter import Tk
from loadConfiguration import load_configurations
#from other_sync import Sync
from createObjects_new import CreateObjects

GEOMETRY = '350x350'
TITLE = 'New app'
path_user_config = "user_config_new.xml"
path_configs = "configs_new.xml"


def init_tk() -> None:
    root = Tk()
    root.config(bg='gray')
    config, config_user = load_configurations(path_user=path_user_config, path_configs=path_configs)
    objects = {item: value for item, value in config['TkUSB'].items() if not item in ['title', 'geometry']}
    heigth, width = config['TkUSB']['geometry'].split('x')
    #dll = Sync(root=root)
    CreatObj = CreateObjects(root=root)
    CreatObj.create_objects(objects=objects, config_user=config_user)
    #pprint(sync(root, dll, objects['buttons']))
    root.title(config['TkUSB']['title'])
    root.geometry(config['TkUSB']['geometry'])
    #root.protocol('WM_DELETE_WINDOW', partial(on_exit, root, dll))
    root.mainloop()

def main():
    init_tk()


if __name__ == '__main__':
    main()
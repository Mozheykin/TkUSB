from tkinter import Tk
from loadConfiguration import load_configurations
from createObjects import creator
from pprint import pprint


GEOMETRY = '350x350'
TITLE = 'New app'
path_config = "/home/legal/github/hour_contract_year/Task#1_v3_HWCleware/TkUSB/config.xml"


def init_tk() -> None:
    root = Tk()
    config = load_configurations(path=path_config)
    objects = {item: value for item, value in config['TkUSB'].items() if not item in ['title', 'geometry']}
    pprint(creator(root=root, objects=objects))
    root.title(config['TkUSB']['title'])
    root.geometry(config['TkUSB']['geometry'])
    root.mainloop()


def main():
    init_tk()


if __name__ == "__main__":
    main()
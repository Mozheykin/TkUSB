from tkinter import Tk, Button
import json


GEOMETRY = '350x350'
TITLE = 'New app'
path_config = "config.json"


def all_on():
    pass

def all_off():
    pass

COMMANDS = {
    'all_on': all_on,
    'all_off': all_off,
}


def load_json(path:str) -> None | dict:
    try:
        with open(path) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        exit('Config file not found!')


def create_button(root, buttons:dict) -> None | list:
    buttons_list = []
    for pr in buttons.values():
        button = Button(root, bg=pr['bg'], text=pr['text'], font=pr['font'], width=pr['width'], bd=pr['bd'], relief=pr['relief'], command=COMMANDS[pr['command']])
        button.pack(pady=5)
        button.place(relx=pr['relx'], rely=pr['rely'])
        buttons_list.append(button)
    return(buttons_list)


def create_objects(root, objects:dict) -> None:
    print(objects)
    for item, value in objects.items():
        match item:
            case 'buttons':
                create_button(root=root, buttons=value)


def init_tk() -> None:
    root = Tk()
    config = load_json(path=path_config)
    objects = {item: value for item, value in config.items() if not item in ['title', 'geometry']}
    create_objects(root=root, objects=objects)
    root.title(config['title'])
    root.geometry(config['geometry'])
    root.mainloop()


def main():
    init_tk()


if __name__ == "__main__":
    main()
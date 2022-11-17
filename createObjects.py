from tkinter import Button, CENTER
from functions import COMMANDS


anchor = {
    'CENTER': CENTER,
}



class CreateObjects:
    def __init__(self, root) -> None:
        self.root = root
        self.created_objects = {}

    def create_objects(self, objects:dict) -> dict:
        for item, value in objects.items():
            match item:
                case 'buttons':
                    self.created_objects['buttons'] = self.create_button(buttons=value)
        return self.created_objects

    def create_button(self, buttons:dict) -> None | dict:
        buttons_dict = dict()
        for name, pr in buttons.items():
            button = Button(self.root, bg=pr['bg'], text=pr['text'], font=pr['font'], width=pr['width'], bd=pr['bd'], relief=pr['relief'], command=COMMANDS[pr['command']])
            button.pack(pady=5)
            button.place(relx=pr['relx'], rely=pr['rely'], anchor=anchor[pr['anchor']])
            buttons_dict[name] = button
        return({'buttons': buttons_dict})


def creator(root, objects:dict) -> dict:
    co = CreateObjects(root=root)
    result = co.create_objects(objects=objects)
    return result

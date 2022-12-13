from typing import NamedTuple
from tkinter import Button
from tkinter.ttk import Combobox
from other_sync import Sync


class _Button(NamedTuple):
    _object:Button
    interaction:Combobox
    bg:str #=gray
    font:str
    width:int
    bd:int
    relief:str
    name:str # = 'PIN_'
    text_swich:list# = ['STATUS OFF', 'STATUS ON']
    relx:int
    rely:int
    command:str #= 'change_collor'
    collors_def:list #= ['red', 'green']
    
class _ImgButton(NamedTuple):
    _object:Button
    interaction:Combobox
    activate:str
    _type:str
    image:str
    

class Objects:
    objects_on_the_panel = {}
    dll:Sync



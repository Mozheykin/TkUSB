from typing import NamedTuple
from tkinter import Button
from tkinter.ttk import Combobox
from other_sync import Sync


class _Button(NamedTuple):
    object_:Button
    interaction:str
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
    object_:Button
    interaction:str
    activate:str
    type_:str
    image:str

class _Combobox(NamedTuple):
    object_:Combobox
    values:dict
    selected_serNum:str | None
    operation:str
    

class Objects:
    objects_on_the_panel = {}
    dll:Sync



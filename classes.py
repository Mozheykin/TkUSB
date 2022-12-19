from typing import NamedTuple
from tkinter import Button, Label, Entry, Checkbutton
from tkinter.ttk import Combobox, Notebook
from other_sync import Sync


class _Button(NamedTuple):
    object_:Button
    interaction:str #=None, CB1 ....
    on_what:str #=root, WD1....
    bg:str #=gray
    font:str
    width:int
    bd:int
    relief:str
    name:str # = 'PIN_'
    saved:str # = 'else PIN_name'
    text_swich:list# = ['STATUS OFF', 'STATUS ON']
    relx:float
    rely:float
    command:str #= 'change_collor'
    collors:list #= ['red', 'green']
    anchor:str

class _Label(NamedTuple):
    object_:Label
    name:str
    text:str
    interaction:str #=None, CB1 ....
    on_what:str #=root, WD1....
    background:str
    highlightthickness:int
    relx:float  
    rely:float
    anchor:str

class _Entry(NamedTuple):
    object_:Entry
    name:str
    text:str
    on_what:str #=root, WD1....
    weidth:int
    heigth:int
    relx:float
    rely:float
    anchor:str

class _ImgButton(NamedTuple):
    object_:Button
    interaction:str #=None, CB1 ....
    on_what:str #=root, WD1....
    bd:int
    name:str # = 'PIN_'
    relx:float
    rely:float
    command:str #= 'change_checkbutton_position'
    anchor:str
    activate:str
    type_:str
    image:str
    images:list #['yes', 'no', 'null']
    highlightthickness:int #0
    activebackground:str #gray
    bg:str #gray
    subsample:int #6

class _Checkbutton(NamedTuple):
    object_:Checkbutton
    interaction:str
    on_what:str
    name:str
    width:int
    text:str
    background:str
    relx:float
    rely:float
    anchor:str

class _Combobox(NamedTuple):
    object_:Combobox
    interaction:str
    on_what:str
    name:str
    selected_serNum:str | None
    operation:str
    width:int
    height:int
    textvariable:str
    anchor:str
    values:list
    relx:float
    rely:float

class _Notebook(NamedTuple):
    object_:Notebook
    frames_objects_:dict
    interaction:str
    on_what:str
    name:str # = 'NB1'
    expand:bool # = true
    fill:str # = BOTH
    frames:list # = ['List1', 'List2', 'List3']
    names_frames:list # =['L1', 'L2', 'L3']
    width:int
    height:int
    padding:int



class _Device(NamedTuple):
    id_:int
    devCnt:str
    serNum:str
    devType:int
    devVersion:int

class Objects:
    objects_on_the_panel = {}
    dll:Sync
    devices:dict



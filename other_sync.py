import createObjects
from functions import change_collor


class Sync:
    def __init__(self, root, dll, buttons:dict) -> None:
        self.dll = dll
        self.buttons = buttons
        self.root
        self.cw = self.dll.FCWInitObject()
        self.get_devises()
        
    def get_devises(self):
        self.devCnt = self.dll.FCWOpenCleware(0)
    
    def read_all_devices(self) -> dict:
        self.devices = {}
        if self.devCnt:
            for dev in range(self.devCnt):
                serNum = self.dll.FCWGetSerialNumber(self.cw, dev)
                devType = self.dll.FCWGetUSBType(self.cw, dev)

                self.devices[dev] = {
                    'serNum': serNum,
                    'devType': devType,
                    }
                
                for pin in range(8):
                    self.devices[dev][f'PIN_{pin}'] = self.dll.FCWGetSwitch(self.cw, dev, hex(pin + 16))
        return self.devices
    
    def change_collors_buutons_sync_usb(self, buttons:dict={}):
        if buttons:
            self.buttons = buttons
        for name in self.buttons.keys():
            if '_' in name:
                if self.devices[0][name] == 0:
                    collor = 'red'
                else: 
                    collor = 'green'
                change_collor(root=self.root, name=name, _type='buttons', collor=collor)
        
        
    
    def __close__(self):
        self.dll.FWCCloseCleware(0)



def sync(root, dll, buttons:dict) -> dict:
    """
    Sync all buttons, for USB spliter
    Retur list [
        {'Name_button': enabled},
        ...
        ]
    """

    sync_first = Sync(root=root, dll=dll, buttons=buttons)    
    sync_first.get_devises()
    sync_first.read_all_devices()
    sync_first.change_collors_buutons_sync_usb(buttons=buttons)
    sync_first.__close__()

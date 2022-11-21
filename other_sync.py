import createObjects

def sync() -> list:
    """
    Sync all buttons, for USB spliter
    Retur list [
        {'Name_button': enabled},
        ...
        ]
    """
    dll = createObjects.CreateObjects.Objects['DLL']
    read_all_devices(dll=dll)


    buttons = createObjects.CreateObjects.Objects['buttons']
    for name, button in buttons:
        if '_' in name:
            pass



def read_all_devices(dll) -> dict:
    devices = {}
    cw = dll.FCWInitObject()
    if devCnt:=dll.FCWOpenCleware(0):
        for dev in range(devCnt):
            serNum = dll.FCWGetSerialNumber(cw, dev)
            devType = dll.FCWGetUSBType(cw, dev)
            
            for pin in range(8):
                devices[dev][f'PIN_{pin}'] = dll.FCWGetSwitch(cw, dev, 0x1pin)

            devices[dev] = {
                'serNum': serNum,
                'devType': devType,
                'PIN_1': dll.FCWGetSwitch(cw, dev, 0x10)
                }
        

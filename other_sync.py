import createObjects
from functions import change_collor
from ctypes import windll
from loguru import logger


class Sync:
    LIBRARY = 'dll\\USBaccessX64.dll'

    _devCnt = {
        0: 'USB Multiplexer 2x4',
        1: 'USB 3.0 Connect',
        2: 'USB Switch 4',
    }

    def __init__(self, root) -> None:
        self.dll = windll.LoadLibrary(Sync.LIBRARY)
        self.dll.FCWInitObject()
        self.root = root
        self.cw = 0
        logger.add('devices.log', format='{time} {level} {message}', level='INFO')
        
    def update_all_devices(self) -> dict:
        self.devCnt = self.dll.FCWOpenCleware(self.cw)
        self.devices = {}
        if self.devCnt:
            for devNum in range(self.devCnt):
                serNum = self.dll.FCWGetSerialNumber(self.cw, devNum)
                devType = self.dll.FCWGetUSBType(self.cw, devNum)
                devVersion = self.dll.FCWGetVersion(self.cw, devNum)

                self.devices[devNum] = {
                    'serNum': serNum,
                    'devType': devType,
                    'devVersion': devVersion,
                    }
                
                for pin in range(1, 9):
                    self.devices[devNum][f'PIN_{pin}'] = self.dll.FCWGetSwitch(self.cw, devNum, hex(pin + 15))
        logger.info(f'self.devices = {self.devices}')
        return self.devices

    def get_list_devices(self):
        self.update_all_devices()
        if self.devices:
            result = [[params[dev] for dev in ['serNum', 'devType', 'devVersion']] for params in self.devices.values()] 
            logger.info(f'get_list_devices() {result}')
            return result

    def verify_serNum(self, serNum, take_params:bool=False, update:bool=False) -> int | dict | None:
        if update:
            self.update_all_devices()
        for devNum, params in self.devices.items():
            if params['serNum'] == serNum:
                if take_params:
                    return devNum, params
                else:
                    return devNum

    def set_pin_param(self, serNum, PIN:str=None, value:int=0, PINS:list=[], values:list=[]) -> bool:   
        if all([devNum:=self.verify_serNum(serNum), PIN]):
            self.dll.FCWSetSwitch(self.cw, devNum, PIN, value)
            logger.info(f'change_pin_param() {devNum}, {serNum}, {PIN}, {value}')
            return True
        elif all([devNum:=self.verify_serNum(serNum), PINS]):
            [self.dll.FCWSetSwitch(self.cw, devNum, PIN, value) for PIN, value in zip(PINS, values)]
            return True
        return False
    
    def get_pin_param(self, serNum, PIN:str=None, PINS:list=[]) -> int | list | None:
        devNum, params =self.verify_serNum(serNum, take_params=True)
        if devNum:
            if PIN:
                result = params.get(PIN)
                logger.info(f'get_pin_param() {devNum}, {serNum}, {result}')
                return result 
            elif PINS:
                result = [params.get(pin) for pin in PINS]
                logger.info(f'get_pin_param() {devNum}, {serNum}, {result}')
                return result 
    
    def set_multi_switch(self, serNum, value) -> bool:
        if devNum:=self.verify_serNum(serNum, update=True):
            self.dll.FCWSetMultiSwitch(self.cw, devNum, value)
            logger.info(f'set_multi_swirch() {devNum}, {serNum}, {value}')
            return True
        return False
    
    def get_multi_switch(self, serNum, value):
        if devNum:=self.verify_serNum(serNum, update=True):
            return self.dll.FCWGetMultiSwitch(self.cw, devNum, value, 0)

    
    def close(self):
        self.dll.FWCCloseCleware(0)

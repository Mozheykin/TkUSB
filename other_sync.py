from ctypes import windll
from loguru import logger
from loadConfiguration import load_configurations


class Sync:
    LIBRARY = 'dll\\USBaccessX64.dll'

    _devCnt = {
        'USB Switch 4': {
            'devType': 8,
            'devVersion': 513,
        },
        'USB 3.0 Connect': {
            'devType': 8,
            'devVersion': 259,
        },
        'USB Multiplexer 2x4': {
            'devType': 48,
            'devVersion': 129,
        }
    }

    def __init__(self, path_devices:str='') -> None:
        self.dll = windll.LoadLibrary(Sync.LIBRARY)
        self.dll.FCWInitObject()
        self._devCnt, _ = load_configurations(path_configs=path_devices, path_user=path_devices)
        logger.add('devices.log', format='{time} {level} {message}', level='INFO')
        
    def update_all_devices(self, cw:int=0) -> dict:
        self.devCnt = self.dll.FCWOpenCleware(cw)
        self.devices = {}
        if self.devCnt:
            for devNum in range(self.devCnt):
                serNum = self.dll.FCWGetSerialNumber(cw, devNum)
                devType = self.dll.FCWGetUSBType(cw, devNum)
                devVersion = self.dll.FCWGetVersion(cw, devNum)

                devCnt = None
                if self._devCnt:
                    for name, pr in self._devCnt['Dvices'].items():
                        if all([pr['expDevType'] == devType, pr['minVersion'] < devVersion, pr['maxVersion'] > devVersion]):
                            devCnt = pr['devName']

                self.devices[devNum] = {
                    'devCnt': devCnt,
                    'serNum': serNum,
                    'devType': devType,
                    'devVersion': devVersion,
                    }
                
                for pin in range(0, 8):
                    self.devices[devNum][f'PIN_{pin + 1}'] = self.dll.FCWGetSwitch(cw, devNum, 0x10 + pin)
        logger.info(f'self.devices = {self.devices}')
        return self.devices

    def get_list_devices(self, cw:int=0):
        self.update_all_devices(cw=cw)
        if self.devices:
            result = [[params[dev] for dev in ['serNum','devCnt','devType', 'devVersion']] for params in self.devices.values()] 
            logger.info(f'get_list_devices() {result}')
            return result

    def verify_serNum(self, serNum, take_params:bool=False, cw:int=0, update:bool=False) -> int | dict | None:
        logger.info(f'Inputs: serNim:{serNum}, take_params:{take_params}, cw:{cw}, update:{update}')
        if update:
            logger.info('verify_serNum devices updated!')
            self.update_all_devices(cw=cw)
        logger.info(f'devices:{self.devices}')
        for devNum, params in self.devices.items():
            if params['serNum'] == serNum:
                logger.info(f'SerNum finded:{serNum}')
                if take_params:
                    logger.info(f'Output: devNum:{devNum}, params:{params}')
                    return devNum, params
                else:
                    logger.info(f'Output: devNum:{devNum}')
                    return devNum

    def split_pin_for_set(self, PIN:str) -> int:
        if '_' in PIN:
            pin_num = int(PIN.split('_')[1])
            return pin_num - 1
        return 0

    def set_pin_param(self, serNum, PIN:str=None, cw:int=0, value:int=0, PINS:list=[], values:list=[]) -> bool:   
        devNum = self.verify_serNum(serNum)
        logger.info(f'set_pin_param() {devNum}, {PIN}')
        if all([devNum is not None, PIN]):
            self.dll.FCWSetSwitch(cw, devNum, 0x10 + self.split_pin_for_set(PIN), value)
            logger.info(f'change_pin_param() {devNum}, {serNum}, {PIN}, {value}')
            return True
        elif all([devNum is not None, PINS]):
            [self.dll.FCWSetSwitch(cw, devNum, 0x10 + self.split_pin_for_set(PIN), value) for PIN, value in zip(PINS, values)]
            return True
        return False
    
    def get_pin_param(self, serNum, cw:int=0, PIN:str=None, PINS:list=[]) -> int | list | None:
        logger.info(f'get_pin_param() {serNum}, {PIN}')
        devNum, params =self.verify_serNum(serNum, take_params=True, cw=cw, update=True) # Update devices in 52 line
        logger.info(f'get_pin_param() {devNum}, {params}')
        if devNum is not None:
            if PIN:
                result = params.get(PIN)
                logger.info(f'get_pin_param() {devNum}, {serNum}, {result}')
                return result 
            elif PINS:
                result = [params.get(pin) for pin in PINS]
                logger.info(f'get_pin_param() {devNum}, {serNum}, {result}')
                return result 
    
    def set_multi_switch(self, serNum, contact, cw:int=0) -> bool:
        devNum = self.verify_serNum(serNum, update=True)
        if devNum is not None:
            value = 2 ** contact - 1
            self.dll.FCWSetMultiSwitch(cw, devNum, value)
            logger.info(f'set_multi_swirch() {devNum}, {serNum}, {value}')
            return True
        return False
    
    def get_multi_switch(self, serNum:int, cw:int=0, mask:int=0, value:int=0, seqNum:int=0) -> int | None:
        devNum = self.verify_serNum(serNum, update=True)
        if devNum is not None:
            # mask, and value is optional values
            result = self.dll.FCWGetMultiSwitch(cw, devNum, seqNum)
            # if use mask, values
            #result = self.dll.FCWGetMultiSwitch(self.cw, devNum, mask, value, seqNum)
            logger.info(f'get_multi_switch() {devNum}, {serNum}, {mask}, {value}, {result}')
            return result 
    
    def close(self, cw:int=0):
        self.dll.FWCCloseCleware(cw)


def test():
    try:
        # Add cw parametr 
        sync = Sync(cw=0)
        _device_for_selected = sync.update_all_devices()  # get all devices in dict
        sync.get_list_devices()  # get list device for combobox
        # first device get PIN1 and two PIN3, PIN4 for 0 device
        select0_device = _device_for_selected[0]
        serNum0_device = select0_device['serNum']
        sync.set_multi_switch(serNum=serNum0_device, contact=4)
        sync.get_multi_switch(serNum=serNum0_device)

        sync.get_pin_param(serNum=serNum0_device, PIN='PIN_1')
        sync.get_pin_param(serNum=serNum0_device, PINS=['PIN_3', 'PIN_4'])
        # second device set PIN2 and two PIN3, PIN4 for 0 device
        sync.set_pin_param(serNum=serNum0_device, PIN='PIN_2', value=1)
        sync.set_pin_param(serNum=serNum0_device, PINS=['PIN_3', 'PIN_4'], values=[1, 1])

        # third device set PIN2 and two PIN5, PIN6 for 1 device
        select1_device = _device_for_selected[1]
        serNum1_device = select1_device['serNum']
        sync.set_pin_param(serNum=select1_device, PIN='PIN_2', value=1)
        sync.set_pin_param(serNum=serNum1_device, PINS=['PIN_5', 'PIN_6'], values=[1, 1])
        # fourth device set all PINS 1 for 2 device
        select2_device = _device_for_selected[2]
        serNum2_device = select2_device['serNum']
        sync.set_multi_switch(serNum=serNum2_device, contact=8)
        sync.get_multi_switch(serNum=serNum2_device)
        sync.set_multi_switch(serNum=serNum2_device, contact=0)
        sync.get_multi_switch(serNum=serNum2_device)
        sync.set_multi_switch(serNum=serNum2_device, contact=8)
        sync.get_multi_switch(serNum=serNum2_device)
        # fifth device get all PINS for 1 device
        sync.set_multi_switch(serNum=serNum1_device, contact=1)
        sync.get_multi_switch(serNum=serNum1_device)
        sync.close()
    except Exception as ex:
        logger.error(ex)



if __name__ == '__main__':
    test()
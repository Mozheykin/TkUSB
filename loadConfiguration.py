from abc import abstractclassmethod
from errors import NotConfirationsOnFile
from pathlib import Path


class Configurations:
    def __init__(self, path_user:str, path_configs:str) -> None:
        self.path_user = path_user
        self.path_configs = path_configs
    
    @abstractclassmethod
    def load(self) -> None | dict:
        raise NotImplementedError

    @abstractclassmethod
    def save(self, objects:dict) -> None:
        raise NotImplementedError


class ConfigurationsJson(Configurations):
    def load(self) -> None | dict:
        import json
        with open(self.path) as file:
            data = json.load(file)
        return data


class ConfigurationsXml(Configurations):
    def load(self) -> None | dict:
        import xmltodict
        with open(self.path_configs) as file:
            data = xmltodict.parse(file.read())
        with open(self.path_user) as file:
            data_user = xmltodict.parse(file.read())
        return data, data_user
    
    def save(self, objects:dict) -> None:
        import xml.etree.cElementTree as ET
        TkUSB = ET.Element('TkUSB')
        for object_class, object_parametrs in objects.items():
            tree_object = ET.SubElement(TkUSB, object_class)
            for name, pr in object_parametrs.items():
                ET.SubElement(tree_object, name, name='activate').text = pr.get('activate')
        tree = ET.ElementTree(TkUSB)
        tree.write(self.path_user)



def load_configurations(path_user:str, path_configs:str) -> None | dict:
    init_class = path_user.split('.')[-1]
    if Path(path_user).is_file():
        match init_class:
            case 'json':
                config = ConfigurationsJson(path_user=path_user, path_configs=path_configs)
                if not config:
                    raise NotConfirationsOnFile
                return config.load()
            case 'xml':
                config = ConfigurationsXml(path_user=path_user, path_configs=path_configs)
                if not config:
                    raise NotConfirationsOnFile
                return config.load()
    else:
        raise NotConfirationsOnFile 
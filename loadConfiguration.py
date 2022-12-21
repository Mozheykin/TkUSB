from abc import abstractclassmethod
from errors import NotConfirationsOnFile
from pathlib import Path


class Configurations:
    def __init__(self, path_user:str, path_configs:str='') -> None:
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
        import xml.etree.ElementTree as ET
        #with open(self.path_configs) as file:
        #    data = xmltodict.parse(file.read())
        xml = ET.tostring(ET.parse(self.path_configs).getroot())
        data = xmltodict.parse(xml, attr_prefix="@", cdata_key="#text", dict_constructor=dict)
        try:
            with open(self.path_user) as file:
                data_user = xmltodict.parse(file.read())
        except Exception:
            data_user = {}
        return data, data_user
    
    def save(self, objects:dict) -> None:
        import xml.etree.cElementTree as ET
        TkUSB = ET.Element('TkUSB')
        for object_class, object_parametrs in objects.items():
            tree_object = ET.SubElement(TkUSB, object_class)
            for name, pr in object_parametrs.items():
                name_object = ET.SubElement(tree_object, name)
                ET.SubElement(name_object, 'activate').text = pr
        tree = ET.ElementTree(TkUSB)
        tree.write(self.path_user)


def get_init_class(path:str) -> Configurations:
    init_class = path.split('.')[-1]
    if Path(path).is_file():
        match init_class:
            case 'json':
                return ConfigurationsJson
            case 'xml':
                return ConfigurationsXml
    else:
        raise NotConfirationsOnFile 


def load_configurations(path_user:str, path_configs:str) -> None | dict:
    config = get_init_class(path=path_configs)(path_user=path_user, path_configs=path_configs)
    return config.load()


def save_configurations(path:str, path_user:str, objects:dict) -> None:
    config = get_init_class(path=path)(path_user=path_user)
    config.save(objects=objects)
from abc import abstractclassmethod
from errors import NotConfirationsOnFile
from pathlib import Path


class Configurations:
    def __init__(self, path:str) -> None:
        self.path = path
    
    @abstractclassmethod
    def load(self) -> None | dict:
        raise NotImplementedError


class ConfigurationsJson(Configurations):
    def __init__(self, path: str) -> None:
        super().__init__(path)
    
    def load(self) -> None | dict:
        import json
        with open(self.path) as file:
            data = json.load(file)
        return data


class ConfigurationsXml(Configurations):
    def __init__(self, path: str) -> None:
        super().__init__(path)
    
    def load(self) -> None | dict:
        import xmltodict
        with open(self.path) as file:
            data = xmltodict.parse(file.read())
        return data


def load_configurations(path:str) -> None | dict:
    init_class = path.split('.')[-1]
    if Path(path).is_file():
        match init_class:
            case 'json':
                config = ConfigurationsJson(path=path)
                if not config:
                    raise NotConfirationsOnFile
                return config.load()
            case 'xml':
                config = ConfigurationsXml(path=path)
                if not config:
                    raise NotConfirationsOnFile
                return config.load()
    else:
        raise NotConfirationsOnFile 
# scripts.python.read_language.Component
import bge
from collections import OrderedDict
from .config import *

class Component(bge.types.KX_PythonComponent):

    args = OrderedDict([])

    def start(self, args):
        # read .json
        with open(jsonfile_config_path, "r") as config_file:
            contents = json.loads(config_file.read())

        # strings
        self.texts = {}
        self.texts["pt_br"] = {"Language pt_BR", "Sair"}
        self.texts["en_us"] = {"Language en_US", "Exit"}

        # change texts
        self.object["Text"]             = list(self.texts[contents["user_language"]])[0]
        self.object.children[0]["Text"] = list(self.texts[contents["user_language"]])[1]
        
    def update(self):
        pass

# scripts.python.check_language.Component
import bge
from collections import OrderedDict
from .config import *

class Component(bge.types.KX_PythonComponent):

    args = OrderedDict([])

    def start(self, args):

        if os.path.isfile(jsonfile_config_path):
            bge.logic.startGame(rangefile_read_language_path)
            
        else:
            bge.logic.startGame(rangefile_selection_path)

    def update(self):
        pass

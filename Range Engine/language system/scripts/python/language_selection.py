# scripts.python.language_selection.Component
import bge
from collections import OrderedDict
from .config import *

class Component(bge.types.KX_PythonComponent):

    args = OrderedDict([])

    def start(self, args):
        # control variables
        self.ui_interaction = True

        # left mouse input
        self.left_mouse = bge.logic.mouse.inputs[bge.events.LEFTMOUSE]

        # mouse over sensor
        self.mo_sensor = self.object.sensors["mouse_over_sensor"]

        # user language
        self.user_language = self.object["language"]

    def update(self):
        # language selection
        if self.ui_interaction and self.mo_sensor.positive and self.left_mouse.activated:

            # hide mouse cursor
            bge.render.showMouse(False)

            # deactivate ui interaction
            self.ui_interaction = False

            # create the config file (if not exists)
            self.create_config()

            # load .range file
            bge.logic.startGame(rangefile_read_language_path)

    def create_config(self):
        # json contents
        json_contents = json.dumps(
            {
                "user_language" : self.user_language if self.user_language in available_languages else default_language
            },
            indent = 4
        )

        # create config if not exists
        if not os.path.isfile(jsonfile_config_path):
            with open(jsonfile_config_path, "w") as config:
                config.write(json_contents)

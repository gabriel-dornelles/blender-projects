# scripts.python.language_selection.Component
import bge
from collections import OrderedDict
from json import dumps
from os.path import isfile

class Component(bge.types.KX_PythonComponent):

    args = OrderedDict([])

    def start(self, args):

        # available languages
        self.languages = ["pt_BR", "en_US"]

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

            # deactivate ui interaction
            self.ui_interaction = False

            # hide mouse cursor
            bge.render.showMouse(False)

            # create the config file (if not exists)
            self.create_config()

            # exit
            bge.logic.endGame()

    def create_config(self):

        # paths
        filename   = "config"
        final_path = bge.logic.expandPath("//" + filename + ".json")

        # language
        default_language = "pt_BR"
        user_language    = self.user_language if self.user_language in self.languages else default_language

        # config file contents
        file_contents = dumps(
            {
                "user_language" : user_language
            },

            indent = 4
        )

        # create file if not exists
        if not isfile(final_path):
            with open(final_path, "w") as config_file:
                config_file.write(file_contents)

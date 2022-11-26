import json
import os
import os.path
from collections import OrderedDict

# available languages
available_languages = ["pt_br", "en_us"]

# default language
default_language = "pt_br"

# files extension
rangefile_extension = ".range"
jsonfile_extension = ".json"

# range files name
rangefile_start_name         = "start"         + rangefile_extension
rangefile_selection_name     = "selection"     + rangefile_extension
rangefile_read_language_name = "read_language" + rangefile_extension

# json file name
jsonfile_name = "config" + jsonfile_extension

# main folder path
main_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

# range files path
rangefile_start_path         = main_folder + "\\" + rangefile_start_name
rangefile_selection_path     = main_folder + "\\" + rangefile_selection_name
rangefile_read_language_path = main_folder + "\\" + rangefile_read_language_name

# json file path
jsonfile_config_path = main_folder + "\\" + jsonfile_name

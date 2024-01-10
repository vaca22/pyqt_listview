import os
import sys


def get_resource_path(relative_path):
    """ Return the path to the resource, whether running from source or bundled app """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # sys._MEIPASS is not set, so return the path as is
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
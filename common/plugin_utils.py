import os
import traceback
import inspect


def find_plugins(dir_to_search, plugin_type):
    dirname = os.path.split(dir_to_search)[1]
    py_files = [os.path.splitext(fname)[0]
                for fname in os.listdir(dir_to_search)
                if os.path.splitext(fname)[1] == '.py']
    plugins = []
    for py_file in py_files:
        if py_file in ['__init__']:
            continue

        try:
            __import__('%s.%s' % (dirname, py_file))
        except ImportError:
            traceback.print_exc()

        for sc in plugin_type.__subclasses__():
            if not inspect.isabstract(sc):
                plugins.append(sc)
    return plugins

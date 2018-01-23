import os
import inspect
from plugin_types.notifier import Notifier


def get_classes(module):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            yield obj


def find_notifier_modules():
    cur_dir = os.path.dirname(__file__)
    dirname = os.path.split(cur_dir)[1]
    py_files = [os.path.splitext(fname)[0] for fname in os.listdir(cur_dir)
            if os.path.splitext(fname)[1] == '.py']
    ret_val = []
    
    for py_file in py_files:
        if py_file in ['__init__']:
            continue

        module = __import__('%s.%s' % (dirname, py_file))
        #for class_obj in get_classes(getattr(module, py_file)):
        #    if not inspect.isabstract(class_obj) and issubclass(class_obj, Notifier):
        #        ret_val.append(class_obj)
        for sc in Notifier.__subclasses__():
            if not inspect.isabstract(sc):
                ret_val.append(sc)
    return ret_val


NOTIFIERS = find_notifier_modules()

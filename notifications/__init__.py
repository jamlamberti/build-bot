import os
from common.plugin_utils import find_plugins
from plugin_types.notifier import Notifier

NOTIFIERS = find_plugins(os.path.dirname(__file__), Notifier)

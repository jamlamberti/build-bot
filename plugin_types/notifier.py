import abc


class NotificationFailed(Exception):
    pass


class Notifier():
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        # TODO: set up logging
        pass

    @abc.abstractmethod
    def send_notification(self, msg):
        return

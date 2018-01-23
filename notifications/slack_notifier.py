import requests
import json
from common import config
from plugin_types.notifier import Notifier, NotificationFailed


class Slack(Notifier):
    def __init__(self):
        self.slack_config = config.Section('slack')

    def send_notification(self, msg):
        req = requests.post(
            self.slack_config.get('incoming-url'),
            data=json.dumps({"text": msg}))

        # XXX: log req.text?
        if req.status_code != 200:
            exp_msg = 'Got a response of %d when connecting to %s' % (
                req.status_code, self.slack_config.get('incoming-url'))
            raise NotificationFailed(exp_msg)

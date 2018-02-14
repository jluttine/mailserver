import logging.config

from salmon.routing import Router
from salmon.server import Relay, LMTPReceiver
from salmon import queue

from . import settings


import os
dir_path = os.path.dirname(os.path.realpath(__file__))
loggingConfig = os.path.join(dir_path, "logging.conf")
print(loggingConfig)
raise ValueError(loggingConfig)
logging.config.fileConfig(loggingConfig)

# the relay host to actually send the final message to
settings.relay = Relay(host=settings.relay_config['host'],
                       port=settings.relay_config['port'], debug=1)

# where to listen for incoming messages
settings.receiver = LMTPReceiver(settings.receiver_config['host'],
                                 settings.receiver_config['port'])

Router.defaults(**settings.router_defaults)
Router.load(settings.handlers)
Router.RELOAD = True
Router.UNDELIVERABLE_QUEUE = queue.Queue("run/undeliverable")

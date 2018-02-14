import logging.config

from salmon.routing import Router
from salmon.server import Relay

from . import settings


import os
dir_path = os.path.dirname(os.path.realpath(__file__))
loggingConfig = os.path.join(dir_path, "test_logging.conf")
logging.config.fileConfig(loggingConfig)

# the relay host to actually send the final message to (set debug=1 to see what
# the relay is saying to the log server).
settings.relay = Relay(host=settings.relay_config['host'],
                       port=settings.relay_config['port'], debug=0)


settings.receiver = None

Router.defaults(**settings.router_defaults)
Router.load(settings.handlers)
Router.RELOAD = True
Router.LOG_EXCEPTIONS = False

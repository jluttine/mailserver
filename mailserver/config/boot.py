import logging.config

from salmon.routing import Router
from salmon import queue

from . import settings


import os
dir_path = os.path.dirname(os.path.abspath(__file__))
loggingConfig = os.path.join(dir_path, "logging.conf")
logging.config.fileConfig(loggingConfig)

Router.defaults(**settings.router_defaults)
Router.load(settings.handlers)
Router.RELOAD = True
Router.UNDELIVERABLE_QUEUE = queue.Queue("run/undeliverable")

# This file contains python variables that configure Salmon for email processing.

import json

# You may add additional parameters such as `username' and `password' if your
# relay server requires authentication, `starttls' (boolean) or `ssl' (boolean)
# for secure connections.
#
# Add these configurations to a JSON file settings.json in the directory in
# which Salmon is run and set permissions properly so the configuration is a)
# out of version control and b) not accessible to other users of the computer.
relay_config = json.load(open("relay_config.json", "r"))

receiver_config = json.load(open("receiver_config.json", "r"))

handlers = ['mailserver.app.handlers.sample']

router_defaults = {'host': '.+'}

# the config/boot.py will turn these values into variables set in settings

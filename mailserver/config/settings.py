import json

from salmon.server import Relay, LMTPReceiver

# You may add additional parameters such as `username' and `password' if your
# relay server requires authentication, `starttls' (boolean) or `ssl' (boolean)
# for secure connections.
#
# Add these configurations to a JSON file in the directory in which Salmon is
# run and set permissions properly so the configuration is a) out of version
# control and b) not accessible to other users of the computer.

relay = Relay(**json.load(open("relay_config.json", "r")))

receiver = LMTPReceiver(**json.load(open("receiver_config.json", "r")))

handlers = ['mailserver.app.handlers.tuhlaajapojat']

router_defaults = {'host': '.+'}

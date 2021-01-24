# Personal Salmon mailserver

Relay and receiver configurations are read from `relay_config.json` and
`receiver_config.json` files from the current working directory. This allows one
to run tests etc from the root directory of this repository because there are
some dummy configuration files. However, in production, the working directory
should be something else, for instance, `/var/lib/salmon` and one should put
actual configuration files there so that other users don't have access to them.

To run a server locally:

```
SALMON_SETTINGS_MODULE=mailserver.config.settings salmon start --no-daemon --boot mailserver.config.boot
```

import logging
import requests
import json

from salmon.routing import route, stateless
from salmon.server import SMTPError

from mailserver.config.settings import relay


# Read the configuration JSON file which contains fields "host" and "url". The
# host name (...@host.com) defines which emails are accepted. The API URL is
# used to convert the address part (address@...) to a list of receiving email
# addresses and possibly a mail list prefix tag.
#
# This configuration is kept in the JSON file out of VCS so that this
# information isn't publicly available.
config = json.load(open("tuhlaajapojat_config.json", "r"))


@route("(address)@(host)", address=".+", host=config["host"])
@stateless
def START(message, address=None, host=None):

    # Get the email addresses and the subject prefix/tag from an API URL.
    resp = requests.get("{0}{1}".format(config["url"], address))
    data = json.loads(resp.text)

    emails = data["emails"]
    prefix = unicode(data["tag"])

    if emails is None:
        raise SMTPError(550, "Unknown address")

    subject = message["Subject"]

    # Add the prefix if not already in the subject field
    if not prefix.lower() in subject.lower():
        new_subject = u"{0} {1}".format(prefix, subject)
        del message["Subject"]
        message["Subject"] = new_subject

    if len(emails) > 0:
        relay.deliver(message, To=emails)

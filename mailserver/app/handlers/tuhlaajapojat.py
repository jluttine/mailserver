import logging
import requests
import json

from salmon.routing import route, stateless
from salmon.server import SMTPError
from salmon.mail import MailResponse

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
    prefix = data["tag"]

    if emails is None:
        raise SMTPError(550, "Unknown address")

    subject = message["Subject"]

    # Add the prefix if not already in the subject field
    if not prefix.lower() in subject.lower():
        new_subject = "{0} {1}".format(prefix, subject)
        del message["Subject"]
        message["Subject"] = new_subject

    if len(emails) > 0:
        if any(email is None for email in emails):
            # Send back to the sender
            emails = [message["From"]]
            message = MailResponse(
                To=message["From"],
                From="noreply@nodomain.com",
                Subject="FAILED TO SEND: {0}".format(subject),
                Body="""
                Failed to send the email.

                Some recipients don't have email addresses defined.

                The email wasn't delivered to anyone.

                Please contact the administrator for help.
                """
            )
        relay.deliver(message, To=emails)
    else:
        logging.debug("No receivers, not relaying the email")

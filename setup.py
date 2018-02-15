from setuptools import setup, find_packages
setup(
    name             = "mailserver",
    version          = "0.1",
    install_requires = ["salmon-mail", "requests"],
    packages         = find_packages(),
    package_data     = {
        'mailserver': ["config/*.conf"],
    },
)

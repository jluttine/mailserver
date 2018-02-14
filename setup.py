from setuptools import setup, find_packages
setup(
    install_requires = ["salmon-mail"],
    packages         = find_packages(),
    package_data     = {
        '': ["config/*.conf"],
    },
    name             = "mailserver",
    version          = "0.1",
)

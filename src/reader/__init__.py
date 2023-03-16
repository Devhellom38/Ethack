"""Real Python feed reader.

Import the `feed` module to work with the Real Python feed:

    >>> from Ethack import webattack
    >>> webattack.list()
    ['DDOS', 'Bot Creator', ...]

See https://github.com/hellom38/Ethack/ for more information.
"""
# Standard library imports
from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    # Third party imports
    import tomli as tomllib

author = "hellom38/dev.hellom38.hireable@gmail.com"
# Version of realpython-reader package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("reader", "config.toml"))
URL = _cfg["feed"]["url"]

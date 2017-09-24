import pkg_resources

from .signers import fetch_signers

__version__ = pkg_resources.require("signhash")[0].version
__author__ = 'SignHash'
__all__ = [
    'fetch_signers',
]

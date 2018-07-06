"""Bitcoin framework module.

Intended to create transactions with smart contracts in Bitcoin in an easy
way
"""
from .address import AddressPKHLengthError, AddressSHLengthError, \
    P2PKHAddress, P2SHAddress
from .encoding import b58decode, b58encode, bech32decode, bech32encode

__all__ = ["AddressPKHLengthError", "AddressSHLengthError", "P2PKHAddress",
           "P2SHAddress", "b58decode", "b58encode"]

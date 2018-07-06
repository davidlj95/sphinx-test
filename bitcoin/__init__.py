"""Bitcoin framework module.

Intended to create transactions with smart contracts in Bitcoin in an easy
way
"""
from .address import P2PKHAddress, AddressPKHLengthError

__all__ = ["P2PKHAddress", "AddressPKHLengthError"]

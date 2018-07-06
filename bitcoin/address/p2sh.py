"""Models P2SH_ Addresses.

.. _P2SH: https://en.bitcoin.it/wiki/Transaction#Pay-to-Script-Hash

A P2SH_ address is used by user to send bitcoins to a Bitcoin smart
contract

Most information was extracted from the `Bitcoin Wiki`__.

__ P2SH_
"""

# Constants
SH_LENGTH = 20
"""
    int: length of the script hashes stored in addresses
"""


# Errors
class AddressSHLengthError(ValueError):
    """Error raised when the redeem script hash has an incorrect length"""
    pass


# Classes
class P2SHAddress:
    """Models a legacy P2SH Address

    Attributes:
        _script_hash (bytes): public key hash of the address
    """
    __slots__ = ["_script_hash"]

    def __init__(self, script_hash: bytes) -> None:
        """Initializes a P2SH given its script hash.

        Modifies the attribute :py:attr:`_script_hash`

        Args:
            script_hash: script hash to set

        Raises:
            AssertionError: script_hash argument is not a bytes object
            AddressSHLengthError: script_hash argument has not the
                proper length of a script hash
        """
        self._script_hash = None
        self.script_hash = script_hash

    def do_things(self, obj: str) -> bytes:
        """Does some things.

        Args:
            obj: object of options

        Returns:
            things modified by :py:obj:`obj` as bytes
        """
        return bytes()

    @property
    def script_hash(self) -> bytes:
        """Returns the public key hash stored in the address.

        :getter: Returns the script hash as bytes object
        :setter: Sets the script hash, while verifying the length and
                 type
        """
        return self._script_hash

    @script_hash.setter
    def script_hash(self, public_key_hash: bytes) -> None:
        assert isinstance(public_key_hash, bytes), \
            "Script hash must be exactly %d bytes" % SH_LENGTH

        if len(public_key_hash) != SH_LENGTH:
            raise AddressSHLengthError

        self._script_hash = public_key_hash


# Methods
def from_hex(script_hash_hex: str) -> P2SHAddress:
    """Creates a P2SH address from script hash in hexadecimal.

    Converts the hexadecimal string into bytes and then uses those bytes to
    create a P2SH address.

    >>> 2+3
    5

    Args:
        script_hash_hex: string containing script hash in hexadecimal

    Returns:
        pay to script hash address
    """
    return P2SHAddress(bytes.fromhex(script_hash_hex))

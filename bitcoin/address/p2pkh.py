"""Models P2PKH_ Addresses.

.. _P2PKH: https://en.bitcoin.it/wiki/Transaction#Pay-to-PubkeyHash

A P2PKH_ address is used by user to send bitcoins to another user who controls
the private key behind the public key (whose hash appears in the address)

Most information was extracted from the `Bitcoin Wiki`__.

__ P2PKH_
"""

# Constants
PKH_LENGTH = 20
"""
    int: length of the public key hashes stored in addresses
"""


# Errors
class AddressPKHLengthError(ValueError):
    """Error raised when the public key hash has an incorrect length"""
    pass


# Classes
class P2PKHAddress:
    """Models a legacy P2PKH Address

    Attributes:
        _public_key_hash (bytes): public key hash of the address
    """
    __slots__ = ["_public_key_hash"]

    def __init__(self, public_key_hash: bytes) -> None:
        """Initializes a P2PKH given its public key hash.

        Modifies the attribute :py:attr:`_script_hash`

        Args:
            public_key_hash: public key hash to set

        Raises:
            AssertionError: public_key_hash argument is not a bytes object
            AddressPKHLengthError: public_key_hash argument has not the
                proper length of a public key hash
        """
        self._public_key_hash = None
        self.public_key_hash = public_key_hash

    def do_things(self, obj: str) -> bytes:
        """Does some things.

        Args:
            obj: object of options

        Returns:
            things modified by :py:obj:`obj` as bytes
        """
        return bytes()

    @property
    def public_key_hash(self) -> bytes:
        """Returns the public key hash stored in the address.

        :getter: Returns the public key hash as bytes object
        :setter: Sets the public key hash, while verifying the length and
                 type
        """
        return self._public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, public_key_hash: bytes) -> None:
        assert isinstance(public_key_hash, bytes), \
            "Public key hash must be exactly %d bytes" % PKH_LENGTH

        if len(public_key_hash) != PKH_LENGTH:
            raise AddressPKHLengthError

        self._public_key_hash = public_key_hash


# Methods
def from_hex(public_key_hash_hex: str) -> P2PKHAddress:
    """Creates a P2PKH address from public key hash in hexadecimal.

    Converts the hexadecimal string into bytes and then uses those bytes to
    create a P2PKH address.


    >>> 1+1
    2

    Args:
        public_key_hash_hex: string containing public key hash in hexadecimal

    Returns:
        pay to public key hash address
    """
    return P2PKHAddress(bytes.fromhex(public_key_hash_hex))

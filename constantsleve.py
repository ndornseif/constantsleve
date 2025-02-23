#!/usr/bin/env python
"""
nothingupmysleve
Generating nothing up my sleve numbers from the digits of pi.
TODO:

"""

import hashlib
from typing import Union

# File with a million digits of pi
# These are organized into 100_000 blocks of 10 digits each.
# We extract 32 bits per block, so the maximum available is 3200000 bits (400000 bytes, 390.625 kiB)
PI_DIGITS_FILE = "pi.txt"


def int_list_to_hex(int_list: list[int]) -> str:
    """Take a list of integers and format them as a list of hex representations.
    [2, 255] -> [0x2, 0xff]"""
    str_list = list()
    for integer in int_list:
        str_list.append(hex(integer))

    return str(str_list).replace("'", "")


class DataGenerator:
    def __init__(self) -> None:
        self.loaded_bytes = bytearray()
        self.used_bytes = 0

    def available_bytes(self) -> int:
        """Gets number of loaded bytes that have not been used to generate data."""
        return len(self.loaded_bytes) - self.used_bytes

    @classmethod
    def from_pi_file(cls, filepath: str) -> "DataGenerator":
        """Read in the text file containing digits of pi
        and load the contents as bytes.
        Each digit block is equivalent to a 32-bit integer
        and constructed from 10 decimal digits."""
        read_blocks = list()
        with open(filepath, "r", encoding="UTF-8") as file:
            while True:
                if line := file.readline():
                    # Specificaly exclude the block containing the leading '3.'
                    # Also exclude empty strings
                    read_blocks += [
                        word
                        for word in line.strip().split(" ")
                        if word and not "." in word
                    ]
                else:
                    break
        reformed_blocks = bytearray()
        for block in read_blocks:
            try:
                integer_form = int(block)
            except:
                raise ValueError(f"Unable to process read data {block} as integer.")
            # A blocks maximum value is 9_999_999_999
            # Since log2(9_999_999_999) = 33.21928095 we can extract 32 bits safely.
            # Truncate block to 32 bits and append as bytes.
            reformed_blocks += (integer_form & 0xFFFFFFFF).to_bytes(
                4, byteorder="little"
            )
        new_gen = cls()
        new_gen.loaded_bytes = reformed_blocks
        return new_gen

    def hash_blocks(self, chunk_size: int = 64) -> None:
        """Take the loaded bytes and split it into chunks of 'chunk_size',
        these chunks are hashed using blake2b."""
        hashes = bytearray()
        for i in range(0, len(self.loaded_bytes), chunk_size):
            chunk = self.loaded_bytes[i : i + chunk_size]
            hasher = hashlib.blake2b(digest_size=chunk_size)
            hasher.update(chunk)
            hashes += hasher.digest()[: len(chunk)]
        self.loaded_bytes = hashes

    def generate_ints(
        self, bytes_per_int: int = 8, number_of_ints: int = 1, as_hex: bool = False
    ) -> Union[list[int], str]:
        """Generates a list of integers of specified lenght based on the available data blocks.
        If as_hex is set return as string of hex representations"""
        total_bytes_required = bytes_per_int * number_of_ints
        if self.available_bytes() < total_bytes_required:
            raise ValueError(
                f"Not enought bytes available to generate the requested number of ints. Available: {self.available_bytes()}, Required: {total_bytes_required}"
            )
        return_ints = list()
        for i in range(
            self.used_bytes, self.used_bytes + total_bytes_required, bytes_per_int
        ):
            return_ints.append(int.from_bytes(self.loaded_bytes[i : i + bytes_per_int]))
        self.used_bytes += total_bytes_required
        if as_hex:
            return int_list_to_hex(return_ints)
        return return_ints


def main() -> int:
    d = DataGenerator.from_pi_file(PI_DIGITS_FILE)
    d.hash_blocks()
    print("Available bytes:", d.available_bytes())
    print("  8-bit:", d.generate_ints(number_of_ints=16, bytes_per_int=1, as_hex=True))
    print(" 16-bit:", d.generate_ints(number_of_ints=8, bytes_per_int=2, as_hex=True))
    print(" 32-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=4, as_hex=True))
    print(" 64-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=8, as_hex=True))
    print("128-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=16, as_hex=True))
    print("256-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=32, as_hex=True))
    print("Available bytes:", d.available_bytes())
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())

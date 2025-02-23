# constantsleve

Generating nothing-up-my-sleeve numbers from the digits of pi.

## Description
The decimal digits of pi are split into blocks of ten digits, and each of these is interpreted as an integer. These integers are truncated to 32 bits and then used as the data from which nothing-up-my-sleeve numbers are generated. Optionally, these integers can be hashed using Blake2.

## Usage example
`   
d = DataGenerator.from_pi_file(PI_DIGITS_FILE)
d.hash_blocks()
print("Available bytes:", d.available_bytes())
print("  8-bit:", d.generate_ints(number_of_ints=16, bytes_per_int=1, as_hex=True))
print(" 16-bit:", d.generate_ints(number_of_ints=8, bytes_per_int=2, as_hex=True))
print(" 32-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=4, as_hex=True))
print(" 64-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=8, as_hex=True))
print("128-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=16, as_hex=True))
print("256-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=32, as_hex=True))
`

## License
Published under GPL-3.0 license.
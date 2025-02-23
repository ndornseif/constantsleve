# constantsleve

Generating nothing-up-my-sleeve numbers from the digits of pi.

## Description
The decimal digits of pi are split into blocks of ten digits, and each of these is interpreted as an integer.    
These integers are truncated to 32 bits and then used as the data from which nothing-up-my-sleeve numbers are generated.
Optionally, these integers can be hashed using Blake2.

## Usage example
```   
d = DataGenerator.from_pi_file(PI_DIGITS_FILE)   
d.hash_blocks()    
print("Available bytes:", d.available_bytes())     
print("  8-bit:", d.generate_ints(number_of_ints=16, bytes_per_int=1, as_hex=True))    
print(" 16-bit:", d.generate_ints(number_of_ints=8, bytes_per_int=2, as_hex=True))   
print(" 32-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=4, as_hex=True))   
print(" 64-bit:", d.generate_ints(number_of_ints=4, bytes_per_int=8, as_hex=True))   
print("128-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=16, as_hex=True))   
print("256-bit:", d.generate_ints(number_of_ints=2, bytes_per_int=32, as_hex=True))   
```
Returns:
```
Available bytes: 400000
  8-bit: [0x6a, 0x6d, 0xa6, 0x89, 0x9a, 0x47, 0xcf, 0x1e, 0xc8, 0x3, 0x5d, 0xbe, 0x8d, 0x76, 0x44, 0xfa]
 16-bit: [0x3c58, 0xf1f9, 0x9ee8, 0xfe3a, 0x9f51, 0x9b13, 0x74be, 0x15e9]
 32-bit: [0xeaf84041, 0x979ee7e9, 0xb9c014f1, 0xc08a358e]
 64-bit: [0xc3a0ee2a36b14420, 0xb8e8f218967fb679, 0x7542cab95052a02e, 0x1a3ca3185981a979]
128-bit: [0x909cd13f4ee4e2e4d78d6fa413ea4d30, 0x4981fc39ab0af55d056377ce734a16d1]
256-bit: [0x63706eac98013a16d4906b17b79f408a06d70f2ebc202b7e59bcc77c66bf63af, 0xe8e946c50695a79e7ae329401e3604a37b81c9f3c5ec80f22dc26984318ab356]
```

## License
Published under GPL-3.0 license.
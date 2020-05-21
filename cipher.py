from caesar import caesar
from vigenere import vigenere
from onetimepad import one_time_pad

plaintext = input("Enter Plaintext: ")

# Caesar
caesar(plaintext)

# Vigenere
vigenere(plaintext)

# One Time Pad
one_time_pad(plaintext)

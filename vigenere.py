# Vigenere
from fun import fun

def vigenere(txt): 
    key = input("Enter keyword for vingenere cipher: ")
    while not key.isalpha():
        key = input("Please enter only keyword (no symbols): ")
    fun(txt, key)
    print("")

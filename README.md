# cipher
Functions for encrypting a text, using Caesar's cipher, the Vigenere Cipher, and one-time-pad methods.

Caesar's cipher takes an integer (positive or negative) and rotates each letter by the given number, 
wrapping around the alphabet (so that "a" comes after "z"). This encryption is weak.

The Vigenere Cipher encrypts a plaintext using a user-inputted keyword that rotates the plaintext. 
This encryption is stronger, but by no means indecipherable.

One-time-pad, under certain conditions, is indecipherable. A piece of text is used as the key to encrypt 
a plaintext (which is the purpose that "text.txt" serves). Most importantly, the text should be at least as 
long as the plaintext. Each letter in the text is used to rotate the letters of the plaintext, one by one. 
Note that only the alphabets in the .txt file will be used to encrypt the plaintext. A "key.txt" file is
created for this purpose.


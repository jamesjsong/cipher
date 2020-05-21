# Function used in Vigenere and One Time Pad
def fun(txt, key):

    key = key.upper()
    counter = 0
    for char in txt:
        a_num = ord(char)
        if char.isupper():
            new = (a_num - 65 + (int(ord(key[counter])) - 65)) % 26 + 65
            print(chr(new), end = '')
            counter += 1
            counter = counter % len(key)
        elif char.islower():
            new = (a_num - 97 + (int(ord(key[counter])) - 65)) % 26 + 97
            print(chr(new), end = '')
            counter += 1
            counter = counter % len(key)
        else:
            print(char, end = '')

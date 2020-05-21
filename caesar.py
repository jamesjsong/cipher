# Caesar's cipher #
def caesar(txt):
    while True:
        try:
            key = int(input("Enter Key for Caesar's cipher: "))
            break
        except ValueError:
            print("Invalid Key. Enter a number: ")
    
    print("Caesar's cipher: ", end ="")
          
    for char in txt:
        a_num = ord(char)
        if char.isupper():
            new = (a_num - 65 + key) % 26 + 65
            print(chr(new), end = '')
        elif char.islower():
            new = (a_num - 97 + key) % 26 + 97
            print(chr(new), end = '')
        else:
            print(char, end = '')
    print("")


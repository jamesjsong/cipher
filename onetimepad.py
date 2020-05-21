# One Time Pad
from fun import fun

def one_time_pad(txt):
    file_name = input("Enter name of file (.txt) for encryption: ")
    f = open(file_name, "r")

# Create new file with only alphabets. #
    key = open("key.txt", "r+")
    while True: 
        for line in f.read():
            if line == "":
                break
            for char in line:
                if char.isalpha():
                    key.write(char)
        break

    line = key.readline()

    fun(txt, line)

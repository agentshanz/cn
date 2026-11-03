def decryption(string, shift):
    cipher = ""

    for char in string:
        if char == "":
            cipher += char

        elif char.isupper():
            cipher += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():
            cipher += chr((ord(char) - shift - 97) % 26 + 97)

        elif char.isdigit():
            cipher += chr((ord(char) - shift - 48) % 10 + 48)

        else:
            cipher += chr((ord(char) - shift - 32) % 95 + 32)

    return cipher


string = input("Enter encrypted string : ")
shift = int(input("Enter shift number : "))

print("Encrypted text : ", string)
print("Decrypted : ", decryption(string, shift))

"""
Ahmad Shah Yawar
task 8
8. XOR encryption
Write an XOR_cipher function that takes 2 arguments: the string to be encrypted and the encryption key, which returns a string encrypted by applying the XOR (^) function on the characters of the string with the key. Write also the function XOR_uncipher, which, using the encrypted string and the key, restores the original string.
"""

import msvcrt


def encryptDecrypt(inpString):
    xorKey = 'T'

    length = len(inpString);

    for i in range(length):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:]);
        print(inpString[i], end="");

    return inpString;


if __name__ == '__main__':
    sampleString = "I do my Home Work";

    print("Encrypted String: ", end="");
    sampleString = encryptDecrypt(sampleString);
    print("\n");

    print("Decrypted String: ", end="");
    encryptDecrypt(sampleString);

msvcrt.getch()
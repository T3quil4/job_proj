#ENCRYPT

def encrypt(msg, key):
    encrypted = ""
    keylen = len(key)

    for i, char in enumerate(msg):

        if char == " ":
            mcode = 26
        else:
            mcode = ord(char) - ord('a')

        if key[i%keylen] == " ":
            kcode = 26
        else:
            kcode = ord(key[i%keylen]) - ord('a')

        coded = (mcode+kcode)%27

        if coded == 26:
            enc_char = " "
        else:
            enc_char = chr(coded+ord('a'))

        encrypted += enc_char

    return encrypted


msg = "helloworld"
key = "abcdefgijkl"

print(encrypt(msg, key))
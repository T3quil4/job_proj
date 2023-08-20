#DECRYPT

def decrypt(enmsg, key):
    msg = ""
    keylen = len(key)

    for i, char in enumerate(enmsg):

        if char == " ":
            ecode = 26
        else:
            ecode = ord(char) - ord('a')

        if key[i%keylen] == " ":
            kcode = 26
        else:
            kcode = ord(key[i%keylen]) - ord('a')

        dcode = (ecode-kcode)%27

        if dcode == 26:
            msgchar = " "
        else:
            msgchar = chr(dcode+ord('a'))

        msg += msgchar

    return msg

enmsg = "hfnosauzun"
key = "abcdefgijkl"

print(decrypt(enmsg, key))
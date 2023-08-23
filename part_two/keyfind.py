#KEYFIND


def wrdlist(path):
    with open(path, 'r') as file:
        wlist = [line.strip() for line in file]
    return wlist

def decrypt(enmsg, key):
    msg = ""
    keylen = len(key)

    for i, char in enumerate(enmsg):

        if i < keylen:
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

def keyfrag(msg, frag):
    result = ""

    for i, char in enumerate(frag):
        if char == " ":
            startcode = 26
        else:
            startcode = ord(char) - ord('a')
        
        if i < len(msg):
            if msg[i] == " ":
                other_code = 26
            else:
                other_code = ord(msg[i]) - ord('a')
            
            diff = (other_code - startcode) % 27
            if diff == 26:
                result += " "
            else:
                result += chr(diff + ord('a'))

    return result

def solver(enmsg1, enmsg2, matchlist, wordlist, newfrag1, newfrag2):

    keylist=[]
    flag=False

    for wrd in matchlist:

        ext=wrd+" "
        newfrag1 += ext

        result = keyfrag(enmsg1, newfrag1)
        fragment = decrypt(enmsg2, result)
        print("Key-1: ",result)
        print("Res-1: ",fragment)
        
        index = fragment.rfind(" ")
        if index != -1:
            frag = fragment[index + 1:]
        else:
            frag = fragment

        matchlist = []
        for word in wordlist:
            if word.startswith(frag):
                matchlist.append(word)
                continue

        if not matchlist:
            newfrag1 = str(newfrag1).replace(ext,"")


        for wrd in matchlist:

            ext=wrd+" "
            newfrag2 += ext

            result = keyfrag(enmsg2, newfrag2)
            fragment = decrypt(enmsg1, result)
            print("Key-2: ",result)
            print("Res-2: ",fragment)

            index = fragment.rfind(" ")
            if index != -1:
                frag = fragment[index + 1:]
            else:
                frag = fragment

            matchlist = []
            for word in wordlist:
                if word.startswith(frag):
                    matchlist.append(word)
                    continue

            if not matchlist:
                newfrag2 = str(newfrag2).replace(ext,"")


            if len(result)>=len(fragment):
                keylist.append(result)
            else:
                solver(enmsg1, enmsg2, matchlist, wordlist, newfrag1, newfrag2)

    return keylist



wordlist = wrdlist('part_two\words.txt')
emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
list = ["early"]
newfrag1=""
newfrag2=""


keys = solver(emsg1, emsg2, list, wordlist, newfrag1, newfrag2)
for key in keys:
    print(key)

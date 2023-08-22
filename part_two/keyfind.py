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

def keyfind(enmsg1, enmsg2, list):
    keylist=[]
    wordlist = wrdlist('part_two\words.txt')


    for wrd1 in list:

        result = keyfrag(enmsg1, wrd1)
        fragment = decrypt(enmsg2, result)
        print(fragment)

        matchlist = []
        for word in wordlist:
            if word.startswith(fragment):
                matchlist.append(word)
        print(matchlist)

        for wrd2 in matchlist:

            #fragfind
            result2 = keyfrag(enmsg2, wrd2)
            print(result2)
            fragment2 = decrypt(enmsg1, result2)
            print(fragment2)

            #fragcut
            index = fragment2.rfind(" ")
            if index != -1:
                frag = fragment2[index + 1:]
            else:
                frag = fragment2

            #fragtowords
            matchlist = []
            for word in wordlist:
                if word.startswith(frag):
                    matchlist.append(word)
                    continue

            print(matchlist)

            for wrd3 in matchlist:

                newfrag = wrd1+" "+wrd3+" "
                print(newfrag)

                result3 = keyfrag(enmsg1, newfrag)
                fragment3 = decrypt(enmsg2, result3)
                print(fragment3)
                
                #fragcut
                index = fragment3.rfind(" ")
                if index != -1:
                    frag = fragment3[index + 1:]
                else:
                    frag = fragment3
                #fragtowords
                matchlist = []
                for word in wordlist:
                    if word.startswith(frag):
                        matchlist.append(word)
                        continue
                    
                print(matchlist)

    return keylist



emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
list = ["early"]

keys = keyfind(emsg1, emsg2, list)

for key in keys:
    print(key)
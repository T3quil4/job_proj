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

def solver(enmsg1, enmsg2, matchlist, wordlist, newfrag1, newfrag2, ext1, ext2):

    keylist=[]

    for wrd in matchlist:

        ext=wrd+" "
        print("\next-1: ",ext)
        if wrd in ext1:
            continue
        else:
            ext1.append(wrd)
            newfrag1 += ext

            if len(newfrag1)>len(enmsg1):
                newfrag1=str(newfrag1).rstrip(" ")
                if len(newfrag1)>len(enmsg1):
                    newfrag1.replace(wrd,"")

            else:

                result = keyfrag(enmsg1, newfrag1)
                if len(result)>len(enmsg2):
                    result[:len(enmsg2)]
                fragment = decrypt(enmsg2, result)
                print("\nKey-1: ",result)
                print("Res-1: ",fragment)
                print("Wrd-1: ",wrd)
                
                index = fragment.rfind(" ")
                if index != -1:
                    frag = fragment[index + 1:]
                else:
                    frag = fragment

                print("Frag-1: ",frag)

                matchlist = []
                for word in wordlist:
                    if word.startswith(frag):
                        matchlist.append(word)
                        continue
                print("List-1: ",matchlist)

                if not matchlist:
                    newfrag1 = str(newfrag1).replace(ext,"")
                    print("cut-1: ",newfrag1)

                wrds = fragment.split()
                if all(rd in wordlist for rd in wrds):
                    keylist.append(result)


                for wrd in matchlist:

                    ext=wrd+" "
                    print("\next-2: ",ext)
                    if wrd in ext2:
                        continue
                    else:
                        ext2.append(wrd)
                        newfrag2 += ext

                        if len(newfrag2)>len(enmsg2):
                            newfrag2=str(newfrag2).rstrip(" ")
                            if len(newfrag2)>len(enmsg2):
                                newfrag2.replace(wrd,"")
                        else:

                            result = keyfrag(enmsg2, newfrag2)
                            if len(result)>len(enmsg1):
                                result[:len(enmsg1)]
                            fragment = decrypt(enmsg1, result)
                            print("\nKey-2: ",result)
                            print("Res-2: ",fragment)
                            print("Wrd-2: ",wrd)

                            index = fragment.rfind(" ")
                            if index != -1:
                                frag = fragment[index + 1:]
                            else:
                                frag = fragment

                            print("Frag-2: ",frag)

                            matchlist = []
                            for word in wordlist:
                                if word.startswith(frag):
                                    matchlist.append(word)
                                    continue
                            print("List-2: ",matchlist)
                            
                            if not matchlist:
                                newfrag2 = str(newfrag2).replace(ext,"")
                                print("cut-2: ",newfrag2)


                            wrds = fragment.split()
                            if all(rd in wordlist for rd in wrds):
                                keylist.append(result)

                            solver(enmsg1, enmsg2, matchlist, wordlist, newfrag1, newfrag2, ext1, ext2)

    return keylist



wordlist = wrdlist('part_two\words.txt') 
emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
list = ["early"]
newfrag1=""
newfrag2=""
ext1=[]
ext2=[]


keys = solver(emsg1, emsg2, list, wordlist, newfrag1, newfrag2, ext1, ext2)
for key in keys:
    print("\nLehetseges kulcs: ",key)

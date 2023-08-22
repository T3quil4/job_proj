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
            result = keyfrag(enmsg2, wrd2)
            print(result)
            fragment = decrypt(enmsg1, result)
            print(fragment)

            #fragcut
            index = fragment.rfind(" ")
            if index != -1:
                frag = fragment[index + 1:]
            else:
                frag = fragment

            #fragtowords
            matchlist = []
            for word in wordlist:
                if word.startswith(frag):
                    matchlist.append(word)
                    continue

            print(matchlist)

            for wrd in matchlist:
                
                ext=wrd+" "
                newfrag1 = wrd1+" "+ext
                print(newfrag1)

                result = keyfrag(enmsg1, newfrag1)
                fragment = decrypt(enmsg2, result)
                print(fragment)
                
                #fragcut
                index = fragment.rfind(" ")
                if index != -1:
                    frag = fragment[index + 1:]
                else:
                    frag = fragment
                #fragtowords
                matchlist = []
                for word in wordlist:
                    if word.startswith(frag):
                        matchlist.append(word)
                        continue

                if not matchlist:
                    newfrag1 = str(newfrag1).replace(ext,"")

                print(matchlist)

                for wrd in matchlist:

                    ext=wrd+" "
                    newfrag2 = wrd2+" "+ext
                    print(newfrag2)

                    result = keyfrag(enmsg2, newfrag2)
                    fragment = decrypt(enmsg1, result)
                    print(fragment)
                    
                    #fragcut
                    index = fragment.rfind(" ")
                    if index != -1:
                        frag = fragment[index + 1:]
                    else:
                        frag = fragment
                    #fragtowords
                    matchlist = []
                    for word in wordlist:
                        if word.startswith(frag):
                            matchlist.append(word)
                            continue

                    if not matchlist:
                        newfrag2 = str(newfrag2).replace(ext,"")

                    print(matchlist)
                    
                    for wrd in matchlist:

                        ext=wrd+" "
                        newfrag1 += ext
                        print(newfrag1)

                        result = keyfrag(enmsg1, newfrag1)
                        fragment = decrypt(enmsg2, result)
                        print(fragment)
                        
                        #fragcut
                        index = fragment.rfind(" ")
                        if index != -1:
                            frag = fragment[index + 1:]
                        else:
                            frag = fragment
                        #fragtowords
                        matchlist = []
                        for word in wordlist:
                            if word.startswith(frag):
                                matchlist.append(word)
                                continue

                        if not matchlist:
                            newfrag1 = str(newfrag1).replace(ext,"")

                        print(matchlist)
                        
                        for wrd in matchlist:

                            ext=wrd+" "
                            newfrag2 += ext
                            print(newfrag2)

                            result = keyfrag(enmsg2, newfrag2)
                            fragment = decrypt(enmsg1, result)
                            print(fragment)
                            
                            #fragcut
                            index = fragment.rfind(" ")
                            if index != -1:
                                frag = fragment[index + 1:]
                            else:
                                frag = fragment
                            #fragtowords
                            matchlist = []
                            for word in wordlist:
                                if word.startswith(frag):
                                    matchlist.append(word)
                                    continue

                            if not matchlist:
                                newfrag2 = str(newfrag2).replace(ext,"")

                            print(matchlist)
                            
                            for wrd in matchlist:

                                ext=wrd+" "
                                newfrag1 += ext
                                print(newfrag1)

                                result = keyfrag(enmsg1, newfrag1)
                                fragment = decrypt(enmsg2, result)
                                print(fragment)
                                
                                #fragcut
                                index = fragment.rfind(" ")
                                if index != -1:
                                    frag = fragment[index + 1:]
                                else:
                                    frag = fragment
                                #fragtowords
                                matchlist = []
                                for word in wordlist:
                                    if word.startswith(frag):
                                        matchlist.append(word)
                                        continue

                                if not matchlist:
                                    newfrag1 = str(newfrag1).replace(ext,"")

                                print(matchlist)

    return keylist



emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
list = ["early"]

keys = keyfind(emsg1, emsg2, list)

for key in keys:
    print(key)
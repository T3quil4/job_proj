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

def keyfind(enmsg1, enmsg2, start):
    keylist=[]
    wordlist = wrdlist('part_two\words.txt')

    result = keyfrag(enmsg1, start)
    fragment = decrypt(enmsg2, result)
    print(fragment)

    matchlist = []
    for word in wordlist:
        if fragment in word:
            matchlist.append(word)
    print(matchlist)


    for wrd1 in matchlist:

        #fragfind
        result2 = keyfrag(enmsg2, wrd1)
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
            if frag in word:
                matchlist.append(word)
                continue

        print(matchlist)

    return keylist



emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
word1 = "early"

keys = keyfind(emsg1, emsg2, word1)

for key in keys:
    print(key)
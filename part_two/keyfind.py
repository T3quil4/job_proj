#KEYFIND

def wrdlist(path):
    with open(path, 'r') as file:
        wlist = [line.strip() for line in file]
    return wlist

wordlist = wrdlist('part_two\words.txt')

def keyfind(enmsg1, enmsg2, start):
    keylist=[]

    

    return keylist

emsg1 = "cvtlsxoagjvimnhhezpnjnau"
emsg2 = "ebtobehq nkcbvfljyhbrp xquq"
word1 = "early"

keys = keyfind(emsg1, emsg2, word1)

for key in keys:
    print(key)
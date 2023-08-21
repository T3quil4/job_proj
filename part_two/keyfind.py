#KEYFIND

def wrdlist(path):
    with open(path, 'r') as file:
        wlist = [line.strip() for line in file]
    return wlist

def keyfind(enmsg1, enmsg2, start):
    keylist=[]
    wordlist = wrdlist('part_two\words.txt')

    result = ""
    for i, char in enumerate(start):
        if char == " ":
            startcode = 26
        else:
            startcode = ord(char) - ord('a')
        
        if i < len(enmsg1):
            if enmsg1[i] == " ":
                other_code = 26
            else:
                other_code = ord(enmsg1[i]) - ord('a')
            
            diff = (startcode - other_code) % 27
            if diff == 26:
                result += " "
            else:
                result += chr(diff + ord('a'))

            #karakterkód és keykód közti elcsúszás a key character kódja

    print(result)


        












    return keylist
        #early
emsg2 = "cvtlsxoagjvimnhhezpnjnau"
emsg1 = "ebtobehq nkcbvfljyhbrp xquq"
word1 = "early"

keys = keyfind(emsg1, emsg2, word1)

for key in keys:
    print(key)
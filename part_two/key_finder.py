#KEY_FINDER

def wrdlist(path):
    with open(path, 'r') as file:
        wlist = [line.strip() for line in file]
    return wlist

wordlist = wrdlist("words.txt")

for i in wordlist:
    print(i)
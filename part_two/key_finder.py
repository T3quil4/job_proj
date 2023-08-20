#KEY_FINDER

def wrdlist(path):
    with open(path, 'r') as file:
        wlist = [line.strip() for line in file]
    return wlist

wordlist = wrdlist('part_two\words.txt')

for word in wordlist:
    print(word)
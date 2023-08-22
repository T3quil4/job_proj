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
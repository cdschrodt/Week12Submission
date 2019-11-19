# WEEK12Submission
# Christian Schrodt
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(user_input): #WORKS
    print('OUTPUT', user_input)

def LoadFile(file): #WORKS
    data = open(file, 'r')
    newdata = data.readlines()
    data.close()
    datalist = []
    for i in newdata:
        newlist = i.split()
        for j in newlist:
            datalist.append(j)
    return datalist

def UpdateString(stringx, stringy, indexint): #WORKS
    modstring = ''
    for i in range(len(stringx)):
        if i == indexint:
            modstring += stringy
        else:
            modstring += stringx[i]
    print('OUTPUT', modstring)

def FindWordCount(userlist, userstring): #NEED TO CHECK
    numoccurences = 0
    for i in range(len(userlist)):
        if userstring == userlist[i]:
            numoccurences += 1
    return numoccurences

def ScoreFinder(playernames, playerscores, foundplayer): #WORKS
    foundplayer = foundplayer.lower()
    location = -1
    for j in range(len(playernames)):
        playernames[i] = playernames[i].lower()
    for i in range(len(playernames)):
        if foundplayer == playernames[i]:
            location = i
    if location >= 0:
        print('OUTPUT', playernames[location], 'got a score of', playerscores[location])
    else:
        print('OUTPUT player not found')

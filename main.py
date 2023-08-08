words = [
    "second",
    "hundred",
    "twenty",
    "thirty",
    "fourths",
    "fifteen",
    "eighth",
    "less",
    "five"
    ]

wordTableRaw = """f|w|b|c|h|a|l|f|d
i|j|y|k|h|d|e|i|h
f|o|u|r|t|h|s|v|t
t|g|b|b|h|u|s|e|h
e|s|e|c|o|n|d|i|i
e|r|l|y|u|d|g|g|r
n|l|o|y|k|r|y|h|t
v|e|w|t|w|e|n|t|y
m|j|e|a|c|d|u|h|r"""

width = 0
height = 0

def getChar(x, y, wordTable):
    if x < width and x >= 0 and y < height and y >= 0:
        return wordTable[y][x]
    else:
        return "-"

def buildBlank():
    ret = []
    for x in range(width):
        ret.append([])
        for y in range(height):
            ret[x].append[" "]
    return ret

def parseWordTable(wordtable):
    global width
    global height
    rows = wordTableRaw.split("\n")
    out = []
    for i in range(len(rows)):
        out.append(rows[i].split("|"))
    height = len(out)
    width = len(out[0])
    return out

def tryWordAtLoc(word, wordTable, x, y, velx, vely):
    #print("Trying @" + str(x) + ", " + str(y) + " with dir " + str(velx) + ", " + str(vely))
    for i in range(len(word)):
        if not word[i] == getChar(x + velx * i, y + vely * i, wordTable):
            #print(str(i) + "/" + str(len(word)))
            return False
    #print(str(i) + "/" + str(len(word)) + " first " + wordTable[y][x])
    return True

def tryWordAtLocPluse(word, wordTable, x, y):
    if tryWordAtLoc(word, wordTable, x, y, 0, -1):
        return "up"
    elif tryWordAtLoc(word, wordTable, x, y, 0, 1):
        return "down"
    elif tryWordAtLoc(word, wordTable, x, y, -1, 0):
        return "left"
    elif tryWordAtLoc(word, wordTable, x, y, 1, 0):
        return "right"
    else:
        return "fail"

def tryWordFull(word, wordTable):
    for y in range(len(wordTable)):
        for x in range(len(wordTable[y])):
            v = tryWordAtLocPluse(word, wordTable, x, y)
            if not v == "fail":
                return {"word": word, "x": x, "y": y, "dir": v}
    print("Could Not Find Word " + word)

def findAllWords(words, wordTable):
    for i in range(len(words)):
        print(tryWordFull(words[i], wordTable))

wordt = parseWordTable(wordTableRaw)
findAllWords(words, wordt)

findX = 0
findY = 0
foundLog = [[0,0],[0,0]]
while (findX <= 17) and (found == False):
    while (findY <= 23) and (found == False):
        if tileMap[findX][findY] == "(":
            foundLog[0] = [findX, findY]
            while (findY <= 23) and (found == False):
                findY+= 1
                if tileMap[findX][findY] == ")":
                    foundLog[1] = [findX, findY]
                    found = True
                    findY += 1
                    continue
        if found == True:
            continue
        findY += 1
    if found == True:
        continue
    findX += 1


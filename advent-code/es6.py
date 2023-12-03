def isNum(char):
        if(ord(char) >= ord('0') and ord(char) <= ord('9')):
            return True
        else:
            return False
def getNum(string, j):
    while((j > 0 and isNum(string[j-1]))):
        j = j - 1
        
    num = ''
    while((isNum(string[j]))):
        num += string[j]
        j = j + 1
    return int(num)

class es6:
    strings = []
    with open("es5", "r") as f:
        for line in f:
            strings.append(line)

    tot = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            gear = []
            lastNum = 0
            if(strings[i][j] == '*'):

                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i-1][j-1])):
                    num = getNum(strings[i-1], j-1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i-1][j])):
                    num = getNum(strings[i-1], j)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i-1][j+1])):
                    num = getNum(strings[i-1], j+1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i][j-1])):
                    num = getNum(strings[i], j-1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i][j+1])):
                    num = getNum(strings[i], j+1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i+1][j-1])):
                    num = getNum(strings[i+1], j-1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i+1][j])):
                    num = getNum(strings[i+1], j)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num
                    
                if(i > 0 and j<len(strings[i]) -1 and isNum(strings[i+1][j+1])):
                    num = getNum(strings[i+1], j+1)
                    if(lastNum != num):
                        gear.append(num)
                        lastNum = num

                if(len(gear) == 2):
                    tot = tot + (gear[0]*gear[1])
                    gear = []       
                
    print(tot)
                
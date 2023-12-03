import numpy as np

class Es1:
    strings = []
    with open("prova", "r") as f:
        for line in f:
            strings.append(line)
    #print(strings)
    sum1 = []
    sum2 = []
    for string in strings:
        for i in range(len(string)):
            if (ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9')):
                num1 = string[i]
                sum = int(num1) * 10
                sum1.append(sum)
                break

    for string in strings:
        for j in range(len(string)-1, -1, -1):
                if (ord(string[j]) >= ord('0') and ord(string[j]) <= ord('9')):
                        num2 = string[j]
                        sum2.append(num2)
                        break
    tot = 0
    print(len(sum1), len(sum2), len(strings))
    for i in range(len(strings)):
         tot = tot + int(sum1[i]) + int(sum2[i])

    print(tot)
               



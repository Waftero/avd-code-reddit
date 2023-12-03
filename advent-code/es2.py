
class es2:
    strings = []
    with open("es1", "r") as f:
        for line in f:
            strings.append(line)
    #print(len(strings))
    
    # three = ['one', 'two', 'six']
    # four = ['four', 'five', 'nine', 'zero']
    # five = ['three', 'seven', 'eight']
    
    nums = []
    numz = []
    for string in strings:
        for i in range(len(string)):
            if (ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9')):
                num1 = int(string[i]) * 10
                nums.append(num1)
                break
            if(i < (len(string) - 3) and string[i] == 'o' and string[i+1] == 'n' and string[i+2] == 'e'):
                num1 = 10
                nums.append(num1)
                break
            if(i < (len(string) - 3) and string[i] == 't' and string[i+1] == 'w' and string[i+2] == 'o'):
                num1 = 20
                nums.append(num1)
                break
            if(i < (len(string) - 3) and string[i] == 's' and string[i+1] == 'i' and string[i+2] == 'x'):
                num1 = 60
                nums.append(num1)
                break
            if(i < (len(string) - 4) and string[i] == 'f' and string[i+1] == 'o' and string[i+2] == 'u' and string[i+3] == 'r'):
                num1 = 40
                nums.append(num1)
                break
            if(i < (len(string) - 4) and string[i] == 'f' and string[i+1] == 'i' and string[i+2] == 'v' and string[i+3] == 'e'):
                num1 = 50
                nums.append(num1)
                break
            if(i < (len(string) - 4) and string[i] == 'n' and string[i+1] == 'i' and string[i+2] == 'n' and string[i+3] == 'e'):
                num1 = 90
                nums.append(num1)
                break
            if(i < (len(string) - 5) and string[i] == 't' and string[i+1] == 'h' and string[i+2] == 'r' and string[i+3] == 'e' and string[i+4] == 'e'):
                num1 = 30
                nums.append(num1)
                break
            if(i < (len(string) - 5) and string[i] == 's' and string[i+1] == 'e' and string[i+2] == 'v' and string[i+3] == 'e' and string[i+4] == 'n'):
                num1 = 70
                nums.append(num1)
                break
            if(i < (len(string) - 5) and string[i] == 'e' and string[i+1] == 'i' and string[i+2] == 'g' and string[i+3] == 'h' and string[i+4] == 't'):
                num1 = 80
                nums.append(num1)
                break
    
    for string in strings:
            for i in range((len(string)-1), -1, -1):
                #print(string[i])
                if (ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9')):
                    num2 = int(string[i])
                    numz.append(num2)
                    break
                if(string[i] == 'e' and string[i-1] == 'n' and string[i-2] == 'o'):
                    num2 = 1
                    numz.append(num2)
                    break
                if(string[i] == 'o' and string[i-1] == 'w' and string[i-2] == 't'):
                    num2 = 2
                    numz.append(num2)
                    break
                if(string[i] == 'x' and string[i-1] == 'i' and string[i-2] == 's'):
                    num2 = 6
                    numz.append(num2)
                    break
                if(string[i] == 'r' and string[i-1] == 'u' and string[i-2] == 'o' and string[i-3] == 'f'):
                    num2 = 4
                    numz.append(num2)
                    break
                if(string[i] == 'e' and string[i-1] == 'v' and string[i-2] == 'i' and string[i-3] == 'f'):
                    num2 = 5
                    numz.append(num2)
                    break
                if(string[i] == 'e' and string[i-1] == 'n' and string[i-2] == 'i' and string[i-3] == 'n'):
                    num2 = 9
                    numz.append(num2)
                    break
                if(string[i] == 'e' and string[i-1] == 'e' and string[i-2] == 'r' and string[i-3] == 'h' and string[i-4] == 't'):
                    num2 = 3
                    numz.append(num2)
                    break
                if(string[i] == 'n' and string[i-1] == 'e' and string[i-2] == 'v' and string[i-3] == 'e' and string[i-4] == 's'):
                    num2 = 7
                    numz.append(num2)
                    break
                if(string[i] == 't' and string[i-1] == 'h' and string[i-2] == 'g' and string[i-3] == 'i' and string[i-4] == 'e'):
                    num2 = 8
                    numz.append(num2)
                    break
    tot = 0
    for i in range(len(strings)):
         tot = tot + int(nums[i]) + int(numz[i])

    print(tot)
               
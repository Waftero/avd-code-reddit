
class es7:
    c = []
    with open("es7", "r") as f:
        for line in f:
            l = line[8:]
            winning, numbers = l.split(' | ')
            # f'W: {winning.split()}'
            # f'N: {numbers.split()}'
            count = 0
            for win in winning.split():
                for num in numbers.split(): 
                    if(win == num and count == 0):
                        count = 1
                    if(win == num and count != 0):
                        count = count*2
            c.append(count/2)
    tot = 0
    for i in c:
        tot += i
    print(tot)

        
    


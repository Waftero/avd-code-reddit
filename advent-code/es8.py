import numpy as np
class es8:
    cards = []
    tot = []
    with open("es7", "r") as f:
        for line in f:
            l = line[8:]
            winning, numbers = l.split(' | ')
            # f'W: {winning.split()}'
            # f'N: {numbers.split()}'
            count = 0
            for win in winning.split():
                for num in numbers.split(): 
                    if(win == num):
                        count += 1
            cards.append(count)
    
    tot = np.ones(197)
    #print(cards)
    for i in range(len(tot)):
        for j in range(cards[i]):
            tot[i+j+1] = tot[i+j+1] + tot[i]
    sum = 0
    for i in range(len(tot)):
        sum += tot[i]
    print(sum)

            

    
    
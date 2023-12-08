def get_dist(time, start):
    dist = (time - start) * start
    return dist

class es12:
    tab = []
    with open("es11", "r") as f:
        for line in f:
            _, table = line.split(':')
            table = table.split()
            tab.append(table)
    
    old_time = tab[0]
    old_dist = tab[1]
    time = ''
    dist = ''
    for i in old_time:
        time += i
    for i in old_dist:
        dist += i
    time = int(time)
    dist = int(dist)
    
    loss = 0
    for j in range(time):
        if (get_dist(int(time), j) <= int(dist)):
            loss += 1
        else:
            break
    
    win = time + 1 - loss * 2
    print(win)
        
    
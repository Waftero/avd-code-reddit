def get_dist(time, start):
    dist = (time - start) * start
    return dist

class es11:
    tab = []
    with open("es11", "r") as f:
        for line in f:
            _, table = line.split(':')
            table = table.split()
            tab.append(table)
    
    time = tab[0]
    dist = tab[1]
    
    losses = []
    for i in range(len(time)):
        loss = 0
        for j in range(int(time[i])):
            if (get_dist(int(time[i]), j) <= int(dist[i])):
                loss += 1
            else:
                losses.append(loss)
                break
    wins = []
    for i in range(len(time)):
        win = int(time[i]) + 1 - losses[i] * 2
        wins.append(win)
    tot = 1
    for i in wins:
        tot = tot * i
    print(tot)
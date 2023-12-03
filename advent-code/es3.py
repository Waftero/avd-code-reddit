
class es3:
    ids = []
    games = []
    with open("es3", "r") as f:
        for line in f:
            gameId, cubes = line.split(":")
            _, id = gameId.split(" ")
            ids.append(id)
            games.append(cubes)
    tot = 0
    for i in range(len(games)):
        for j in range(len(games[i])):
            if(ord(games[i][j]) >= ord('0') and ord(games[i][j]) <= ord('9') and games[i][j+1] != ' '):
                num = int(games[i][j]) * 10 + int(games[i][j+1])
                if ((games[i][j+3] == 'r' and num > 12) or (games[i][j+3] == 'g' and num > 13) or (games[i][j+3] == 'b' and num > 14)):
                    tot = tot+int(ids[i])
                    break
    sum = 0
    for i in ids:
        sum = sum + int(i)
    
    print(sum-tot)
        

          
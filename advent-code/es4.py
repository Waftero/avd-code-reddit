
class es4:
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
        r = 0
        g = 0
        b = 0
        for j in range(len(games[i])):
            if(ord(games[i][j]) >= ord('0') and ord(games[i][j]) <= ord('9') and games[i][j+1] == ' '):
                num = int(games[i][j])
                if(games[i][j+2] == 'r' and num > r):
                    r = num
                if(games[i][j+2] == 'g' and num > g):
                    g = num
                if(games[i][j+2] == 'b' and num > b):
                    b = num
            if(ord(games[i][j]) >= ord('0') and ord(games[i][j]) <= ord('9') and games[i][j+1] != ' '):
                num = int(games[i][j]) * 10 + int(games[i][j+1])
                if(games[i][j+3] == 'r' and num > r):
                    r = num
                if(games[i][j+3] == 'g' and num > g):
                    g = num
                if(games[i][j+3] == 'b' and num > b):
                    b = num
        tot = tot + r*g*b
    print(tot)
        
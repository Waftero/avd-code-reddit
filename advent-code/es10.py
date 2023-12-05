def val(map, i, seed):
    while(map[i+1] != []):
        if(int(seed) >= int(map[i+1][1]) and int(seed) < int(map[i+1][1]) + int(map[i+1][2])):
            tmp = int(seed) - int(map[i+1][1])
            s = int(map[i+1][0]) + int(tmp)
            break
        else:
            s = int(seed)
        i = i+1
    return s
    
def val_loc(map, i, seed):
    while(i+1 < len(map)):
        if(int(seed) >= int(map[i+1][1]) and int(seed) < int(map[i+1][1]) + int(map[i+1][2])):
            tmp = int(seed) - int(map[i+1][1])
            s = int(map[i+1][0]) + int(tmp)
            break
        else:
            s = int(seed)
        i = i+1
    return s
def getMin(map, seed):
    for i in range(len(map)):
        if(map[i] == ['seed-to-soil', 'map:']):
            soil = val(map, i, seed)
        if(map[i] == ['soil-to-fertilizer', 'map:']):
            fertilizer = val(map, i, soil)
        if(map[i] == ['fertilizer-to-water', 'map:']):
            water= val(map, i, fertilizer)
        if(map[i] == ['water-to-light', 'map:']):
            light=val(map, i, water)
        if(map[i] == ['light-to-temperature', 'map:']):
            temperature=val(map, i, light)
        if(map[i] == ['temperature-to-humidity', 'map:']):
            humidity=val(map, i, temperature)
        if(map[i] == ['humidity-to-location', 'map:']):    
            location=val_loc(map, i, humidity)
    return location

class es10:
    map = []
    with open("prova", "r") as f:
        for line in f:
            table = line.split()
            map.append(table)

    seed = map[0][1::2]
    occ = map[0][2::2]
    
    for j in range(len(seed)):
        for i in range(int(seed[j]), int(seed[j]) + int(occ[j])):
            print(i , getMin(map, i))
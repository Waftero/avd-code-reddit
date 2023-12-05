import numpy as np

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
class es9:
    map = []
    with open("es9", "r") as f:
        for line in f:
            table = line.split()
            map.append(table)
    
    seed = map[0][1:]
    soil = []
    fertilizer = []
    water = []
    light = []
    temperature = []
    humidity = []
    location = []
    for i in range(len(map)):
        if(map[i] == ['seed-to-soil', 'map:']):
            for j in range(len(seed)):
                soil.append(val(map, i, seed[j]))
        if(map[i] == ['soil-to-fertilizer', 'map:']):
            for j in range(len(seed)):
                fertilizer.append(val(map, i, soil[j]))
        if(map[i] == ['fertilizer-to-water', 'map:']):
            for j in range(len(seed)):
                water.append(val(map, i, fertilizer[j]))
        if(map[i] == ['water-to-light', 'map:']):
            for j in range(len(seed)):
                light.append(val(map, i, water[j]))
        if(map[i] == ['light-to-temperature', 'map:']):
            for j in range(len(seed)):
                temperature.append(val(map, i, light[j]))
        if(map[i] == ['temperature-to-humidity', 'map:']):
            for j in range(len(seed)):
                humidity.append(val(map, i, temperature[j]))
        if(map[i] == ['humidity-to-location', 'map:']):    
                for j in range(len(seed)):
                    location.append(val_loc(map, i, humidity[j]))
    
    min = location[0]
    for loc in location:
        if(min > loc):
            min = loc
    print(min)
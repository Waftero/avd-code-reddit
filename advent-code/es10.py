def val(map, seed):
    i = 0
    while(i+1 < len(map)):
        if(int(seed) >= int(map[i+1][0]) and int(seed) < int(map[i+1][0]) + int(map[i+1][2])):
            tmp = int(seed) - int(map[i+1][0])
            s = int(map[i+1][1]) + int(tmp)
            break
        else:
            s = int(seed)
        i = i+1
    return s
    
def val_loc(map, seed):
    i = 0
    while(i+1 < len(map)):
        if(int(seed) >= int(map[i+1][0]) and int(seed) < int(map[i+1][0]) + int(map[i+1][2])):
            tmp = int(seed) - int(map[i+1][0])
            s = int(map[i+1][1]) + int(tmp)
            break
        else:
            s = int(seed)
        i = i+1
    return s

def getMin(map, location):
    map_soil, map_fertilizer, map_water, map_light, map_temperature, map_humidity, map_location = getMap(map)
    humidity = val(map_location, location)
    temperature = val(map_humidity, humidity)
    light= val(map_temperature, temperature)
    water=val(map_light, light)
    fertilizer=val(map_water, water)
    soil=val(map_fertilizer, fertilizer)
    seed=val_loc(map_soil, soil)
    return seed

def getMap(map):
    for i in range(len(map)):
        if(map[i] == ['seed-to-soil', 'map:']):
            map_soil = []
            while(map[i] != []):
                map_soil.append(map[i])
                i += 1
        if(map[i] == ['soil-to-fertilizer', 'map:']):
            map_fertilizer = []
            while(map[i] != []):
                map_fertilizer.append(map[i])
                i += 1
        if(map[i] == ['fertilizer-to-water', 'map:']):
            map_water = []
            while(map[i] != []):
                map_water.append(map[i])
                i += 1
        if(map[i] == ['water-to-light', 'map:']):
            map_light = []
            while(map[i] != []):
                map_light.append(map[i])
                i += 1
        if(map[i] == ['light-to-temperature', 'map:']):
            map_temperature = []
            while(map[i] != []):
                map_temperature.append(map[i])
                i += 1
        if(map[i] == ['temperature-to-humidity', 'map:']):
            map_humidity = []
            while(map[i] != []):
                map_humidity.append(map[i])
                i += 1
        if(map[i] == ['humidity-to-location', 'map:']):    
            map_location = []
            while(i < len(map)):
                map_location.append(map[i])
                i += 1
    return map_soil, map_fertilizer, map_water, map_light, map_temperature, map_humidity, map_location

class es10:
    map = []
    with open("es9", "r") as f:
        for line in f:
            table = line.split()
            map.append(table)

    seed = map[0][1::2]
    occ = map[0][2::2]
    found = False
    i = 0
    while(found != True):
        int_seed = getMin(map,i)
        if(i % 1000000 == 0):
            print('.')
        for j in range(len(seed)):
            if(int_seed >= int(seed[j]) and int_seed < int(seed[j]) + int(occ[j])):
                found = True
                print(int_seed, i)
                break
        i +=1
    
        



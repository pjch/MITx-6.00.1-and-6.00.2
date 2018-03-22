def getMax(cows, wl): #get the heaviest cow under available weight
    current_max = ''
    for name in cows:
        if cows[name] <= wl:
            if current_max == '' or cows[name] > cows[current_max]:
                current_max = name
    return current_max
    
def getShip(cows, wl): #get the ship for one round
    ship = []
    while True:
        maxaval = getMax(cows, wl)
        if maxaval != '':
            ship.append(maxaval)
            wl -= cows[maxaval]
            del cows[maxaval]    
        else:
            break
    return ship
        
def greedy_cow_transport(cows, wl): #get total trips
    result = []
    while cows:
        ship = getShip(cows, wl)
        result.append(ship)
    return result

"Astronomy Board Game"

def getPlanetToDestroy(planets):

    if len(planets) == 1 or len(planets) == 2:
        return 1
        
    odd = 0
    even = 0

    for i in range(len(planets)):
        if i % 2 == 0:
            even += planets[i]
        else:
            odd += planets[i]
    

    prefixEven = 0
    prefixOdd = 0

    for i in range(len(planets)):
        if i % 2 == 0:
            even -= planets[i]
        else:
            odd -= planets[i]
        
        # even to the left of index remain even while even to the right of index become new odd
        if prefixEven + odd == prefixOdd + even:
            return i + 1

        if i % 2 == 0:
            prefixEven += planets[i]
        else:
            prefixOdd += planets[i]
    
    return -1


planets = [2, 5, 6, 7, 8, 4]
print(getPlanetToDestroy(planets))
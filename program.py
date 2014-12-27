from random import randint

def optimalFind(list):
    tmin = list[0]
    tmax = list[0]
    if len(list)%2 != 0:
        list.append(list[0])
    for i,j in zip(list[0::2], list[1::2]):
        if i < j:
            tmin = min(tmin, i)
            tmax = max(tmax, j)
        else:
            tmin = min(tmin, j)
            tmax = max(tmax, i)
    return (tmin, tmax)


elements = 1000000
list = [randint(-1000,10000) for i in range(elements)]
result = optimalFind(list)
print("Min: ",result[0],  "Max: ", result[1])

from random import randint

def optimalFind(list):
    min = list[0]
    max = list[0]
    if len(list)%2 == 0:
        list.append(min)
    range = len(list)
    i = 1
    while i < range:
        if list[i] < list[i+1]:
            if list[i] < min:
                min = list[i]
            if list[i+1] > max:
                max = list[i+1]
        else:
            if list[i+1] < min:
                min = list[i+1]
            if list[i] > max:
                max = list[i]
        i += 2

    return (min, max)


list = [randint(1,10000) for i in range(1000000)]
result = optimalFind(list)
print("Min: ",result[0],  "Max: ", result[1])
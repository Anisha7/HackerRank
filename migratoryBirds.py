def migratoryBirds(arr):
    if len(arr) == 0:
        return None

    d = dict()
    for birdId in arr:
        if birdId in d:
            d[birdId] += 1
        else:
            d[birdId] = 1
    
    maxId = arr[0]
    for key in d.keys():
        if d[key] > d[maxId]:
            maxId = key
    return maxId

print(migratoryBirds([1, 4, 4, 4, 5, 3]))
def migratoryBirds(arr):
    if len(arr) == 0:
        return None

    arr.sort()
    
    currCount = 0
    curr = arr[0]
    
    maxCount = 0
    maxId = curr
    for item in arr:
        if item == curr:
            currCount += 1
        
        if item != curr:
            if currCount > maxCount:
                maxCount = currCount
                maxId = curr
            elif currCount == maxCount:
                maxId = min(maxId, curr)
            currCount = 1
            
        curr = item
    
    if (maxCount > currCount):
        return maxId
    if (maxCount == currCount):
        return min(maxId, curr)
    return curr

print(migratoryBirds([1, 4, 4, 4, 5, 3])) # 4

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])) #3

# def migratoryBirds(arr):
#     if len(arr) == 0:
#         return None

#     d = dict()
#     for birdId in arr:
#         if birdId in d:
#             d[birdId] += 1
#         else:
#             d[birdId] = 1
    
#     maxIds = [arr[0]]
#     for key in d.keys():
#         if d[key] > d[maxIds[0]]:
#             maxIds = [key]
#     return min(maxIds)
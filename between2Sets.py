# Complete the getTotalX function below.
#
def getTotalX(a, b):
    minElem = min(b)
    potentialFactors = []
    
    item = max(a)
    temp = item
    # find potentials
    while temp <= minElem:
        found = True
        # if a multiple for every elem
        for elem in a:
            if temp % elem != 0:
                found = False
        if found: 
            potentialFactors.append(temp)

        temp += item # going through all multiples of temp

    # get potentialFactors that are factors for all elems in b
    count = 0
    for factor in potentialFactors:
        found = True
        for check in b:
            if check % factor != 0:
                found = False
        if found:
            count += 1
    return count


a = [3, 4]
b = [24, 48]
print(getTotalX(a, b)) # 2
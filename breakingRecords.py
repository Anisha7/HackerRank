# Complete the breakingRecords function below.
def breakingRecords(scores):
    # prevent index errors
    if len(scores) == 0:
        return 0, 0

    maxElem = scores[0]
    minElem = scores[0]

    maxCount = 0
    minCount = 0

    # calculate min and max score breaks
    for score in scores:
        if score > maxElem:
            maxCount += 1
            maxElem = score
        if score < minElem:
            minCount += 1
            minElem = score

    return maxCount, minCount

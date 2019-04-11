# Complete the hurdleRace function below.
def hurdleRace(k, height):
    maximum = -1
    for h in height:
        if h > maximum:
            maximum = h
    if maximum > k:
        return maximum - k
    return 0

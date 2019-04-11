# Complete the viralAdvertising function below.
def viralAdvertising(n):
    if (n <= 0) : return 0
    count = 2
    curr = 2 # took care of day 1
    while n > 1:
        curr = (curr*3)//2
        count += curr
        n -= 1
    return count
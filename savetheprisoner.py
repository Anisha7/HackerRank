import os
# Complete the saveThePrisoner function below.
# n = # of seats, m = # of candies, s = start seat
def saveThePrisoner(n, m, s):
    print("Running for %d seats %d candies %s start"%(n,m,s))
    currSeat = s
    while m > 0:
        
        if currSeat > n:
            currSeat = 1
        print("Giving candy to: %d"%currSeat)
        m -= 1
        print("Candy Left: %d"%m)
        currSeat += 1
        
    return currSeat-1

# print(saveThePrisoner(5,2,1)) # 2
# print(saveThePrisoner(7,19,2)) # 6
# print(saveThePrisoner(3,7,3)) # 3

def saveThePrisonerOptimized(n, m, s):
    if (n == m):
        return n
    # offset = m%n
    
    # result = s + offset - 1
    result = (m + s - 1)%n
    if result > n:
        return result - n
    # return result 
    if result != 0:
        return result
    else: 
        return n

# print(saveThePrisonerOptimized(5,2,1)) # 2
# print(saveThePrisonerOptimized(7,19,2)) # 6
# print(saveThePrisonerOptimized(3,7,3)) # 3
# print(saveThePrisonerOptimized(999999999, 999999999, 1))
    

def main():
    f = open('test.py', 'r')
    # content = f.read()
    problems = []
    calculatedResults = []
    for line in f:
        # print("TESTING VALUES: %s"%line)
        testvals = line.split()
        problems.append(line.strip())
        n = int(testvals[0])
        m = int(testvals[1])
        s = int(testvals[2])
        # print("result: %d"%saveThePrisonerOptimized(n,m,s))
        calculatedResults.append(saveThePrisonerOptimized(n,m,s))
    
    f.close()

    f = open('result.py', 'r')
    solutions = []
    for line in f:
        solutions.append(int(line))

    # compare solutions and print problems that don't work
    falseResults = []
    for i in range(len(calculatedResults)):
        if (calculatedResults[i] != solutions[i]):
            falseResults.append(i)
    
    for i in falseResults:
        problem = problems[i]
        print("TEST VALUES: %s"%problem)
        testvals = problem.split()
        n = int(testvals[0])
        m = int(testvals[1])
        s = int(testvals[2])
        print(saveThePrisonerOptimized(n,m,s))
        print("MY RESULT: %s"%calculatedResults[i])
        print("EXPECTED RESULT: %s"%solutions[i])
        print("\n")

    print("*** FAILED %d out of %d CASES ***"%(len(falseResults), len(problems)))

if __name__ == '__main__':
    
    main()

# Complete the countingValleys function in the editor below. 
# It must return an integer that denotes the number of valleys Gary traversed.
# n steps and path s

# For example, if Gary's path is s = [DDUUUUDD], 
# he first enters a valley  units deep. 
# Then he climbs out an up onto a mountain  units high. 
# Finally, he returns to sea level and ends his hike.


def countingValleys(n, s):
    level = 0
    count = 0
    prev = ''
    for i in range(n):
        if (s[i] == 'D'):
            print('D')
            level -= 1
            prev = 'D'
            print(level)
        elif (s[i] == 'U'):
            print('U')
            level += 1
            print(level)
            prev = 'U'
        if (level == 0 and i > 0 and prev == 'U'):
            print(i)
            print('added')
            count += 1
    return count

if __name__ == '__main__':
    count = countingValleys(8, 'UDDDUDUU')
    print('count: ' + str(count))
    count = countingValleys(8, 'DDUUUUDD')
    print('count: ' + str(count))
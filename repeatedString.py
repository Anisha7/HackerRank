# Lilah has a string, s , of lowercase English letters 
# that she repeated infinitely many times.
# Given an integer, n , find and print the number of 
# letter a's in the first  letters of Lilah's infinite string.

# ex. s = 'abcac' and n = 10, we consider 'abcacabcac'. 
# There are 4 occurences of 'a'

#  It should return an integer representing the number of occurrences 
# of a in the prefix of length n in the infinitely repeating string.

def countA(s):
    count = 0
    for i in range(len(s)):
        if (s[i] == 'a'):
            count += 1
    return count

def repeatedString(s, n):
    i = 0
    new = ''
    # create full string of length n
    while (len(new) < n):
        # i tracks the index in s
        if (i == len(s)):
            i = 0
        
        new += s[i]
        i += 1
    print(new)
    return countA(new)

def repeatedStringEfficient(s, n):
    i = 0
    count = 0
    # create full string of length n
    while (n != 0):
        # i tracks the index in s
        if (i == len(s)):
            i = 0
        if (s[i] == 'a'):
            count += 1
        i += 1
    return count

def repStrBetter(s, n):
    mult = n//len(s)
    #result if even divide
    count = s.count('a')*mult

    # if remainder
    extra = n%len(s)
    for i in range(extra):
        if (s[i] == 'a'):
            count += 1
    return count

if __name__ == '__main__':
    print(repStrBetter('abcac', 10)) #4
    print(repStrBetter('aba',10)) #7
    #abaabaabaa
    print(repStrBetter('a', 100000000)) #100000000
        
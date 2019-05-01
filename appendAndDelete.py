# Complete the appendAndDelete function below.
# You can either append or delete at the end of s
# t is the desired string
# return YES if the number of changes == k
def appendAndDelete(s, t, k):
    # find common prefix in s and t
    commonLen = 0
    for i in range(len(s)):
        if i >= len(t):
            break
        if s[i] != t[i]:
            break
        commonLen += 1
    # result is leftover length * 2

    # how much of s is leftover
    sleft = len(s) - commonLen
    # how much of t is leftover
    tleft = len(t) - commonLen

    result = sleft + tleft

    if (result > k):
        return "No"
    if (result%2 == k%2):
        return "Yes"
    if (len(s) + len(t) - k < 0):
        return "Yes"
    return "No"

print(appendAndDelete("y", "yu", 2)) # NO
print(appendAndDelete("abcd", "abcdert", 10)) # NO
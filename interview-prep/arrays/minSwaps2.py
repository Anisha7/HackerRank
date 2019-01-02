# You are given an unordered array consisting of consecutive integers union [1, 2, 3, ..., n] 
# without any duplicates. You are allowed to swap any two elements. 
# You need to find the minimum number of swaps required to sort the array in ascending order.


# O(1)
def swap(q, i, j):
    if (j >= len(q)):
        return q
    q[i],q[j] = q[j],q[i]
    return q

def isSorted(arr):
    return arr == list(range(1, len(arr) + 1))

def minimumSwaps2(arr):
    count = 0
    i = 0
    while (isSorted(arr) == False):
        
        # prevent index out of range
        if (i >= len(arr)):
            i = 0
        # print(arr)
        # print('count: ',count)
        # print('i: ', i)
        if (arr[i] == i+1):
            i += 1
            continue
        # if i+3 is the right place, move it there
        if (arr[i] == i+3):
            # print('arr[i] == i+3')
            arr = swap(arr, i, i+2)
            count += 1

        # if i+2 is the right place, move it there
        if (arr[i] == i+2):
            # print('arr[i] == i+2')
            arr = swap(arr, i, i+1)
            count += 1

        # if i is the right place for arr[i+3]
        if (i+2 < len(arr) and arr[i+2] == i+1):
            # print('arr[i+2] == i+1')
            arr = swap(arr, i, i+2)
            count += 1
        
        # if i is the right place for arr[i+2]
        if (i+1 < len(arr) and arr[i+1] == i+1):
            # print('arr[i+1] == i+1')
            arr = swap(arr, i, i+1)
            count += 1

        i += 1
        
    # print(arr)
    # print('COUNT')
    return count

if __name__ == '__main__':
    print(minimumSwaps2([7,1,3,2,4,5,6])) #5
    print(minimumSwaps2([4,3,1,2])) # 3
    print(minimumSwaps2([2,3,4,1,5])) # 3
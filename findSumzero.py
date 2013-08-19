def find_zero_sum(arr):
    H = {}
    sum = 0
    for i in xrange(len(arr)):
        sum += arr[i]
        if sum in H.keys():
            print "Find the first sub-array with zero sum:"
            print arr[H[sum]+1:i+1]
            return True
        else:
            H[sum] = i
    return False

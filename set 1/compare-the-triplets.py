
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem

""" 


#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):

    r = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            r[0] += 1
        elif a[i] < b[i]:
            r[1] += 1

    return r


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    
    print(result)





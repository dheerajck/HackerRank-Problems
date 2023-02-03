
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/diagonal-difference/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):

    l = len(arr)
    d1 = 0
    d2 = 0
    d1_starter = 0
    d2_starter = -1

    for i in range(l):
        d1 += arr[d1_starter][i]
        d2 += arr[d2_starter][i]

        d1_starter += 1
        d2_starter -= 1

    return abs(d1 - d2)



if __name__ == '__main__':
   
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)


    
    


"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/plus-minus/problem

""" 


#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def ratio_of_plus_minus_neutral(arr):

    l = len(arr)
    p = n = z = 0

    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1

    print(f"{p/l:.6}")
    print(f"{n/l:.6}")
    print(f"{z/l:.6}")
    
    
if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    ratio_of_plus_minus_neutral(arr)
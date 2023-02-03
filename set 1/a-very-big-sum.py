
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem

""" 


#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)



    
    
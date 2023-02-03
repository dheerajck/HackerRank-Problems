
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/simple-array-sum/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar):
    s = 0
    for i in ar:
        s += i
    return s


if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
    





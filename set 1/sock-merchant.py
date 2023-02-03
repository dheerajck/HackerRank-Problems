
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/sock-merchant/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def number_of_matching_pairs(n, ar):

    # can use Counter
    d = {}
    for i in ar:
        d[i] = d.get(i,0) + 1

    r = 0
    # key is only used to pair, value to match
    for v in d.values():
        r += v // 2
    return r


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = number_of_matching_pairs(n, ar)

    print(result)
    

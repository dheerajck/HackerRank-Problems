
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/abbr/problem

""" 


#
# The function abbreviation is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


import sys

sys.setrecursionlimit(150000)

from functools import cache

@cache
def recursive_check(a, b):

    if a == "" and b == "":
        return 1
    elif b == "":
        if a.islower():
            return 1
        else:
            return 0
    elif a == "":
        return 0

    if len(a) < len(b):
        return 0
    if len(a) == len(b):
        if a.upper() == b:
            return 1
        else:
            return 0


    if a[0].upper() != b[0]:
        if a[0].isupper():
            return 0
        return recursive_check ( a[1:], b )

    if a[0].upper() == b[0]:
        if a[0].isupper():
            return recursive_check ( a[1:], b[1:])
        else:
            return recursive_check ( a[1:], b[1:] ) or recursive_check ( a[1:], b )


def abbreviation(a, b):
    result = recursive_check ( a, b )
    print(result)
    if result == 1:
        return "YES"
    return "NO"


if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)


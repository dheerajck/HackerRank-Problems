
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/die-hard-3/problem

""" 


#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#


from math import gcd


def possibility_for_C_unit(a, b, c):
    """
    this function checks if it is possible to
    get C units of water in a container if we 
    have two containers of volume A unit and B unit
    and unlimited supply of water
    """
    
    if c > max(a,b):
        return "NO"
    
    if c % gcd(a,b) == 0:
        return "YES"
    
    return "NO"


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = possibility_for_C_unit(a, b, c)

        print(result)



"""

author: dheerajck

problem: htreminders://www.hackerrank.com/challenges/divisible-sum-pairs/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSum_Pairs(n, k, ar):

    from math import comb

    d = {}
    number = 0
    divisor = 0
    for i in ar:

        reminder = i % k
        # if reminder is zero, then that number is a divisor of k
        if reminder == 0:
            divisor += 1
            continue 

        #  reminder will be equal to constant * k, 
        # k - reminder will be (k - (constant * k) ) = k(1 - constant), which will be divisible by k
        if (k - reminder) in d:
            number += d[k - reminder]

        if reminder in d:
            d[reminder] += 1  
        else:
            d[reminder] = 1

    number += int(comb(divisor, 2))

    return number 


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSum_Pairs(n, k, ar)

    print(result)
    

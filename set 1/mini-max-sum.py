
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/mini-max-sum/problem

""" 


#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def max_and_min_sum(arr):

    from math import inf
    minimum = inf
    maximum = -inf
    sum_of_elements = 0

    for i in arr:
        sum_of_elements += i
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

    amax_part = sum_of_elements - minimum
    amin_part = sum_of_elements - maximum

    print(amin_part, amax_part)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    max_and_min_sum(arr)
    

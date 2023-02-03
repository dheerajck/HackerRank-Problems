
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def number_of_ways_to_divide_chocolate(s, d, m):

    if m > len(s):
        return 0

    c = 0
    for start in range(len(s) -  m + 1):
        if sum(s[ start: start + m ]) == d:
            c += 1        
    return c


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = number_of_ways_to_divide_chocolate(s, d, m)

    print(result)
    

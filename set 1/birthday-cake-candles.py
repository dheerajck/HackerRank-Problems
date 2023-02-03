
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def number_of_tallest_birthday_candles(candles):

    d = {}
    maximum = -1

    for i in candles:

        # it should be 0 not -1 since a key in dict 
        # will have a minimum value 1 (0+1) and not 0 (-1+1)
        d[i] = 1 + d.get(i,0)
        if i > maximum:
            maximum = i

    return d[maximum]


if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = number_of_tallest_birthday_candles(candles)

    print(result)
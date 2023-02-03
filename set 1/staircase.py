
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/staircase/problem

""" 


#
# The function accepts INTEGER n as parameter.
#


def print_staircase(n):
    space = n - 1
    symbol = 1
    for i in range(n):
        print(" " * space + "#" * symbol)
        space -= 1
        symbol += 1


if __name__ == '__main__':
    
    n = int(input().strip())
    print_staircase(n)
    





"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/drawing-book/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):

    result = min([p//2, (n - p + (1 - n % 2) ) // 2])
    return result


if __name__ == '__main__':

    n = int(input().strip())
    p = int(input().strip())

    result = pageCount(n, p)
    print(result)
    


    
    
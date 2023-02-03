
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/diwali-lights/problem

""" 


#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#


def find_light_combination(n):
    
    m = 10**5

    result = (2 ** n) - 1
    return result % m


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = find_light_combination(n)
        
        print(result)



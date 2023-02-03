
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/kangaroo/problem

""" 


#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def find_possibility_of_kangaroo_meeting(x1, v1, x2, v2):
    
   
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return "NO"
    
    
    t = (x1 - x2) / (v2 - v1)
    
    if not t.is_integer():
        return "NO"
         
    
    if (x1 + v1 * t) == (x2 + v2 * t):
        return "YES"
    
    return "NO"
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = find_possibility_of_kangaroo_meeting(x1, v1, x2, v2)

    print(result)
    


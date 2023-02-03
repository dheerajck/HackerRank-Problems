
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/between-two-sets/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def gcd_function(a, b):
    
    a, b = b, a % b
    
    while b != 0:
        
        a, b = b, a % b
    
    return a
    
      
def get_total_number(a, b):
    
    from functools import reduce
    
   
    # lcm of first array
    lcm = reduce( lambda x,y: (x * y) / gcd_function(x,y), a )
  
   
    # gcd of second array
    gcd = reduce( gcd_function, b )
   
    output = 0
    lcm = int(lcm)
    gcd = int(gcd)
    
    for i in range(lcm, gcd + 1, lcm):
        
        if gcd % i == 0:
            output += 1
            
    return output
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = get_total_number(arr, brr)

    print(total)
    


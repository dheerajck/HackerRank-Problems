
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/counting-valleys/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
 

def number_of_valleys_traversed(steps, path):
    
    """
    A valley is a sequence of consecutive steps below sea level, 
    =>starting with a step down from sea level and ending with 
    a step up to sea level
    valley => D .. U
    
    using maths for simple implementation
    using two loops # 1
    """
    val = 0
    # s = [0]
    v = {"D": -1, "U": +1}
    
    # intially start = 1, 
    # start = 1 implies travelling through sea level
    # so start = 0 implies travelling through valley
    start = 1
    result = 0
    for i in path:
        val += v[i]
        # sea level + val < 0 => going to valley
        if val < 0 and start:
            start = 0
            
        # valley + val = 0 => reached back to sea level from valley
        # this implies the hiker have completed travelling
        # through a valley so r += 1
        elif start == 0 and val == 0:
            start = 1
            result  += 1
            
    return result
            
            
if __name__ == '__main__':

    steps = int(input().strip())
    path = input()

    result = number_of_valleys_traversed(steps, path)
    print(result)
    

    

    
    

   
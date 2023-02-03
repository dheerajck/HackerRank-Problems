
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/grading/problem

""" 


#
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def count_Apples_and_Oranges(s, t, a, b, apples, oranges):
    
    result = [0, 0]
    for distance_value in apples:
        if s <= a + distance_value <=t:
            result[0] += 1
            
    for distance_value in oranges:
        if s <= b + distance_value  <= t:
            result[1] += 1
            
    print(result[0])
    print(result[1])
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    count_Apples_and_Oranges(s, t, a, b, apples, oranges)
    

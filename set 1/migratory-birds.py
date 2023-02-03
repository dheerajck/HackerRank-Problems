
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/migratory-birds/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def most_frequently_sighted_migratoryBird(arr):


    # can do with Counter
    d = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1

    # possible to sort dict now because dict are insertion ordered from python 3.6+
    d = {k: v for k, v in sorted(d.items(), key=lambda item:item[1], reverse = True)}

    # initializing key and value variable in our favour to get desired result :)
    # so every keys in the dict will be less than key_r first
    key_r = float("inf") 
    # so every values in the dict will be greater than previous_value first
    previous_value = -1 * float("inf")

    for k, v in d.items():
        if v >= previous_value:
            if k < key_r: key_r = k
            previous_value = v
        else:
            break 

    return key_r


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = most_frequently_sighted_migratoryBird(arr)

    print(result)
    

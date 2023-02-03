
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/jim-and-the-jokes/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY dates as parameter.
#


def find_dates_combinations(dates):
    
    from math import comb

    count_d = {}
    
    for i in dates:
        try:
            date = i[1]
            month = i[0]
            decimal_representaion = int(str(date), month)
        except ValueError:
            continue
        
        if decimal_representaion in count_d:
            count_d[decimal_representaion] += 1
        else:
            count_d[decimal_representaion] = 1

    c = 0
    # only value is needed now 
    # keys are used to organise values 
    for value in count_d.values():
        c += comb(value ,2)

    return c
    

if __name__ == '__main__':
   
    n = int(input().strip())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = find_dates_combinations(dates)

    print(result)
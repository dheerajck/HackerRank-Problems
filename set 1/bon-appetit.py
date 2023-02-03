
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/bon-appetit/problem

""" 


#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bill_equality_check(bill, k, b):
    
    """
    if both paid bill for what they bought correctly, 
    prints Bon Appetit
    """
    total_bill_half = sum(bill) / 2
    amount_anna_should_pay = total_bill_half - bill[k] / 2
    
    if b == amount_anna_should_pay:
        print("Bon Appetit")
    else:
        # it is said money_anna_should_get will be always integer
        money_anna_should_get = bill[k] / 2
        print(money_anna_should_get)


if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bill_equality_check(bill, k, b)
    


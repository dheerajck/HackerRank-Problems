
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/electronics-shop/problem

""" 


#
# function returns maximum amount that can be spent for a keyboard and usb, If it is not possible to buy both items function returns -1
#


def expensive_Keyboard_and_USB_with_in_budget(keyboards, drives, b):

    # descending sort
    keyboards.sort(reverse = True)
    # ascending sort
    drives.sort() 
    maximum = -1

    ascending_counter = 0

    # m + n iterator
    for desc_value in keyboards:
        while ascending_counter < len(drives):

            value_of_products_in_hand = desc_value + drives[ascending_counter]

            if value_of_products_in_hand == b:
                return value_of_products_in_hand

            if value_of_products_in_hand > b:
                break
            if value_of_products_in_hand < b:
                maximum = max(maximum, value_of_products_in_hand)
                ascending_counter += 1

    return maximum


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = expensive_Keyboard_and_USB_with_in_budget(keyboards, drives, b)
    print(moneySpent)
    

    
    
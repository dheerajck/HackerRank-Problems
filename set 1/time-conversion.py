
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/time-conversion/problem

""" 


#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):

    hour = int(s[:2])
    # can get hour by doing split and slicing
    # list_splitted = s.split(":")
    # hour = int(list_splitted[0])

    am_pm = s[-2:]

    if (am_pm == "AM" and hour == 12) or (am_pm == "PM" and hour != 12):
        hour = (hour + 12) % 24

    # hour = format(hour, '02')
    hour = f"{hour:02d}"
    # Adding leading zero two make hour two digits
    # https://stackoverflow.com/a/21620664
    """
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    """

    return f"{hour}{s[2:-2]}"


if __name__ == '__main__':
   
    s = input()

    result = timeConversion(s)
    
    print(result)
    




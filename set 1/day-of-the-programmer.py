
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

""" 


#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):

    # works for both calender 
    def leap_year_check(year):

        if year < 1918:
            return year % 4 == 0 
        if year >= 1918:
            p = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
            return p

    if year == 1918:
        return f"26.09.1918"
    if leap_year_check(year):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"


if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
    

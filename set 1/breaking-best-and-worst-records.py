
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

""" 


#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breaking_records_count(scores):

    mx = mn = 0
    maximum = minimum = scores[0]

    for game_score in scores[1:]:

        if game_score > maximum:
            mx += 1
            maximum = game_score

        elif game_score < minimum:
            mn += 1
            minimum = game_score

    return [mx, mn]


if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breaking_records_count(scores)

    print(result)
    

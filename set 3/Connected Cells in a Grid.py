
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

""" 


#
# The function connectedCell is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def connectedCell(matrix):

    just_a_flag = {(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1}
    max_ones_value = 0
    if len (just_a_flag) == 0:
        return 0

    root = just_a_flag.pop()

    while len(just_a_flag) > 0:

        ones_in_region = 1

        # visited_ones = {root} not used so commented
        to_be_visited = []

        while True:

            x, y = root

            for x_range in range(x - 1, x + 2):
                for y_range in range(y - 1, y + 2):

                    if (x, y) == (x_range, y_range):
                        continue

                    if 0 <= x_range <= len(matrix)-1 and 0 <= y_range <= len(matrix[0])-1:
                        if matrix[x_range][y_range] == 1:

                            if (x_range, y_range) in just_a_flag:
                                to_be_visited.append((x_range, y_range))


                                just_a_flag.remove ( (x_range, y_range) )
                                ones_in_region += 1

            if len(to_be_visited) == 0:
                break

            visiting = to_be_visited.pop(-1)
            root = visiting

        max_ones_value = max(ones_in_region, max_ones_value)
        if len(just_a_flag) > 0:
            root = just_a_flag.pop()
            
    return max_ones_value


if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    print(result)


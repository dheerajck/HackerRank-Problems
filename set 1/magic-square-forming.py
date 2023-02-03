
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/magic-square-forming/problem

""" 


#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def next_position(new_row, new_column, final_step, row_len=3, col_len=3):
    
    step = 0
    # print(new_row, new_column)
    while step < final_step:
        while step < final_step:
            flag = 0
            if new_row == 0 and new_column < col_len - 1:
                if new_column + 1 < col_len:
                    flag = 1
                    new_column += 1
                    step += 1
            if flag == 0:
                break

        while step < final_step:
            flag = 0
            if new_column == col_len - 1 and new_row < row_len - 1:
                if new_row + 1 < row_len:
                    flag = 1
                    new_row += 1
                    step += 1
            if flag == 0:
                break

        while step < final_step:
            flag = 0
            if new_row == row_len - 1 and col_len > 0:
                if new_column - 1 > -1:
                    flag = 1
                    new_column = new_column - 1
                    step += 1
            if flag == 0:
                break

        while step < final_step:
            flag = 0
            if new_column == 0 and row_len > 0:
                if new_row - 1 > -1:
                    flag = 1
                    new_row = new_row - 1
                    step += 1
            if flag == 0:
                break

    return new_row, new_column


def matrix_rotation(matrix, rotation_number=2):
    
    row_len = len(matrix)
    col_len = len(matrix[0])

    new_matrix = empty_list()
    new_matrix[1][1] = 5
    total_val = row_len * col_len
    current_val = 0
    # if anticlockwise
    # outer length that is total_perimeter will be 2*row + 2*(column-2)
    # step = outer length - step
    total_perimeter = (2 * row_len) + (2 * (col_len - 2))

    final_step = rotation_number % total_perimeter

    iter_row = 0
    iter_col = 0

    while current_val <= total_val:
        element = matrix[iter_row][iter_col]

        new_row, new_column = next_position(iter_row, iter_col, final_step)
        # print(new_row, new_column)

        new_matrix[new_row][new_column] = element

        current_val += 1

        # finding next row and column to be rotated
        iter_row, iter_col = next_position(iter_row, iter_col, 1)

    return new_matrix


def empty_list(row=3, column=3):
    new_list = []
    for i in range(row):
        new_list.append([None] * column)
    return new_list


def formingMagicSquare(s):
    
    # first_magic_matrix = [[None] * 3] * 3 here all list is copy of one 
    # so value of every row in the nested list will be always be same

    first_magic_matrix = empty_list()
    first_magic_matrix[1][1] = 5

    first_magic_matrix[0][0] = 8
    first_magic_matrix[2][2] = 2

    first_magic_matrix[0][2] = 4
    first_magic_matrix[2][0] = 6

    first_magic_matrix[1][0] = 1
    first_magic_matrix[1][2] = 9

    first_magic_matrix[0][1] = 3
    first_magic_matrix[2][1] = 7

    # we know there will be only 8 magic matrix
    # n = 8 // 2
    minimum_cost = float("inf")

    # list and copy because change in value of one list
    # should not affect value of other lists
    import copy
    tp = copy.deepcopy(first_magic_matrix)

    matrix = matrix_rotation(tp)
    yy = 0
    # print(matrix)
    while yy <= 8:

        cost = 0
        for i in range(len(s)):
            for j in range(len(s)):
                cost += abs(s[i][j] - matrix[i][j])

        minimum_cost = min(cost, minimum_cost)
        # print(matrix)

        matrix2 = list(zip(*matrix))

        cost = 0
        for i in range(len(s)):
            for j in range(len(s)):
                cost += abs(s[i][j] - matrix2[i][j])

        minimum_cost = min(cost, minimum_cost)

        matrix = matrix_rotation(tp, yy)
        yy += 2

    return minimum_cost


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
    

    
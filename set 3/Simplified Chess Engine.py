
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/simplified-chess-engine/problem

""" 


BOTTOM_BORDERS = {0,1,2,3}
TOP_BORDERS = {12,13,14,15}

LEFT_BORDERS = {0,4,8,12}
RIGHT_BORDERS = {3,7,11,15}


def rook_possible_movements(current_position, our_positions, enemey_positions, current_player_color):

    running = True


    for incrementer, border in ((-1, LEFT_BORDERS), (1, RIGHT_BORDERS), (-4, BOTTOM_BORDERS),(4, TOP_BORDERS)):

        current_temp_position = current_position

        while running:

            new_our_dict = dict(our_positions)
            new_enemy_dict = dict(enemey_positions)


            if current_temp_position in border:
                break

            next_position = current_temp_position + incrementer


            if next_position == enemey_positions["queen_info"]:

                piece = our_positions[current_position]

                new_our_dict [next_position] = piece
                del new_enemy_dict[next_position]

                if current_player_color == "white":
                    boolean_to_return_back = True   
                else:
                    boolean_to_return_back = False


                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield boolean_to_return_back, new_our_dict, new_enemy_dict
                running = False
                break


            if next_position in our_positions:
                break


            if next_position in enemey_positions:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                del new_enemy_dict[next_position]

                new_our_dict[next_position] = piece

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield None, new_our_dict, new_enemy_dict
                break


            if next_position in border:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                new_our_dict[next_position] = piece

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield None, new_our_dict, new_enemy_dict
                break


            else:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                new_our_dict [next_position] = piece

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield None, new_our_dict, new_enemy_dict
                current_temp_position = next_position



def bishop_possible_movements(current_position, our_positions, enemey_positions, current_player_color):

    running = True

    for incrementer, border in ((5, TOP_BORDERS | RIGHT_BORDERS), (-5, LEFT_BORDERS | BOTTOM_BORDERS), (3, TOP_BORDERS | LEFT_BORDERS),(-3, BOTTOM_BORDERS | RIGHT_BORDERS)):

        current_temp_position = current_position

        while running:

            new_our_dict = dict(our_positions)
            new_enemy_dict = dict(enemey_positions)


            if current_temp_position in border:
                break

            next_position = current_temp_position + incrementer


            if next_position == enemey_positions["queen_info"]:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                new_our_dict [next_position] = piece

                del new_enemy_dict[next_position]

                if current_player_color == "white":
                    boolean_to_return_back = True   
                else:
                    boolean_to_return_back = False

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield boolean_to_return_back, new_our_dict, new_enemy_dict
                running = False
                break


            if next_position in our_positions:
                break


            if next_position in enemey_positions:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                new_our_dict [next_position] = piece

                del new_enemy_dict[next_position]

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield None, new_our_dict, new_enemy_dict
                break


            if next_position in border:

                piece = our_positions[current_position]
                del new_our_dict[current_position]
                new_our_dict [next_position] = piece

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position               

                yield None, new_our_dict, new_enemy_dict
                break


            else:

                piece = our_positions[current_position]

                del new_our_dict[current_position]
                new_our_dict [next_position] = piece

                if piece == "Q":
                    new_our_dict["queen_info"] = next_position

                yield None, new_our_dict, new_enemy_dict
                current_temp_position = next_position



def queen_possible_movements(current_position, our_positions, enemey_positions, current_player_color):
    rook_func = rook_possible_movements(current_position, our_positions, enemey_positions, current_player_color) 
    bishop_func = bishop_possible_movements(current_position, our_positions, enemey_positions, current_player_color)


    for i in rook_func:
        yield i
    for i in bishop_func:
        yield i



def knight_possible_movements(current_position, our_positions, enemey_positions, current_player_color):

    # up right
    so_can_do_these = (    
                        (2, 1), (2,-1),
                        (-2, 1), (-2,-1),

                        (1, 2), (1,-2),
                        (-1, 2), (-1,-2)
                      )

    for up, right in so_can_do_these:

        new_our_dict = dict(our_positions)
        new_enemy_dict = dict(enemey_positions)

        start_left = 1 if current_position in LEFT_BORDERS else 0
        start_right = 1 if current_position in RIGHT_BORDERS else 0

        # all moves starts from here
        current_temporary_position = current_position 

        magnitude_up = abs(up)
        magnitude_right = abs(right)

        up_inc = 1 if up > 0 else -1
        up_inc = up_inc * 4


        # this variable will tell if the knight is going left from curren position or right from current position
        right_inc = 1 if right > 0 else -1


        while magnitude_up > 0 or magnitude_right > 0:
            if magnitude_up > 0:
                current_temporary_position = current_temporary_position + up_inc
                magnitude_up  = magnitude_up  - 1

            elif  magnitude_right > 0:
                current_temporary_position = current_temporary_position + right_inc
                magnitude_right  = magnitude_right  - 1

            # going right
            if right_inc > 0:
                if current_temporary_position in LEFT_BORDERS and not(start_left):
                    current_temporary_position = None
                    break

            # going left
            if right_inc < 0:
                if current_temporary_position in RIGHT_BORDERS and not(start_right):
                    current_temporary_position = None
                    break

            if (current_temporary_position < 0) or (current_temporary_position > 15):
                current_temporary_position = None
                break


        if current_temporary_position is not None:
            if current_temporary_position not in our_positions:

                if current_temporary_position == enemey_positions["queen_info"]:
                    piece = our_positions[current_position]


                    del new_our_dict[current_position]
                    new_our_dict[current_temporary_position] = piece

                    del new_enemy_dict[current_temporary_position]


                    if current_player_color == "white":
                        boolean_to_return_back = True
                    else:
                        boolean_to_return_back = False

                    yield boolean_to_return_back, new_our_dict, new_enemy_dict
                    break

                else:

                    if current_temporary_position in enemey_positions:

                        piece = our_positions[current_position]

                        del new_our_dict[current_position]
                        new_our_dict[current_temporary_position] = piece

                        del new_enemy_dict[current_temporary_position]
                        yield None, new_our_dict, new_enemy_dict

                    else:

                        piece = our_positions[current_position]
                        del new_our_dict[current_position]

                        new_our_dict[current_temporary_position] = piece
                        yield None, new_our_dict, new_enemy_dict



def recursive_depth(our_Dict, enemy_Dict, depth, max_depth, player_color):

    COLOR_OPPOSITE = {"white": "black", "black": "white"}

    # checking if black got whites queen in blacks last move
    if player_color == "white":
        if "Q" not in our_Dict.values():
            return False

    # checking if white got blacks queen in blacks last move
    if player_color == "black":
        if "Q" not in our_Dict.values():
            return True

    if depth >= max_depth:
        return False


    FUNCTION_CHOOSE = {"Q": queen_possible_movements, "R": rook_possible_movements, 
                       "B": bishop_possible_movements, "N": knight_possible_movements}  


    #####################################################################################

    for position_now, full_name, in our_Dict.items():

        if position_now == "queen_info":
            continue

        function_to_call = FUNCTION_CHOOSE[full_name]

        for condition_check, temp_our, temp_enemy in function_to_call(position_now, our_Dict, enemy_Dict, player_color):

                # print(player_color, temp_our, temp_enemy, "-----", depth, sep="\n")
                # print()

                if player_color =="white":
                    if condition_check is True:
                        return True
                    else:
                        if recursive_depth(temp_enemy, temp_our, depth + 1, max_depth, COLOR_OPPOSITE[player_color]):
                            return True

                if player_color =="black":
                    if condition_check is False:
                        return False
                    else:
                        if not recursive_depth(temp_enemy, temp_our, depth + 1, max_depth, COLOR_OPPOSITE[player_color]):
                            return False


    if player_color =="white":
        return False

    if player_color =="black":
        return True



def serialising_i_say(stats_of_given_piece):

    horizontal_scale = {"A": 0, "B": 1, "C": 2, "D": 3}
    vertical_scale = {"1": 0, "2": 4, "3": 8, "4": 12}
    piece_dict = {}

    for piece_info in stats_of_given_piece:

        piece_name = piece_info[0]

        x = piece_info[1]
        y = piece_info[2]

        position_in_board = int(horizontal_scale[x] + vertical_scale[y])

        piece_dict[position_in_board] = piece_name

        if piece_name == "Q":
            piece_dict["queen_info"] = position_in_board

    return piece_dict



def simplifiedChessEngine(whites, blacks, moves):

    player_color = "white"
    current_depth = 0
    max_depth = moves
    if moves % 2 == 0:
        max_depth = moves - 1

    whites = serialising_i_say(whites)
    blacks = serialising_i_say(blacks)

    a = recursive_depth(whites, blacks, current_depth, max_depth, player_color)

    if a:
        return "YES"
    return "NO"



if __name__ == '__main__':
    
    g = int(input())

    for g_itr in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        whites = []

        for _ in range(w):
            whites.append(list(map(lambda x: x[0], input().rstrip().split())))

        blacks = []

        for _ in range(b):
            blacks.append(list(map(lambda x: x[0], input().rstrip().split())))

        result = simplifiedChessEngine(whites, blacks, m)
        print(result)


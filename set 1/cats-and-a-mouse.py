
"""

author: dheerajck

problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

""" 


# function returns which cat can get the mouse and if both cant get the mouse, it returns Mouse name


def catAndMouse(x, y, z):

    dist_a = abs(x - z)
    dist_b = abs(y - z)

    if dist_a == dist_b:
        return "Mouse C"
    if dist_a < dist_b:
        return "Cat A"
    if dist_a > dist_b:
        return "Cat B"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)
        

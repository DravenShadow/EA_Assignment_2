"""
    Author: Rowland DePree                  Pascal_Triangle_V2.py

    This is a program to print out pascal triangle's to a certain depth specified by the user.
"""


def pascal(depth, pos):
    '''
    A recursive method to find a particular number by adding the two previous numbers together.
    :param depth:
    :param pos:
    :return:
    '''
    if depth == pos:
        return 1
    elif depth <= -1 or pos <= -1:
        return 0
    else:
        return pascal(depth - 1, pos) + pascal(depth - 1, pos - 1)


def pascal_row(row, depth, list):
    '''
    A recursive method find a row in pascal's triangle
    :param row:
    :param depth:
    :param list:
    :return list:
    '''
    if row > depth:
        return
    else:
        list.append(pascal(depth, row))
        pascal_row(row + 1, depth, list)
        return list


def pascal_depth(curr_depth, desired_depth):
    '''
    A recursive method to find the depth in pascal's triangle and print out the depth's row
    :param curr_depth:
    :param desired_depth:
    :return:
    '''
    if curr_depth > desired_depth:
        return
    else:
        list = []
        print pascal_row(0, curr_depth, list)
        pascal_depth(curr_depth + 1, desired_depth)


def main():
    """
    A method to take in user specified depth
    :return:
    """
    pascal_depth(0, input('Enter in desired level of pascals triangle:'))


"""
    Starts the main method
"""
if __name__ == "__main__":
    main()

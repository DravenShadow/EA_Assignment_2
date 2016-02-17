def pascal(depth, pos):
    if depth == pos:
        return 1
    elif depth <= -1 or pos <= -1:
        return 0
    else:
        return pascal(depth - 1, pos) + pascal(depth - 1, pos - 1)


def pascal_row(row, depth, list):
    if row > depth:
        return
    else:
        list.append(pascal(depth, row))
        pascal_row(row + 1, depth, list)
        return list


def pascal_depth(curr_depth, desired_depth):
    if curr_depth > desired_depth:
        return
    else:
        list = []
        print pascal_row(0, curr_depth, list)
        pascal_depth(curr_depth + 1, desired_depth)


def main():
    pascal_depth(0, 5)


if __name__ == "__main__":
    main()

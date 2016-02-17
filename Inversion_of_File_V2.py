"""
    Author: Rowland DePree                      Inversion_of_File_V2.py

    A program designed to read in an file containing numbers on each line.  Then sort the array of numbers using
    one of the divide and conquer sorting techniques, quick sort.  Then it will compare the original array to the newly
    sorted array to see which spots are the same.  The quick sort algorithm code was obtained
    from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html.  It is NOT of my own creation.
"""


def compare_file_with_array(array, sorted_array):
    """
    A method to compare two arrays and print out the matching positions
    :param array:
    :param sorted_array:
    :return:
    """
    print 'Line numbers from file that match up with sorted array: '
    for x in range(len(array)):
        if array[x] == sorted_array[x]:
            print(x + 1)


def quickSort(alist):
    """
    A method to start the quick sort algorithm
    :param alist:
    :return:
    """
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    """
    A recursive method used to partition the alist
    :param alist:
    :param first:
    :param last:
    :return:
    """
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """
    A method used to sort the list at the given first and last points
    :param alist:
    :param first:
    :param last:
    :return:
    """
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def read_in_list(file):
    """
    A method to read in a file containing numbers
    :param file:
    :return:
    """
    list = []
    f = open(file, 'r')
    for line in f:
        if line[0:(len(line) - 1)] == '':
            pass
        else:
            list.append(int(line[0:(len(line) - 1)]))
    f.close()
    print 'DONE READ_IN_LIST'
    return list


def main():
    """
    The main method.  Here it will take in the location of the file from the users and call on other methods to read in the file,
    sort it, and compare it.
    :return:
    """
    list = read_in_list(raw_input('Enter in location of file: '))
    original_list = list[:]
    quickSort(list)
    compare_file_with_array(original_list, list)


"""
    Starts the main method
"""
if __name__ == '__main__':
    main()

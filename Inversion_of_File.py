"""
    Author: Rowland DePree                      Inversion_of_File.py

    A program designed to read in an file containing numbers on each line.  Then sort the array of numbers using
    one of the divide and conquer sorting techniques, merge sort.  Then it will compare the original array to the newly
    sorted array to see which spots are the same.
"""


def mergeSort(list):
    """
    A recursive method that does the merge sorting algorithm.  This algorithm is not of my own designed, the original form of it was
    acquired from http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html..
    :param list:
    :return:
    """
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i += 1
            else:
                list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j += 1
            k += 1


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
    return list


def main():
    """
    The main method.  Here it will take in the location of the file from the users and call on other methods to read in the file,
    sort it, and compare it.
    :return:
    """
    list = read_in_list(raw_input('Enter in location of file: '))
    original_list = list[:]
    mergeSort(list)
    compare_file_with_array(original_list, list)


"""
    Starts the main method
"""
if __name__ == '__main__':
    main()

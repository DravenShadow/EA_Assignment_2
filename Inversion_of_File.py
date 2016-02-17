"""
    Author: Rowland DePree                      Inversion_of_File.py

    A program designed to read in an file containing numbers on each line.  Then sort the array of numbers using
    one of the divide and conquer sorting techniques, merger sort.  Then it will compare the original array to the newly
    sorted array to see which spots are the same.
"""


def compare_file_with_array(array, sorted_array):
    """
    A method to compare two arrays and print out the matching positions
    :param array:
    :param sorted_array:
    :return:
    """
    print 'START COMPARE'
    print 'Here are the line numbers with array spots that match: '
    for x in range(len(array)):
        if array[x] == sorted_array[x]:
            print(x + 1)
    print 'DONE WITH COMPARE\nGOODBYE!'


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


def merge(arr, mid):
    """
    A method designed to merge two subarrays together given an array with a mid point.
    :param arr:
    :param mid:
    :return:
    """
    leftArr = arr[:mid]
    rightArr = arr[mid:]

    i = 0
    j = 0
    k = 0
    while i < len(leftArr) and j < len(rightArr):
        if (leftArr[i] < rightArr[j]):
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1


def mergeSort(arr, startIndex, endIndex):
    """
    A recursive method designed to divided the array into two subarray's
    :param arr:
    :param startIndex:
    :param endIndex:
    :return:
    """
    if (startIndex < endIndex):
        mid = (startIndex + endIndex) / 2
        mergeSort(arr, startIndex, mid)
        mergeSort(arr, mid + 1, endIndex)
        merge(arr, mid)


def divideAndConquer(arr):
    """
    A method designed to start the merge sort algorithm
    :param arr:
    :return:
    """
    length = len(arr)
    return mergeSort(arr, 0, length - 1)


def main():
    """
    The main method.  Here it will take in the location of the file from the users and call on other methods to read in the file,
    sort it, and compare it.
    :return:
    """
    # list = read_in_list(raw_input('Enter in location of file: '))
    list = read_in_list(r'/home/draven/PycharmProjects/EA_Assignment_2/integer_file')
    original_list = list[:]
    divideAndConquer(list)
    compare_file_with_array(original_list, list)


"""
    Starts the main method
"""
if __name__ == '__main__':
    main()

def compare_file_with_array(array, sorted_array):
    list = []
    for x in range(len(array)):
        if array[x] == sorted_array[x]:
            list.append(x)
    return list


def read_in_list(file):
    list = []
    f = open(file, 'r')
    for line in f:
        list.append(line[0:(len(line) - 1)])
    f.close()
    try:
        list.remove(r'\n')
    except ValueError:
        pass
    return list


def merge(arr, mid):
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
    if (startIndex < endIndex):
        mid = (startIndex + endIndex) / 2
        mergeSort(arr, startIndex, mid)
        mergeSort(arr, mid + 1, endIndex)
        merge(arr, mid)


def divideAndConquer(arr):
    length = len(arr)
    return mergeSort(arr, 0, length - 1)


def main():
    list = read_in_list(raw_input('Enter in location of file: '))
    original_list = list[:]
    divideAndConquer(list)
    compare_file_with_array(original_list, list)


if __name__ == '__main__':
    main()

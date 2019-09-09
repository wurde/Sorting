def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if arr[cur_index] != arr[smallest_index]:
            tmp = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = tmp
    return arr

def bubble_sort(arr):
    is_unsorted = True

    while is_unsorted:
        did_swap = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                did_swap = True

        if did_swap == False:
            is_unsorted = False
    return arr

def count_sort(arr, maximum =- 1):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'

    if maximum > 0:
        count_arr = [0] * (maximum + 1)
    else:
        for i in range(0, len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        count_arr = [0] * (maximum + 1)

    for i in arr:
      count_arr[i] += 1

    pos = 0;
    for i in range(len(count_arr)):
      while count_arr[i] > 0:
        arr[pos] = i
        pos += 1
        count_arr[i] -= 1

    return arr

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

# TO-DO: implement the Bubble Sort function below
def bubble_sort(arr):
    is_unsorted = True

    while is_unsorted:
        did_swap = False

        for i in range(0, len(arr) - 1):
            print(arr[i], arr[i + 1], arr[i] < arr[i+1])
            # if arr[i] < arr[i+1]:
            #     did_swap = True

        if did_swap = False:
            is_unsorted = False
    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr)
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum =- 1):
    return arr

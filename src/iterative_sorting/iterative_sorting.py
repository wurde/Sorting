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
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum =- 1):
    return arr

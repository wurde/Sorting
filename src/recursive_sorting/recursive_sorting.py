#
# Define methods
#

def merge(left, right):
  elements = len(left) + len(right)
  merged_arr = [0] * elements

  return merged_arr

def merge_sort(arr):
  if len(arr) > 1:
    left = arr[:int(len(arr)/2)]
    right = arr[int(len(arr)/2):]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i = i + 1
      else:
        arr[k] = right[j]
        j = j + 1
      k = k + 1

    while i < len(left):
      arr[k] = left[i]
      i = i + 1
      k = k + 1

    while j < len(right):
      arr[k] = right[j]
      j = j + 1
      k = k + 1

  return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr1)
merge_sort(arr1)
print(arr1)

#
# Dependencies
#

import numpy

#
# Define methods
#

def merge(arrA, arrB):
  elements = len(arrA) + len(arrB)
  merged_arr = [0] * elements
  # TO-DO
  
  return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
  while len(arr) > 1:
    [left, right] = merge(numpy.array_split(arr, 2))

    merge_sort(left)
    merge_sort(right)

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

# 1. Bubble Sort:
# Bubble sort is a simple sorting algorithm that works
# by repeatedly swapping the adjacent elements if they are in wrong order.

numbers = [6, 5, 3, 1, 8, 7, 2, 4]

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort_optimized(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if swapped == False:
      break
  return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort_recursive(arr):
  n = len(arr)
  if n <= 1:
    return arr
  for i in range(n-1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
  return bubble_sort_recursive(arr[:n-1]) + [arr[n-1]]

# Bubble sort recursive Time Complexity: O(n^2)
# Bubble sort recursive Space Complexity: O(n)
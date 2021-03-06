# Linear Search:
# Linear search to find an element "20" in a given lists of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def findNumberByLinearSearch(numbers, numberToFind):
    for index, number in enumerate(numbers):
        if number == numberToFind:
            return index
    return -1

# Time complexity of this algorithm is O(n)
# Space complexity of this algorithm is O(1)

# Binary Search Sorted Array:
# Pseudo code:
# 1. Find the middle element of the list
# 2. If the middle element is the number, return the index
# 3. If the middle element is greater than the number, search the left half of the list
# 4. If the middle element is less than the number, search the right half of the list
# 5. If the number is not found, return -1

def findNumberByBinarySearch(numbers, numberToFind):
  low = 0
  high = len(numbers) - 1
  while low <= high:
      mid = (low + high) // 2
      if numbers[mid] == numberToFind:
          return mid
      elif numbers[mid] < numberToFind:
          low = mid + 1
      else:
          high = mid - 1
  return -1

# Time complexity of this algorithm is O(log n)
# Space complexity of this algorithm is O(1)

# If the list is not sorted, then the algorithm will not work
# Then, Time complexity of this algorithm is O(n log n) and Space complexity of this algorithm is O(1)

# Linear Search Recursive:
# Pseudo code:
# 1. If the list is empty, return -1
# 2. If the first element is the number, return the index
# 3. If the first element is greater than the number, search the left half of the list
# 4. If the first element is less than the number, search the right half of the list
# 5. If the number is not found, return -1

def findNumberByLinearSearchRecursive(numbers, numberToFind):
    if len(numbers) == 0:
        return -1
    if numbers[0] == numberToFind:
        return 0
    return findNumberByLinearSearchRecursive(numbers[1:], numberToFind) + 1

# Time complexity of this algorithm is O(n)
# Space complexity of this algorithm is O(n)

# Binary Search Recursive:
# Pseudo code:
# 1. If the list is empty, return -1
# 2. Find the middle element of the list
# 3. If the middle element is the number, return the index
# 4. If the middle element is greater than the number, search the left half of the list
# 5. If the middle element is less than the number, search the right half of the list
# 6. If the number is not found, return -1

def findNumberByBinarySearchRecursive(numbers, numberToFind):
  if len(numbers) == 0:
      return -1
  mid = len(numbers) // 2
  if numbers[mid] == numberToFind:
      return mid
  elif numbers[mid] < numberToFind:
      return findNumberByBinarySearchRecursive(numbers[mid + 1:], numberToFind)
  return findNumberByBinarySearchRecursive(numbers[:mid], numberToFind)

# Time complexity of this algorithm is O(log n)
# Space complexity of this algorithm is O(log n)

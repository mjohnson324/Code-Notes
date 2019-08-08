def binary_search(list, item):
	low = 0 # Track list with two points
	high = len(list) - 1

	while low <= high:
		mid = (low + high) // 2 # Check mid-point
		guess = list[mid]
		if guess == item: # reset high or low based on how guess compares to item
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
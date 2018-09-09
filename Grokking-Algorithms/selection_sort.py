# Memory: "drawers" with addresses (e.g. fe0ffeeb)
# Store related items? Use an array or list!

# Array: contiguous storage
# Because elements must be contiguous, adding new elements is challenging
# if memory slot taken up whole array must be moved to wherever it can fit
# Workaround: reserve more space (may waste memory or have to move anyway)
# Strength: instant lookup, random access
# Reading = O(1), Insertion = O(N), Deletion = O(N)

# Linked List: items go anywhere
# Strength: more manageable storage and additions
# items store addresses to next item to connect
# + No need to move items!
# Weakness: lookup (must start at #1 every time), sequential access
# Reading = O(N), Insertion = O(1), Deletion = O(1)

# 2.1 Use a linked list (inserts matter more than lookup)
# 2.2 linked list (You won't randomly take an order in the middle of the queue; you'll only add them on one end and remove them on another)
# 2.3 array (random access necessary)
# 2.4 Array elements must be moved in the event of inserts, which is slow O(N)
# 2.5 Insertion: faster than arrays, fast like linked lists
# Reading: potentially as slow as a linked list (You must traverse it based on the first letter)

# Selection sort: 
# 1. select the first item best meeting the criteria (O(N))
# 2. select the next item; do this repeatedly until none are left.
# This process takes O(N^2) time

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5,3,6,2,10]))

def greet(name):
    return 'Hello, ' + name + '!'

print(greet('Michael'))


# >>> def greet(name):
# ...     return 'Hello, ' + name + '!'

# >>> greet('Dan')
# 'Hello, Dan!'

# >>> import dis
# >>> dis.dis(greet)
# 2   0 LOAD_CONST     1 ('Hello, ')
#     2 LOAD_FAST      0 (name)
#     4 BINARY_ADD
#     6 LOAD_CONST     2 ('!')
#     8 BINARY_ADD
#    10 RETURN_VALUE
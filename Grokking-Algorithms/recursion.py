# Loops vs. recursion: 
# Loops > performance
# Recursion requires memory for each function call. High memory consumption requires applying loops
# or tail recursion instead (not supported in Python)
# Recursion > productivity/problem modeling

# Base Case: function is done; no recursive calls
# Recursive Case: function calls itself
# Call Stack: memory stack used by computers to store variable data in different functions
# Comes into play whenever function called in another function
# Variables in each function call are inaccessible to other functions in stack

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile.is_empty() is not True:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!")

def look_for_key_recursive(box):
    for item in box:
        if item.is_a_box():
            look_for_key_recursive(item)
        elif item.is_a_key():
            print("Found the key!")

def countdown(i):
    print(i)
    if i <= 0: # base case
        return None
    else: # recursive case
        countdown(i - 1)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
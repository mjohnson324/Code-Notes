Dunder Methods:
__hash__: What hash value an object returns. To be hashable, objects must maintain the same value and equal themselves.
__bool__: How an object is evaluated for its truthiness
__str__: What gets printed by print
__iter__: Makes an object iterable
__next__: Determines how iteration proceeds
__eq__: How an object is evaluated for equality
__del__: How an object is removed from memory
__call__: How an object is invoked when declared as a function

super() for inheritance

-Conditional expressions (eg 8 > x > 4) can be saved as variables
-Python functions take arguments as a Tuple
-.get doesn't raise exceptions for nonexistent dictionary keys

Useful Modules:
Math Module- .ceil, abs, max, min, .sqrt, .floor, .round
Random Module- .randint, .random, .shuffle, .choice, .randrange

Binary Operators:
<< - Left-shift (x << y = x * 2**y)
>> - Right-shift (x >> y = x / 2**y)
| - OR (compare bits, get 1 unless both 0)
& - AND (compare bits, get 0 unless both 1)
^ - XOR (~x if y bit is 1, same if y bit is 0)
~ - complement (~x = -x -1)

if name == '__main__':

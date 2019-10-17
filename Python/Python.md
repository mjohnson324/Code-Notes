# Python

* Python functions take arguments as a tuple
* Activating a project: if name == '__main__':

## Inline Documentation

* For light and accessible documentation Python uses docstrings, consisting of triple-double quotes (""") to document code within the code itself.
* By convention, docstrings are placed at the top of an object's definition. Docstrings placed this way will be printed when the user checks an object's definition with the built-in "help" function.


## Classes

* super(): For inheritance

### Dunder Methods

* __hash__: What hash value an object returns. To be hashable, * objects must maintain the same value and equal themselves.
* __bool__: How an object is evaluated for its truthiness
* __str__: What gets printed by print
* __iter__: Makes an object iterable
* __next__: Determines how iteration proceeds
* __eq__: How an object is evaluated for equality
* __call__: How an object is invoked when declared as a function

## Standard Objects

### Dictionaries

* .get doesn't raise exceptions for nonexistent dictionary keys

## Useful Modules

* math- .ceil, abs, max, min, .sqrt, .floor, .round
* random- .randint, .random, .shuffle, .choice, .randrange

## Binary Operators, x _ y

* Left-shift `x << y == x * 2**y`
* Right-shift `x >> y == x / 2**y`
* Complement `~x # returns -x -1`
* XOR `x ^ y # returns _`
* OR `x | y # returns 1 unless both 0`
* AND `x & y # returns 0 unless both 1`

Bit: binary digit
Byte: 8 bits (256 possible values)
Basis of storage is a byte

Encoding: Translating bytes to other characters
Octal, Hexadecimal, Base64, unicode, utf-8, etc.
2⁸ = 16² = 256
Hex: IP address, hexspeak for errors
Hex used for color codes because 256 values.
RGB is additive model (add colors), 3 bytes per color
Red-Yellow-Blue is subtractive, used in printing

Abstract Data Type- concept for storing data; the rules are what matter

Data Structure- A way of organizing data in memory

Sliding Window:
    -Construct for efficient array analysis
    -Start/end indices represent a sub-portion of data and are incremented separately

Set:
	-
	-Key Methods: add, includes, delete

Map:
	-
	-Key Methods: set, get, delete

Stack: "Last in, first out"
	-Data type where data entries can only be added and removed individually from one end
	-Key Methods: push, pop
	Example: function calls in other functions, including recursive calls
	Stacks - Simon says color game, backspace, language call stack
    Stack Frame - a function's slice of stack
    Stack (LIFO) - call stack, browsing history

Queue: "First in, first out"
	-Data type where entries are added in one end and removed on the opposite end
	-Key Methods: enqueue, dequeue
	job scheduling (Rails, DMV, deli)
    JS message queue (function order)
    Stack from queue
    OS queues: multi level priority
    Cyber Monday shopping

Node- An object with data and pointers to other objects with data.
	-They link together to form different data structures.

Trees:
	-Hierarchies of data branching outward. Nodes link to lower-level nodes in a "parent-child" arrangement, where parents can have multiple children but children have only one parent
		Example: file systems
		Root- The top-most node
		Leaves- Nodes without children
		Subtree- A subset of the tree not including the root
		Depth- The length of the longest chain of nodes from the root to a leaf
		Binary Tree- Tree where each node has only two children
		Binary Search Tree- Binary tree where all left nodes are less than the current node and all right nodes are greater than the current node
		Balanced Tree - Tree where the number of nodes on each side of the root is nearly equal and the difference in depth between the deepest left branch and right branch is not greater than one.
	-Key Methods: Parent, value, left & right (binary)

Root, parent, children, siblings, leaves
Childless nodes are leaves, others are internal
There are x-1 for x nodes
A tree is a recursive structure
Depth- number of edges a node is away from root
Height- number of edges from a node to its most distant leaf
Balanced trees are better for searching and insertion
Applications: OOP inheritance, folders
Binary trees useful for search and insertion
Tree - Node - root - left and right
Insertion: start at root, compare value, branch or insert
Binary search = divide and conquer
4 binary trees
Works because entries are ordered
In databases! B or t tree, indexing

	Traversal Methods:
		1. Depth-First-Search (moving down left-most branch first)
			-Recursive and iterative approaches
			-Iteration uses a stack
			-Recursion recursively checks all the children of each node (left first, then right)
		2. Breadth-First-Search (moving left to right, reading nodes the same distance from the root)
			-Iterative approach (a queue)
			-Add a node's children into the queue; eventually you will have all the nodes

Linked List:
	-Nodes organized like a chain, where nodes have pointers to other nodes (one-to-one)
		-AKA unary tree
	-Key Methods: next, value, previous (for doulby-linked lists)
	-Runtime: Insert/Eject (1), Read (n)

Hashmap: Runtime: Insert/Eject (n), Read (1)

LRU Cache: A combination of a hashmap and linked list, inheriting the best performance of both
Tracks links in the hashmap

Array:
	-Indices are not stable
Ring Buffer- Arrays employ these for greater efficiency when adding in values

Graph:
	-Nodes interconnected in a many-to-many relationship

Recursion:
	-Function that calls itself
		Base Case- The end result of recursion; a return value
		Inductive Step- Step in which recursion occurs
		Memoization- recording values of recursive calls during execution
			-Key to reducing runtime of many recursive functions (e.g. fibonacci sums)
	-Recursive methods can be written iteratively
	Strategy:
		1. Identify how to reduce the problem to its base case(s)
			-The base case is the most trivial case
		2. Think of how to get the next case after the base case
			-Make sure the return values are of the same type
			-Compare and contrast successive solutions to identify the inductive step
		3. Get a stack trace going for analysis

Binary Search: Find an element or its position in a list in
	O(logN)
	-Applies only to sorted lists; otherwise bifurcation provides no guarantee of finding element
	Base Case: Default to null value, find the element or run out of elements to check (1 or less)
	Inductive Step:
		1. Start at the list's midpoint
		2. Check against the midpoint value:
			a. For midpoints smaller than the target, look list values left of the midpoint
			b. For midpoints larger than the target, look right.
				-Track the index by adding the mid-point's index value
		3. Finally, if you find the element return its position. If not, return null

Merge Sort: Sort a list (describe more specifically here)
	Nlog(N)
	Base Case: return the array when one or fewer elements remain to sort
	Inductive Step:
		1. Split the array into halves
		2. Perform merge-sorting on each half
			1. Create two new arrays to add the array's contents to
			2. Append elements into each array based on some pivot value
			3. Concatenate the left and right arrays
		4. Finally, merge the sorted arrays

Quick Sort: Sort a list in the fastest(?) time possible
	Nlog(N)
	Base Case: return the array when one or fewer elements remain to sort
	Inductive Step:
		1. Select an element to be a pivot
		2. Divide up elements into those smaller than the pivot and those larger than the pivot
		3. Call quicksort on each list of elements
		4. Finally, concatenate left elements, the pivot, and right elements together

Traveling Salesman: O(N!)

Amortization- A technique to optimize average-case insertions into a data structure. Increasing a contiguous structure proportionaly amount creates occasional slowdowns but most insertions will be constant-time.

Base Case: function is done; no recursive calls
Recursive Case: function calls itself
Call Stack: memory stack used by computers to store variable data in different functions
Comes into play whenever function called in another function
Variables in each function call are inaccessible to other functions in stack

Graphs: Nodes connecting to whatever
Not always a starting point! Nonlinear, not always directional
Directed Graph: edges with direction
Major rules: at least one node
Singleton: graph with one node
G = (V, E), a set of vertices and set of edges
V = node, E = (node1, node2)
Edge- connection between nodes
Parentheses around edge pairs = ordered
Facebook: undirected, Twitter: directed
Path: origin node + edges to destination node
Cycle: path where starting point is ending point
Eulerian Cycle: cycle with no repeats except start
Simple Path: don't repeat edges or nodes already traversed.
Degrees- Number of a node's connections to other nodes

Memory: "drawers" with addresses (e.g. fe0ffeeb)
Array: contiguous storage
Because elements must be contiguous, adding new elements is challenging
if memory slot taken up whole array must be moved to wherever it can fit
Workaround: reserve more space (may waste memory or have to move anyway)
Strength: instant lookup, random access
Reading = O(1), Insertion = O(N), Deletion = O(N)
Linked List: items go anywhere
Strength: more manageable storage and additions
items store addresses to next item to connect
+ No need to move items!
Weakness: lookup (must start at #1 every time), sequential access
Reading = O(N), Insertion = O(1), Deletion = O(1)
Use a linked list if inserts matter more than lookup
Use an array for random access

Selection sort:
1. select the first item best meeting the criteria (O(N))
2. select the next item; do this repeatedly until none are left.
This process takes O(N^2) time

Degrees can be odd or even

To traverse an Eulerian circuit (cycle) where every path is traversed once and you end up at the same spot:

Every vertex must have an even degree

Every vertex must have more than 0 degrees

For a simple path (every edge once) either all even or two odd and the rest even

Graphs: relationships, modeling

How to traverse to get the shortest path?



np-complete: A problem with no better solution or no solution (traveling salesman)



DFS applies to graphs too

DFS: you need to read, update or sort

Keep going down left (or right)

Maybe good if you know a node is deep down



Strategy- implementation of an algorithm

DFS Strategies: all are permutations of the three things you can do at each node:

1. read it (d)

2. Look left (l)

3. look right (r)

The order of operations matters!

root 6, l4, r5, l2, r3, l1, r8, l7, r9

1. Pre order- dlr, 6421_358_7_9

2. In order- ldr, ordered list!

3. Post order- lrd, 13_25_4_79_8_6; Example: deletion, delete children first (left and right)

Time Complexity: O(n), linear

Space complexity: O(h), tree height



BFS: level by level (graphs too) or in-level order, level-order traversal

Might be better if you don't know a node's location

Discovered node: nodes referenced for future processing (includes root)

1. Read data

2. Reference discovered nodes for later reading in a queue

3. Repeat until all nodes discovered and processed

Time: O(n)

Space: O(w), width of tree

Hash Table: array + hash function

Fast searching! Constant

Function maps where data goes in array and also retrieves data quickly.

Evenly distribute things in random buckets (indices)

Buckets are unique and have unique keys

Table size affects function output

Example: remainder of book title length and array length used to determine bucket choice

Collision: when two items go to same bucket

Minimize collisions! Uneven distribution sabotages fast search

Collision resolution - different techniques

Resolution Types:

Move over to the nearest bucket: linear probing but may be slow and promote clustering

Clustering: when data in a few a buckets that are close together while rest of table empty

Chaining - restructure table so multiple elements in one key via linked list. Add onto beginning of list

Average O(1)

How to manage list size?

Hash functions should make it easy to compute fast for data insertion and retrieval (minimal collisions), handle all input data, and always return the same key when you insert an element into the same bucket

Think about hash function before allocating more buckets



Set: no duplicates, unordered collection

Intersection- shared

Union- shared and unshared

Disjunctive Union- opposite of Union

Difference / Relative complement- unshared one set

Symmetric difference- unshared of both sets

Set Theory in CS: relational databases (SQL and relational algebra based on set theory)

Time Complexity: must look at all the things

multi-set comparisons = O(n + m)

Add, remove, find = O(1)

Sets use hash tables to work

Out of place algorithm - when algorithm does operation on copy



In place- less memory, usually constant, but alters data



Sorting - organizing items by a common comparable property in order

Output is a list

A sorted list is a permutation of a list

Data must be homogeneous



Motivation: Data operations (reading and retrieval, addition, removal) are faster



6 Properties of Sorting Algorithms:

1. Time complexity

2. Space complexity

3. Stability- what if two elements are equal? Algorithms that preserve the relative order of equal elements. Stable means output guaranteed to do this. Why unstable? Because of fragmentation of datasets

4. Internal or external? - Does it use main memory (RAM) or rely on external memory?

5. Recursive or not?- d & c

6. Comparison or not?- comparison operators used? Non comparator example- radix sort (digits, not comparators)

Examples:

Selection Sort: go through items, find smallest, swap with first element, repeat

O(n²/2)



Bubble Sort- compare all adjacent elements by size; big numbers bubble up, O(n²)



Insertion sort - 2 sets: sorted and unsorted, iterates through unsorted to insert in proper place in sorted place.

2 explicit sublists (selection focuses on what item, insertion on where) place by comparing to current sorted items

O(n²)



Merge sort - splits unsorted set into halves, sorts halves, merges to whole via recursion

Divide and conquer, down to smallest subset e.g. 1 number

This smallest subset is sorted

"Conquer" aka merge into larger lists

Compare and then merge each list. If more than 1, compare 1st element of each list, then compare elements in each with pointers for each list

2 functions: mergesort and merge

O(n logn) - closer to linear than quadratic



Quick sort - divide and conquer, partition by pivot, two lists

Pivot is critical; ideal choice is median

You want a pivot near the middle, otherwise quadratic because of uneven sublists

Each list gets another pivot in the same way as the first list

Repeat until every pivot finds its place and fuse back together

Instead of new array, swap with pointers

Left pointer 1st, bigger? If not move on, if yes prepare to swap

Right next, smaller? If not move on, if yes prepare to swap

e.g. 91625

If left bigger and right smaller, swap

We want to swap smaller with bigger

21695

Now L1 R6: both good, do nothing

When pointers intersect L >= R, swap pivot with L

21596

Now 21 and 96: just swap

O(n logn to n²) n² - comparing pivot to everything else

41253 - 4 & 2 swap

21453 - 1 & 4 - good, move on

21354 - swapped pivot and 4

21, 54

1. Don't use with sorted or nearly sorted lists

2. Sort sublists in parallel (parallel in quicksort)

3. Pick a sensible median based on the data, such as picking through last several elements



Heaps: Binary tree with special rules:

1. Nodes must be arranged in specific order - based on root node. Heap Order Property: how the root node compares to other nodes. Root and all parents must be >= children or <= children in value

2. Complete shape - every level is filled with nodes before new levels get filled, and left must be filled first

(queues, trees, binary search)

Minheap - Heap with root as minimum

Maxheap

• Duplicates allowed

• Left child can be bigger than right child

Heaps - normally you grow and shrink them



Growth- insert into bottom left-most space and check value.



Maxheap- if bigger, swap with parent. Continue until smaller



Heapifying Up- swapping up with parents

Heapify down- deleting a node!

Usually deleting the root node, but you can't just delete nodes arbitrarily

Safe Spot- next bottom left-most opening

You can swap root with safe spot for deletion, then heapify node down to right place



Represent heaps as arrays- because queues and indices

Ordering- max/min value, root at 0, use index to place other nodes (parent I, child left 2i+1, right 2i+2; parent: floor of (i-1)/2 )

Priority Queue: queue with weight/ priority dictating order of dequeing

Heaps can be represented as priority queues (lookup of max or min: O(1); insertion and deletion: O(logn))



Heapsort: Sorting the nodes by finding and sorting the next-largest node repeatedly, starting with unsorted collection to make a maxheap using formulas

Starts by making binary tree and heapifies it

3 19 1 14 >

19, 14, 3, 1 (step 1)

Step 2- take values and place in array

Swap root and smallest node, then change (change index of heap)

1 14 3 19 > 14 1 3 19 > 3 114 19 (swap 14 with 3, change index) > 1 3 14 19

Heap sort is like selection sort but nlogn
An approximation of an algorithm's speed relative to the size of its input.
-The number of steps (calculations, like 2 + 2 or lookup) which must be performed to complete an algorithm based on its input 
-A basic operation takes one step
-We are mainly concerned with the worst-case scenario.

Asymptomatic Analysis: The behavior of a line graph as it approaches infinity
-Key to how time and space complexity are evaluated because larger inputs tend to be evaluated much more slowly.

Conventions:
1. Ignore constants
2. Simplify the notation to the largest and therefore slowest term

In most cases space complexity is less of a concern than time complexity, but is not irrelevant

Average cases should also be taken into account

Classifications:
Constant, O(1)
Logarithmic, O(logn) -When the input grows exponentially relative to the number of steps
Linear, O(n)
Linearithmic, O(n logn) -Characteristic of the best sorting algorithms
Quadratic, O(n^2)
Exponential, O(X^n)
Factorial, O(n!)
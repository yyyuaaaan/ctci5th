"""__author__ = 'anyu'

9.10. You have a stack of n boxes, with widths w., heights l\ and depths dr The boxes cannot be rotated and can only be
stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height,
and depth. Implement a method to build the tallest stack possible, where the heigh t of a stack is the sum of the
heights of each box.

I think you can solve this using the dynamic programming longest increasing subsequence algorithm
http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence

this is actually much easier than the original problem, because you cannot rotate boxes, and also require strictly larger:
including three dimensions, BUT selection sort is not ok, still DP problem

The adapted recurrence is: D[i] = maximum height we can obtain if the last tower must be i.

D[1] = h(1);
D[j] = h(j) + max(D[i] | i < j, we can put block j on top of block i)
for D[i] use recursion or another for loop, but in this problem, only use recursion, because i has several options

Answer is the max element of D.

"""

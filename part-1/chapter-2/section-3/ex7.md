# Q

Describe a $\Theta(n \lg n)$-time algorithm that, given a set $S$ of $n$ integers and another integer $x$, determines whether or not there exist two elements in $S$ whose sum is exactly $x$.

# A


## Solution 1.

1. Sort $S$ as an array.
2. For each element $a$ in $S$, perform binary search on the sorted array in order to find an element $b$ such that $a + b = x$.

## Solution 2. [1]

1. Sort $S$ as an array.
2. Start with $i = 0$ and $j = n - 1$ at both ends of the array.
   1. Compute $a = S[i] + S[j]$.
   2. If $a < x$, increment $i$ and try again.
   3. If $a > x$, decrement $j$ and try again.
   4. If $i$ and $j$ meet, there are no such elements.


[1] [Solution 2](https://atekihcan.github.io/CLRS/02/E02.03-07/)

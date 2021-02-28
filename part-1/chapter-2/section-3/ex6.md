# Q

Observe that the **while** loop of lines 5-7 of the Insertion-Sort procedure in Section 2.1 uses a linear search to scan (backward) through the sorted subarray $A$[1..$j-1$]. Can we use a binary search (see Exercise 2.3-5) instead to improve the overall worst-case running time of insertion sort to $\Theta(n\lg n)$?

# A

No, because we still have to move the elements when inserting.

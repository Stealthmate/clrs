# Q
# Consider sorting $n$ numbers stored in array $A$ by first finding the smallest element of $A$ and exchanging it with the element in $A$[1]. Then find the second smallest element of $A$, and exchange it with $A$[2]. Continue in this manner for the first $n - 1$ elements of $A$. Write pseudocode for this algorithm, which is known as *selection sort*. What loop invariant doesthis algorithm maintain? Why does it need to run for only the first $n - 1$ elements, rather than for all $n$ elements? Give the best-case and worst-case running times of selection sort in $\Theta$-notation.

# It needs to run only for the first n-1 elements because the last one cannot be smaller than all the others.
# Loop invariant is that on each iteration, the first i elements are the smallest elements in A, sorted in the correct order.
# Best-case time: n(n-1)/2 = O(n^2)
# Worst-case time: n(n-1)/2 = O(n^2)

def selection_sort(A):
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        t = A[min_idx]
        A[min_idx] = A[i]
        A[i] = t
    return A

print(selection_sort([3, 2, 5, 1, 4]))

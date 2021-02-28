# Q

# Referring back to the searching problem (see Exercise 2.1-3), observer that if the sequence A is sorted, we can check the midpoint of the sequence against v and eliminate half of the sequence from further consideration. The binary search algorithm repeats this procedure, halving the size of the remaining portion of the sequence each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is O(lg n).

def binary_search(A, v, l, h):
    i = (l + h) // 2
    if v == A[i]:
        return i
    if v < A[i]:
        return binary_search(A, v, l, i)
    return binary_search(A, v, i, h)

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 7, 0, 8))

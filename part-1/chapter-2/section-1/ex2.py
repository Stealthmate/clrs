# Q
# Rewrite the Insertion-Sort procedure to sort into
# nonincreasing instead of nondecreasing order.

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[0...j - 1]
        i = j - 1
        while i >= 0 and A[i] < key: # A: Change A[i] > key to A[i] < key
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

print(insertion_sort([31,41,59,26,41,58]))

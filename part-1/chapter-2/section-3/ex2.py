# Q
# Rewrite the Merge procedure so that it does not use sentinels, instead stopping once either array L or R has had all its elements copied back to A and then copying the remainder of the other array back into A.

def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = A[p + i]
    for i in range(n2):
        R[i] = A[q + i]
    i = 0
    j = 0
    k = p
    while k < r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        if i == n1 or j == n2:
            break
    while i < n1:
        A[k] = L[i]
        k += 1
        i += 1
    while j < n2:
        A[k] = R[j]
        k += 1
        j += 1
    return A

print(merge([1, 3, 5, 7, 2, 4, 6, 8], 0, 4, 8))

def merge(A, l, i, h):
    L = A[l:i]
    R = A[i:h]
    j = 0
    k = 0
    invs = 0
    for idx in range(l, h):
        if (j < len(L)) and (k == len(R) or L[j] < R[k]):
            A[idx] = L[j]
            j += 1
        else:
            A[idx] = R[k]
            invs += len(L) - j
            k += 1
    return invs

def n_inversions(A, l, h):
    n = 0
    if l < h - 1:
        i = (l + h) // 2
        n = n_inversions(A, l, i)
        n += n_inversions(A, i, h)
        n += merge(A, l, i, h)
    return n

A = [2, 3, 8, 6, 1]
print(n_inversions(A, 0, 5))
print(A)

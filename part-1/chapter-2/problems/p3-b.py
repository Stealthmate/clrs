# O(n)
def naive_exp(x, n):
    xn = 1
    for i in range(n):
        xn *= x
    return xn

# O(log n)
def efficient_exp(x, n):
    if n == 0:
        return 1
    n1 = 1
    r = 1
    if n % 2 == 0:
        r = efficient_exp(x, n // 2)
        return r * r
    else:
        r = efficient_exp(x, (n - 1) // 2)
        return r * r * x

# Assuming exponentiation is not an instruction,
# the naive method can be done in either
# 1 + 2 + 3 + ... + n = O(n^2) when using naive exponentiation
# or
# log 1 + log 2 + log 3 + ... + log n = O(log n!) = O(nlog n) (not proved here)
def naive_eval(A, x):
    v = 0
    for i in range(len(A)):
        v += naive_exp(x, i) * A[i]
        # v += efficient_exp(x, i) * A[i]
    return v

print(naive_eval([1, 2, 3], 3))

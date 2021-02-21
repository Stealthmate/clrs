"""
Q
Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n+1)-element array C. State the problem formally and write pseudocode for adding the two integers.
"""

"""
A

  Input: Two sequences of n numbers A = <a1,a2,...,an> and B = <b1,b2,...,bn> where ai, bi in {0, 1}.
  Output: A sequence of (n + 1) numbers C = <c1,c2,...,cn> which satisfies the following property:
    $\sum_{i=0}^{n + 1} c_i2^{i} = (\sum_{i=0}^{n} a_i2^{i}) + (\sum_{i=0}^{n} b_i2^{i})
"""

def add_binary_integers(A, B):
    C = [0 for _ in range(len(A) + 1)]
    carry = 0
    """
    Loop invariant:
      At the start of each iteration, C[0:i] contains the first i digits of the sum of the integers represented by A[0:i] and B[0:i], and carry represents the carry bit (the (i+1)-th digit).
    """
    for i in range(0, len(A)):
        r = A[i] + B[i] + carry
        if r <= 1:
            C[i] = r
            carry = 0
        else:
            C[i] = r % 2
            carry = 1
    C[len(A)] = carry
    return C

A = [0,1,0]
B = [1,1,1]
print(add_binary_integers(A, B))

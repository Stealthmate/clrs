"""
Q
Consider the searching problem:

  Input: A sequence of n numbers A = <a1,a2,...,an> and a value v.

  Output: An index i such that v-A[i] or the special value NIL if v does not appear in A.

Write pseudocode for linear search, which scans through the sequence, looking for v. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.
"""

def linear_search(A, v):
    """
    Loop invariant:
       At the start of each iteration, v appears in the subarray A[0:i] if and only if idx is not NIL points to the index of v in A.

    Initialization: idx = NIL and v does not appear in the (empty) subarray A[0:0].

    Maintenance: Assume v does not appear in A[0:i] and idx is NIL. idx changes its value to i + 1 only if A[i+1] = v, implying that v appears in A and vice versa.

    Termination: The loop terminates when i becomes greater than the length of A. At that point the invariant states that idx points to an element in A if and only if v appears in A.
    """
    idx = None
    for i in range(0, len(A)):
        if A[i] == v:
            idx = i
    return idx

A = [1, 2, 3, 4, 5]
print(A, 3, linear_search(A, 3))
print(A, 6, linear_search(A, 6))

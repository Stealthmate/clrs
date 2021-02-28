# Q

Use mathematical induction to show that when $n$ is an exact power of 2, the solution of the recurrence

$$
T(n) = \begin{cases}
    2 & \text{if } n = 2,\\
    2T(n/2) + n & \text{if } n = 2^k, \text{for} k > 1
\end{cases}
$$

is $T(n) = n\lg n$.

# A

For $n = n2$ we have $T(2) = 2 = 2 \lg 2$. Suppose equality holds for $n = k$ and solve for $n = 2k$.

$$
T(2k) = 2T(k) + k = 2k\lg k + 2k = 2k(\lg k + 1) = 2k(\lg k + 2\lg 2) = 2k\lg 2k
$$

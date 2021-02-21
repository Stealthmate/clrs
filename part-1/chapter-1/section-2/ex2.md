# Q

Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size $n$, insertion sort runs in $8n^2$ steps, while merge sort runs in $64n\lg n$ steps. For which values of $n$ does insertion sort beat merge sort?

# A

$$
\begin{aligned}
8n^2 &= 64n\lg n \\
n &= 8\lg n
\end{aligned}
$$

Using powers of 2 for ease of calculation, insertion sort is faster than merge sort for most $n < 64$.

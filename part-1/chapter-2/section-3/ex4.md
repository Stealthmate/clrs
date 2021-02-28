# Q

We can express insertion sort as a recursive procedure as follows. In order to sort $A$[1..$n$], we recursively sort A[1..$n-1$] and then insert $A$[n] into the sorted array $A$[1..$n-1$]. Write a recurrence for the running time of this recursive version of insertion sort.

# A

$$
T(n) = T(n - 1) + M(n) + I(n)
$$

where $M(n)$ is the time to find the place for the element and $I(n)$ is the time to insert it into the array.

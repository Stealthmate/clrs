# Q

Using Figure 2.2 as a model, illustrate the operation of Insertion-Sort on the array $A = \langle 31, 41, 59, 26, 41, 58 \rangle$.

# A

Using ^ to show current loop position.

- ^ 31,41,59,26,41,58
- 31 ^ 41,59,26,41,58
- 31,41 ^ 59,26,41,58
- 31,41,59 ^ 26,41,58
- 26,31,41,59 ^ 41,58, where 26 is swapped with 59, then 41, then 31.
- 26,31,41,41,59, ^ 58, where 41 is swapped with 59.
- 26,31,41,41,58,59 ^ , where 58 is swapped with 59.

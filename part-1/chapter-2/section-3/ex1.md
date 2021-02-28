# Q

Using Figure 2.4 as a model, illustrate the operation of merge sort on the array $A = \langle 3, 41, 52, 26, 38, 57, 9, 49 \rangle$.

# A

- 3, 41, 52, 26, 38, 57, 9, 49 -> 3, 9, 26, 38, 41, 49, 52, 57
  - 3, 41, 52, 26 -> 3, 26, 41, 52
    - 3, 41
      - 3
      - 41
    - 52, 26 -> 26, 52
      - 52
      - 26
  - 38, 57, 9, 49 -> 9, 38, 49, 57
    - 38, 57
      - 38
      0 47
    - 9, 49
      - 9
      - 47

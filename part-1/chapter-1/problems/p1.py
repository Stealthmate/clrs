# Q
# For each function $f(n)$ and time $t$ in the following table,
# determine the largest size $n$ of a problem that can be solved in time t,
# assuming the algorithm to solve the problem takes f(n) microseconds.

import numpy as np

TIMES = []
TIMES.append(1000)            # Second
TIMES.append(TIMES[-1] * 60)  # Minute
TIMES.append(TIMES[-1] * 60)  # Hour
TIMES.append(TIMES[-1] * 24)  # Day
TIMES.append(TIMES[-1] * 30)  # Month
TIMES.append(TIMES[-1] * 12)  # Year
TIMES.append(TIMES[-1] * 100) # Century

def print_row(ns):
    print("  1 second : ", ns[0])
    print("  1 minute : ", ns[1])
    print("  1 hour   : ", ns[2])
    print("  1 day    : ", ns[3])
    print("  1 month  : ", ns[4])
    print("  1 year   : ", ns[5])
    print("  1 century: ", ns[6])

def bisect_range(f, y1, low, high):
    x = (low + high) // 2
    while f(float(x)) != y1 and high - low > 1:
        if f(float(x)) < y1:
            low = x
        else:
            high = x
        x = (low + high) // 2
    return x

print("log(n)")
print_row([f"10^{int(t * np.log10(2))}" for t in TIMES])
print()

print("sqrt(n)")
print_row([t**2 for t in TIMES])
print()

print("n")
print_row(TIMES)
print()

print("nlog(n)")
print_row([bisect_range(lambda n: n * np.log2(n), t, 0, int(1e20)) for t in TIMES])
print()

print("n^2")
print_row([int(np.sqrt(t)) for t in TIMES])
print()

print("n^3")
print_row([int(np.cbrt(t)) for t in TIMES])
print()

print("2^n")
print_row([int(np.log2(t)) for t in TIMES])
print()

print("n!")
print_row([bisect_range(lambda n: np.math.factorial(n), t, 0, 20) for t in TIMES])
print()

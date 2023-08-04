import time
import numpy as np


def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


num_runs = 100
all_runtimes = []
Ns = np.array([1000, 10_000, 100_000, 1_000_000])
for N in Ns:
    numbers = list(range(N))

    runtimes = []
    for _ in range(num_runs):
        t0 = time.perf_counter()
        find_smallest(numbers)
        elapsed_time_run = time.perf_counter() - t0
        runtimes.append(elapsed_time_run)

    elapsed_time = np.mean(runtimes)
    print(f"{N:10}\t{elapsed_time:10.4f}")
    all_runtimes.append(elapsed_time)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.loglog(Ns, all_runtimes, label="Runtime")
ax.loglog(Ns, Ns * 2e-8, linestyle="--", label="$\mathcal{O}(n)$")
ax.set_xlabel("N")
ax.set_ylabel("Time [seconds]")
ax.legend()
plt.show()

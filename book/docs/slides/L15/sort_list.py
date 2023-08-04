import time
import numpy as np
import matplotlib.pyplot as plt


def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def sort_list(numbers):
    sorted_numbers = []
    N = len(numbers)
    for _ in range(N):
        smallest = find_smallest(numbers)
        sorted_numbers.append(smallest)
        numbers.remove(smallest)
    return sorted_numbers


num_runs = 100
all_runtimes = []
Ns = np.array([1000, 5_000, 10_000, 20_000])
for N in Ns:
    numbers = list(range(N))

    runtimes = []
    for _ in range(num_runs):
        t0 = time.perf_counter()
        sort_list(numbers)
        elapsed_time_run = time.perf_counter() - t0
        runtimes.append(elapsed_time_run)

    elapsed_time = np.mean(runtimes)
    all_runtimes.append(elapsed_time)
    print(f"{N:10}\t{elapsed_time:10.4f}")

fig, ax = plt.subplots()
ax.loglog(Ns, all_runtimes, label="Runtime")
ax.loglog(Ns, Ns * 1e-7, linestyle="--", label="$\mathcal{O}(n)$")
ax.loglog(Ns, Ns * Ns * 1e-10, linestyle="--", label="$\mathcal{O}(n^2)$")
ax.set_xlabel("N")
ax.set_ylabel("Time [seconds]")
ax.legend()
fig.savefig("fig/sort_list_runtime.png")
plt.show()

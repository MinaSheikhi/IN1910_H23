import typing
import time
import numpy as np
import matplotlib.pyplot as plt


def plot_run_time(f, Ns=None):

    np.random.seed(1)
    Ns = [10, 100, 1000, 10000]
    times = []
    o_n = []
    o_n2 = []
    o_n3 = []
    o_logn = []
    o_nlogn = []
    for N in Ns:
        x = np.random.randint(0, N, size=N)
        y = np.random.randint(0, N, size=N)
        t0 = time.perf_counter()
        z = f(x, y)
        t1 = time.perf_counter()
        times.append(t1 - t0)
        o_n.append(N)
        o_n2.append(N**2)
        o_n3.append(N**3)
        o_logn.append(np.log(N))
        o_nlogn.append(N * np.log(N))

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.loglog(Ns, (times[-1] / o_n[-1]) * np.array(o_n), label="O(N)")
    ax.loglog(Ns, (times[-1] / o_n2[-1]) * np.array(o_n2), label="O(N^2)")
    ax.loglog(Ns, (times[-1] / o_n3[-1]) * np.array(o_n3), label="O(N^3)")
    ax.loglog(Ns, (times[-1] / o_logn[-1]) * np.array(o_logn), label="O(log(N))")
    ax.loglog(Ns, (times[-1] / o_nlogn[-1]) * np.array(o_nlogn), label="O(Nlog(N))")

    ax.loglog(Ns, times, "k--", label="Run time")
    ax.set_xlabel("$N$")
    ax.set_ylabel("Run time [seconds]")
    ax.legend()
    plt.show()


def benchmark(
    f: typing.Callable[
        [typing.Iterable[int], typing.Iterable[int]], typing.Iterable[int]
    ]
):
    N = 5000
    np.random.seed(1234)
    x = np.random.randint(0, N, size=N)
    y = np.random.randint(0, N, size=N)
    t0 = time.perf_counter()
    f(x, y)
    t1 = time.perf_counter()
    print(f"Elsapsed time: {t1 - t0:.3f} seconds")


def find_unique_elements1(x, y):
    unique_elements = []
    for xi in x:
        for yi in y:
            if xi == yi:
                if xi not in unique_elements:
                    unique_elements.append(xi)

    return unique_elements


def find_unique_elements2(x, y):
    unique_elements = []
    for xi in x:
        if xi in y:
            if xi not in unique_elements:
                unique_elements.append(xi)

    return unique_elements


def main():
    # benchmark(find_unique_elements2)
    plot_run_time(find_unique_elements2)


if __name__ == "__main__":
    main()

# import ctypes

# library = ctypes.CDLL("estimate_pi_cpp.so")
# library.print_hello()


# library = ctypes.CDLL("estimate_pi_c.so")
# # func = library.print_hello
# func = library.estimate_pi

# func.argtypes = [ctypes.c_long]
# func.restype = ctypes.c_double

# print(func(1000))
# # breakpoint()

import typing

import numpy as np
import time

import numba
import ctypes

# import cppyy
import pyjion

pyjion.enable()

# c_library = ctypes.CDLL("estimate_pi_c.so")

# c_library.estimate_pi.argtypes = [ctypes.c_uint]
# c_library.estimate_pi.restype = ctypes.c_double


# cpp_library = ctypes.CDLL("estimate_pi_cpp.so")

# cpp_library.estimate_pi.argtypes = [ctypes.c_uint]
# cpp_library.estimate_pi.restype = ctypes.c_double

# cppyy.include("cmath")
# cppyy.cppdef(
#     """
# double estimate_pi(unsigned int N)
# {
#     double pi_fourth = 0.0;
#     for (unsigned int i = 0; i < N; i++)
#     {
#         pi_fourth += std::pow(-1, i) * 1.0 / (2.0 * i + 1.0);
#     }
#     return 4.0 * pi_fourth;
# }
# """
# )

# from cppyy.gbl import estimate_pi as estimate_pi_cppyy


class BenchmarkResults(typing.NamedTuple):
    values: list[float]
    times: list[float]
    name: str
    number: int = 1

    @property
    def mean(self) -> float:
        return np.mean(self.times)

    @property
    def std(self) -> float:
        return np.std(self.times)

    @property
    def repeats(self) -> int:
        return len(self.times)

    @property
    def best(self) -> float:
        return np.min(self.times)

    def print(self):
        print(
            f"{self.name}: mean: {self.mean}, std: {self.std}, best: {self.best}"
            f"with {self.number} runs and {self.repeats} repeats"
        )


def benchmark(f: typing.Callable[[int], float]):
    times = []
    values = []
    N = 1_000_000
    num_repeats = 5
    num_runs = 2
    for _ in range(num_repeats):
        t0 = time.perf_counter()
        for _ in range(num_runs):
            pi = f(N)
        times.append(time.perf_counter() - t0)
        values.append(pi)

    return BenchmarkResults(
        values=values, times=times, name=f.__name__, number=num_runs
    )


# # @profile
def estimate_pi_v2(N):
    return sum((-1.0) ** n / (2.0 * n + 1.0) for n in range(N)) * 4


def estimate_pi_v1(N):
    pi_forth = 0.0
    for n in range(N):
        pi_forth += (-1.0) ** n / (2.0 * n + 1.0)
    return pi_forth * 4
    # return sum((-1.0) ** n / (2.0 * n + 1.0) for n in range(N)) * 4


def estimate_pi_numpy(N):
    sign = np.ones((N,))
    sign[1::2] = -1
    i = np.arange(N)

    return 4 * np.sum(sign * (1 / (2 * i + 1)))


def estimate_pi_c(N):
    return c_library.estimate_pi(N)


def estimate_pi_cpp(N):
    return cpp_library.estimate_pi(N)


@numba.jit
def estimate_pi_numba(N):
    sign = np.ones((N,))
    sign[1::2] = -1
    i = np.arange(N)

    return 4 * np.sum(sign * (1 / (2 * i + 1)))


@numba.njit
def estimate_pi_numba_njit(N):
    sign = np.ones((N,))
    sign[1::2] = -1
    i = np.arange(N)

    return 4 * np.sum(sign * (1 / (2 * i + 1)))


#     pi_fourth = 1
#     for i in range(1, N):
#         sign = -(2 * (i % 2) - 1)
#         pi_fourth += sign * 1 / (2 * i + 1)
#     return 4 * pi_fourth


def analyze_profile():
    import pstats

    stats = pstats.Stats("estimate_pi.cprof")
    stats.sort_stats(pstats.SortKey.TIME).print_stats(5)
    stats.sort_stats(pstats.SortKey.CALLS).print_stats(5)

    # breakpoint()


def main():
    res = benchmark(estimate_pi_v1)
    res.print()
    print(res.values)
    # breakpoint()


def summary():

    data = {
        "python_v1": 0.2276,
        "python_v2": 0.2198,
        "numpy": 0.008878,
        "mypyc": 0.2313,
        "numba": 0.00622,
        "pypy": 0.198,
        "ren c++": 0.0102,
        "C utvidelse": 0.008065,
        "C utvidelse (Ofast)": 0.007690,
        "C++ utvidelse": 0.009439,
        "cppyy": 0.006816,
    }

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(data.keys(), data.values())
    ax.set_yscale("log")
    ax.grid()
    ax.set_xticklabels(data.keys(), rotation=30)
    ax.set_ylabel("Execution time [seconds]")
    fig.savefig("summary.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
    # analyze_profile()
    # summary()

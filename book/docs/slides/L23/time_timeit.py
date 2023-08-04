import typing
import numpy as np
import timeit


def slow_sum(x: typing.Iterable[float]) -> float:
    s = 0
    for xi in x:
        s += xi
    return s


def fast_sum(x: typing.Iterable[float]) -> float:
    return np.sum(x)


if __name__ == "__main__":
    x = np.arange(10000000)

    # res1 = timeit.repeat("slow_sum(x)", number=2, repeat=3, globals=globals())
    # res2 = timeit.repeat("fast_sum(x)", number=2, repeat=3, globals=globals())
    # breakpoint()

    # res1 = benchmark(slow_sum, num_runs=2, num_repeats=2)
    # res2 = benchmark(fast_sum, num_runs=2, num_repeats=2)
    # res1.print()
    # res2.print()
    # assert res1.value == res2.value

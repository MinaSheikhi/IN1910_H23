import typing
import numpy as np
import time


class BenchmarkResults(typing.NamedTuple):
    value: float
    number: int
    times: list[int]
    name: str

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


def slow_sum(x: typing.Iterable[float]) -> float:
    s = 0
    for xi in x:
        s += xi
    return s


def fast_sum(x: typing.Iterable[float]) -> float:
    return np.sum(x)


def benchmark(
    f: typing.Callable[[typing.Iterable[float]], float],
    number: int = 1,
    repeats: int = 1,
) -> BenchmarkResults:
    x = np.arange(10000000)
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        for _ in range(number):
            y = f(x)

        times.append((time.perf_counter() - t0))

    return BenchmarkResults(value=y, times=times, number=number, name=f.__name__)


if __name__ == "__main__":

    res1 = benchmark(slow_sum, number=2, repeats=2)
    res2 = benchmark(fast_sum, number=2, repeats=2)
    res1.print()
    res2.print()
    assert res1.value == res2.value

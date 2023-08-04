import numpy as np
import time


class DrukardsWalk:
    def __init__(self, home: int, start: int = 0, N=1000) -> None:
        self._position = start
        self._home = home
        self._history = [start]
        self._N = N
        self._make_steps()

    def _make_steps(self):
        self._steps = 2 * np.random.randint(2, size=self._N) - 1
        self._n = 0

    def step(self) -> None:
        if self._n >= self._N:
            self._make_steps()

        self._position += self._steps[self._n]
        self._n += 1
        self._history.append(self.position)

    def is_home(self) -> bool:
        return self._home == self._position

    @property
    def position(self) -> int:
        return self._position

    @property
    def history(self) -> tuple[int, ...]:
        return tuple(self._history)

    @property
    def num_steps(self) -> int:
        return len(self._history)

    def walk_home(self) -> None:
        while not self.is_home():
            self.step()


def benchmark():
    np.random.seed(1)
    drukard = DrukardsWalk(100)
    drukard.walk_home()


def main():
    t0 = time.perf_counter()
    N = 20
    for _ in range(N):
        benchmark()
    print(f"Elapsed time: {(time.perf_counter() - t0)} seconds")


if __name__ == "__main__":
    main()
    # benchmark()

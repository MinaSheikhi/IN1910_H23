import time

# import typing


def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


t0 = time.time()
fib(32)
print(time.time() - t0)

# def estimate_pi(N: int) -> float:
#     pi_forth: float = 0.0
#     for n in range(N):
#         pi_forth += (-1.0) ** n / (2.0 * n + 1.0)
#     return pi_forth * 4.0


# def benchmark(f: typing.Callable[[int], float]):
#     times = []
#     values = []
#     N = 1_000_000
#     num_repeats = 5
#     num_runs = 2
#     for _ in range(num_repeats):
#         t0 = time.perf_counter()
#         for _ in range(num_runs):
#             pi = f(N)
#         times.append(time.perf_counter() - t0)
#         values.append(pi)

#     print(times)


# benchmark(estimate_pi)

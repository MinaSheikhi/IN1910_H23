import time
import concurrent.futures
import numpy as np
import numba


def take_time(f):
    def wrap(*args, **kwargs):
        t0 = time.perf_counter()
        f(*args, **kwargs)
        print(f"Elapsed time: {time.perf_counter() - t0} seconds")

    return wrap


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


@take_time
def serial(number):
    print("Serial")
    results = []
    for number in number:
        result = is_prime(number)
        results.append((number, result))

    for number, result in results:
        print(f"{number} is prime: {result}")


@take_time
def threads(numbers):
    print("\nRunning multithreading")
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number in numbers:
            future = executor.submit(is_prime, number)
            results.append((number, future))

    for number, future in results:
        print(f"{number} is prime: {future.result()}")


@take_time
def processes(numbers):
    print("\nRunning multiprocessing")
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number in numbers:
            future = executor.submit(is_prime, number)
            results.append((number, future))

    for number, future in results:
        print(f"{number} is prime: {future.result()}")


@numba.njit()
def is_prime_numba(n):
    prime = True
    if n % 2 == 0:
        prime = False

    for i in range(3, n):
        if n % i == 0:
            prime = False
    return prime


@numba.jit(parallel=True)
def fun(numbers, results):
    n = len(numbers)
    for i in numba.prange(n):
        number = numbers[i]
        results[i] = is_prime_numba(number)


@take_time
def run_numba(numbers):
    results = np.empty(len(numbers), dtype=bool)
    fun(np.array(numbers), results)

    for number, result in zip(numbers, results):
        print(f"{number} is prime: {result}")


def main():
    numbers = [
        13466917,
        20996011,
        24036583,
        25964951,
        25964953,
        30402457,
        32582657,
        37156667,
        37156669,
        10002847,
        10001209,
    ]

    # serial(numbers)
    # threads(numbers)
    # processes(numbers)
    run_numba(numbers)


if __name__ == "__main__":
    main()

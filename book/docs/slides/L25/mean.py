import numpy as np
import dask.array as da
import time


def take_time(f):
    def wrap(*args, **kwargs):
        t0 = time.perf_counter()
        f(*args, **kwargs)
        print(f"Elapsed time: {time.perf_counter() - t0} seconds")

    return wrap


@take_time
def main_numpy():
    x1 = np.random.normal(10, 0.1, size=(20000, 20000))
    x1.mean()


@take_time
def main_dask():
    x1 = da.random.normal(10, 0.1, size=(20000, 20000))
    x1.mean().compute()


if __name__ == "__main__":
    main_dask()

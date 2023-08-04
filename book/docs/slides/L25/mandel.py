from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
import time
import concurrent.futures
import numba
import subprocess as sp


def take_time(f):
    def wrap(*args, **kwargs):
        for _ in range(4):
            t0 = time.perf_counter()
            ret = f(*args, **kwargs)
            print(f"{f.__name__}: Elapsed time: {time.perf_counter() - t0} seconds")
        return ret

    return wrap


@take_time
def mandelbrot_cpp():
    sp.run(["c++", "mandel.cpp", "-o", "mandel", "-std=c++14"])
    sp.run(["./mandel"])


@take_time
def mandelbrot_cpp_O3():
    sp.run(["c++", "mandel.cpp", "-o", "mandel", "-std=c++14", "-O3"])
    sp.run(["./mandel"])


@take_time
def mandelbrot_cpp_Ofast():
    sp.run(["c++", "mandel.cpp", "-o", "mandel", "-std=c++14", "-Ofast"])
    sp.run(["./mandel"])


@take_time
def mandelbrot_cpp_Ofast():
    sp.run(["c++", "mandel.cpp", "-o", "mandel", "-std=c++14", "-O3", "-fopenmp"])
    sp.run(["./mandel"])


@take_time
def mandelbrot_cpp_O3_omp():
    sp.run(
        [
            "/opt/homebrew/opt/llvm/bin/clang++",
            "mandel.cpp",
            "-o",
            "mandel",
            "-std=c++14",
            "-O3",
            "-fopenmp",
        ]
    )
    sp.run(["./mandel"])


def mandelbrot_pixel_python(c: complex, maxiter: int) -> int:
    """Check wether a single pixel diverges"""
    z = 0

    for n in range(maxiter):
        z = z * z + c
        if abs(z) > 2:
            return n

    return 0


@take_time
def mandelbrot_image_python(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
) -> np.ndarray:
    """Render an image of the Mandelbrot set"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            c = xi + 1j * yj
            img[i, j] = mandelbrot_pixel_python(c, maxiter)

    return img


def task(xi, y, maxiter):
    result = np.zeros_like(y)
    for j, yj in enumerate(y):
        c = xi + 1j * yj
        result[j] = mandelbrot_pixel_python(c, maxiter)
    return result


@take_time
def mandelbrot_image_mp(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
) -> np.ndarray:
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i, xi in enumerate(x):
            result = executor.submit(task, xi, y, maxiter)
            results.append((i, result))

    for i, value in results:
        img[i, :] = value.result()

    return img


@take_time
def mandelbrot_image_numpy(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
) -> np.ndarray:
    x = np.linspace(xmin, xmax, num=width).reshape((1, width))
    y = np.linspace(ymin, ymax, num=height).reshape((height, 1))
    C = np.tile(x, (height, 1)) + 1j * np.tile(y, (1, width))

    Z = np.zeros((height, width), dtype=complex)
    M = np.ones((height, width), dtype=bool)
    M_tmp = np.ones((height, width), dtype=bool)
    img = np.zeros((height, width), dtype=float)
    for i in range(maxiter):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        M_tmp = ~M & ~M_tmp
        img[~M_tmp] = i
        M_tmp[:] = M[:]

    img[np.where(img == maxiter - 1)] = 0
    return img.T


@numba.njit
def mandelbrot_pixel_numba(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z * z + c
        if abs(z) > 2:
            return n
    return 0


@numba.jit
def mandelbrot_pixel_numba_opt(cx, cy, maxiter):
    x = cx
    y = cy
    for n in range(maxiter):
        x2 = x * x
        y2 = y * y
        if x2 + y2 > 4.0:
            return n
        y = 2 * x * y + cy
        x = x2 - y2 + cx
    return 0


@take_time
@numba.njit
def mandelbrot_image_numba(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            # c = x[i] + 1j * y[j]
            # img[i, j] = mandelbrot_pixel_numba(c, maxiter)
            img[i, j] = mandelbrot_pixel_numba_opt(x[i], y[j], maxiter)
    return img


@take_time
@numba.njit(parallel=True)
def mandelbrot_image_parallel_numba(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in numba.prange(width):
        for j in range(height):
            img[i, j] = mandelbrot_pixel_numba_opt(x[i], y[j], maxiter)
    return img


import cppyy

cppyy.cppdef(
    """
int mandelbrot_pixel(double cx, double cy, int maxiter) {
    double x = cx;
    double y = cy;

    for (int n = 0; n < maxiter; n++) {
        double x2 = x * x;
        double y2 = y * y;

        if (x2 + y2 > 4.0) {
            return n;
        }

        y = 2 * x * y + cy;
        x = x2 - y2 + cx;
    }
    return 0;
}

void mandelbrot(int *output, double xmin, double xmax, double ymin, double ymax, int width,
                int height, int maxiter)
{
    int i, j;

    double xlin[width];
    double ylin[height];
    double dx = (xmax - xmin) / width;
    double dy = (ymax - ymin) / width;

    for (i = 0; i < width; i++) {
        xlin[i] = xmin + i * dx;
    }

    for (j = 0; j < height; j++) {
        ylin[j] = ymin + j * dy;
    }

    for (i = 0; i < width; i++) {
        for (j = 0; j < height; j++) {
            output[i * height + j] = mandelbrot_pixel(xlin[i], ylin[j], maxiter);
        }
    }
}

"""
)


from cppyy.gbl import mandelbrot as _mandelbrot_cppy


@take_time
def mandelbrot_image_cppyy(
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
    width: int,
    height: int,
    maxiter: int,
):
    img = np.zeros((width, height), dtype=np.int32)
    # img = np.zeros(width * height, dtype=np.int32)
    _mandelbrot_cppy(img, xmin, xmax, ymin, ymax, width, height, maxiter)
    return img


def benchmark(
    mandelbrot: Callable[[float, float, float, float, int, int, int], np.ndarray]
) -> np.ndarray:
    xmin = -0.74877
    xmax = -0.74872
    ymin = 0.065053
    ymax = 0.065103
    pixels = 1000
    maxiter = 2048
    return mandelbrot(xmin, xmax, ymin, ymax, pixels, pixels, maxiter)


def summary():

    data = {
        "python": 107.19,
        "mp": 14.82,
        "numpy": 21.18,
        "numba": 2.11,
        "numba (opt)": 1.96,
        "ren c++": 4.89,
        "cppyy": 1.96,
        "C++ (O3)": 0.20,
        "C++ (OpenMP)": 0.6,
        "numba (parallel)": 0.38,
    }

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(data.keys(), data.values())
    ax.set_yscale("log")
    ax.grid()
    ax.set_xticklabels(data.keys(), rotation=30)
    ax.set_ylabel("Execution time [seconds]")
    fig.savefig("summary.png", bbox_inches="tight")


def main():

    img = benchmark(mandelbrot_image_parallel_numba)
    fig, ax = plt.subplots(dpi=100)
    ax.imshow(img.T, cmap="hot", origin="lower")
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    # main()
    # mandelbrot_cpp()
    # mandelbrot_cpp_O3()
    # mandelbrot_cpp_Ofast()
    # mandelbrot_cpp_O3_omp()
    summary()

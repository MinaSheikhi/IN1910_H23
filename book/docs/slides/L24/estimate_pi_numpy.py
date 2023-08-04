# estimate_pi_numpy.py
import numpy as np


def estimate_pi(N):
    sign = np.empty((N,))
    sign[::2] = 1
    sign[1::2] = -1
    i = np.arange(N)

    return 4 * np.sum(sign * (1 / (2 * i + 1)))


if __name__ == "__main__":
    import sys

    N = int(sys.argv[1])
    print(f"\u03C0 = {estimate_pi(N)}")

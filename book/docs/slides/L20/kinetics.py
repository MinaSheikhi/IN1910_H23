import matplotlib.pyplot as plt
import numpy as np


def first_order(k, A0=1):
    """A -> B"""
    A = lambda t: A0 * np.exp(-k * t)
    B = lambda t: A0 - A(t)
    return A, B


def competing(k1, k2, A0=1):
    """A -> B & A -> C"""
    k = k1 + k2
    A = lambda t: A0 * np.exp(-k * t)
    B = lambda t: k1 / k * (A0 - A(t))
    C = lambda t: k2 / k * (A0 - A(t))
    return A, B, C


def consecutive(k1, k2, A0=1):
    """A -> B -> C"""
    dk = k2 - k1
    A = lambda t: A0 * np.exp(-k1 * t)
    B = lambda t: A0 * k1 / dk * (np.exp(-k1 * t) - np.exp(-k2 * t))
    C = lambda t: A0 - A0 / dk * (k2 * np.exp(-k1 * t) - k1 * np.exp(-k2 * t))
    return A, B, C


def equilibrium(k1, k_1, k2, A0=1):
    """A <-> B -> C"""
    k1k2 = k1 * k2
    k = k1 + k_1 + k2
    a = 0.5 * (k + np.sqrt(k * k - 4 * k1k2))
    b = k - a

    e_a = lambda t: A0 / (b - a) * np.exp(-a * t)
    e_b = lambda t: A0 / (a - b) * np.exp(-b * t)

    A = lambda t: (k_1 + k2 - a) * e_a(t) + (k_1 + k2 - b) * e_b(t)
    B = lambda t: k1 * (e_a(t) + e_b(t))
    C = lambda t: A0 - k1k2 / a * e_a(t) - k1k2 / b * e_b(t)
    return A, B, C


def plot(c, X, title):
    Nt = len(c)
    t = np.linspace(0, Nt, 250)
    n = np.arange(Nt)
    colors = ["CornflowerBlue", "Khaki", "SeaGreen", "Orchid"]
    species = "ABCD"
    plt.figure(figsize=(15, 5))
    plt.title(title, fontsize=15)
    for i in range(len(X)):
        plt.plot(t, X[i](t), color=colors[i], lw=5, alpha=0.5)
    for i in range(len(X)):
        plt.scatter(n, c[:, i], c=colors[i], label=species[i], ec="black", lw=1)
    plt.legend()
    plt.xlabel("time step")
    plt.ylabel("concentration fraction")
    plt.tight_layout()
    plt.show()
    print()  # hack for slides

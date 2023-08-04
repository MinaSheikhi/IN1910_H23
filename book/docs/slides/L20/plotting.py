from matplotlib.colors import LogNorm
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

plt.rc("axes", labelsize=14)
plt.rc("legend", fontsize=10)


def transitions(M, title, step=1):
    fig = plt.figure(figsize=(15, 5))
    P = M.copy()
    P[P == 0] = np.nan
    matrix = plt.imshow(P, cmap="plasma")
    bar = plt.colorbar(matrix)
    bar.ax.set_ylabel(r"$P(i | j)$")
    plt.xlabel("$j$")
    plt.ylabel("$i$")
    ticks = np.arange(1, len(M) + 1, step, dtype=int)
    pos = np.arange(0, len(M), step, dtype=int)
    plt.xticks(pos, ticks)
    plt.yticks(pos, ticks)
    plt.title(title)
    plt.tight_layout()
    plt.show()
    print()  # fix for slides


def states(density, states, statelabel, vmin=1e-9, vmax=1, step=1):
    S = len(states)
    density[density == 0] = np.nan
    fig = plt.figure(figsize=(15, 5))
    cax = plt.imshow(density.T, cmap="plasma", norm=LogNorm(vmin=vmin, vmax=vmax))
    plt.yticks(np.arange(0, S, step), states[::step])
    bar = fig.colorbar(cax)
    bar.ax.set_ylabel(r"state density")
    plt.xlabel("$n$")
    plt.ylabel(statelabel)
    plt.tight_layout()
    plt.show()
    print()  # fix for slides

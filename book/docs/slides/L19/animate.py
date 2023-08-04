from matplotlib.animation import FuncAnimation
from matplotlib.colors import TABLEAU_COLORS
import matplotlib.pyplot as plt
import numpy as np


class RandomWalk:
    def __init__(self, r, figsize=(10, 10), rms=False):
        self.rms = rms
        R = np.array(r)
        self.r = R if len(R.shape) > 2 else np.array([R])
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.colors = list(TABLEAU_COLORS.values())
        self.color = "black"
        if self.K > len(self.colors):
            self.colors = ["black"] * self.K
            self.color = "crimson"

    def init(self):
        self.lines = []
        self.points = []
        if self.rms:
            theta = np.linspace(0, 2 * np.pi, 250)
            self.x = np.cos(theta)
            self.y = np.sin(theta)
            (self.circle,) = self.ax.plot(self.x, self.y, c=self.color, lw=2)
        for k in range(self.K):
            c = self.colors[k]
            (line,) = self.ax.plot(self.r[k, 0, 0], self.r[k, 0, 1], alpha=0.25, c=c)
            (point,) = self.ax.plot(self.r[k, 0, 0], self.r[k, 0, 1], "o", c=c)
            self.lines.append(line)
            self.points.append(point)
        self.ax.set_xlim(self.r.min() - 1, self.r.max() + 1)
        self.ax.set_ylim(self.r.min() - 1, self.r.max() + 1)
        self.ax.set_xlabel("$x$", fontsize=14)
        self.ax.set_ylabel("$y$", fontsize=14)
        return (self.lines, self.points)

    def frame(self, idx):
        n = idx + 1
        if self.rms:
            r = np.sqrt(n)
            self.circle.set_xdata(r * self.x)
            self.circle.set_ydata(r * self.y)
        for k in range(self.K):
            self.lines[k].set_xdata(self.r[k, 0 : n + 1, 0])
            self.lines[k].set_ydata(self.r[k, 0 : n + 1, 1])
            self.points[k].set_xdata(self.r[k, n, 0])
            self.points[k].set_ydata(self.r[k, n, 1])
        return (self.lines, self.points)

    def video(self, repeat=False, speed=100):
        animation = FuncAnimation(
            self.fig,
            self.frame,
            init_func=self.init,
            interval=speed,
            frames=self.N - 1,
            repeat=repeat,
            cache_frame_data=False,
        )
        plt.close()
        return animation.to_html5_video()

    @property
    def K(self):
        return self.r.shape[0]

    @property
    def N(self):
        return self.r.shape[1]


class Diffusion:
    def __init__(self, X, figsize=(15, 5), D=0.5, y_max=0.5, dx=1):
        self.D = D
        self.X = np.array(X)
        self.y_max = y_max
        self.x_max = int(max(-self.X.min(), self.X.max()))
        self.bins = np.arange(-self.x_max, self.x_max + 2, dx)
        self.x = np.linspace(-self.x_max, self.x_max, 250)
        self.fig, self.ax = plt.subplots(figsize=figsize)

    def rho(self, t):
        c = 4 * self.D * t
        xx = self.x * self.x
        return 1 / np.sqrt(np.pi * c) * np.exp(-xx / c)

    def init(self):
        _, _, self.hist = self.ax.hist(
            self.X[:, 0],
            self.bins,
            density=True,
            align="left",
            facecolor="Gainsboro",
            edgecolor="black",
            stacked=True,
        )
        y = np.zeros(len(self.x)) + np.nan
        (self.line,) = self.ax.plot(self.x, y, color="crimson")
        self.ax.set_xlim(-self.x_max, self.x_max)
        self.ax.set_ylim(0, self.y_max)
        self.ax.set_xlabel("$x$", fontsize=14)
        self.ax.set_ylabel(r"$\rho$", fontsize=14)
        return (self.hist, self.line)

    def frame(self, idx):
        t = idx + 1
        Ns, _ = np.histogram(self.X[:, t], self.bins, density=True)
        for n, patch in zip(Ns, self.hist.patches):
            patch.set_height(n)
        self.line.set_ydata(self.rho(t))
        return (self.hist, self.line)

    def video(self, repeat=False, speed=100):
        animation = FuncAnimation(
            self.fig,
            self.frame,
            init_func=self.init,
            interval=speed,
            frames=self.X.shape[1] - 1,
            repeat=repeat,
            cache_frame_data=False,
        )
        plt.close()
        return animation.to_html5_video()

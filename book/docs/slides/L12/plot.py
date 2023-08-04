import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("output.txt")
t, v, y = d.T

fig, ax = plt.subplots()
(l1,) = ax.plot(t, v)
ax2 = ax.twinx()
(l2,) = ax2.plot(t, y, color="r")
ax.legend([l1, l2], ["Velocity", "Position"])
plt.show()

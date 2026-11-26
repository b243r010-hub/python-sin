import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")
plt.title("Sin seigenha-")
plt.xlabel("x [rad]")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

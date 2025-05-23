import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_facecolor('green')

# Define the fern leaf using a variation of Barnsley's fern (IFS fractal)
def barnsley_fern(n_points=100000):
    x = np.zeros(n_points)
    y = np.zeros(n_points)
    
    for i in range(1, n_points):
        r = np.random.random()
        if r < 0.01:
            x[i] = 0
            y[i] = 0.16 * y[i-1]
        elif r < 0.86:
            x[i] = 0.85 * x[i-1] + 0.04 * y[i-1]
            y[i] = -0.04 * x[i-1] + 0.85 * y[i-1] + 1.6
        elif r < 0.93:
            x[i] = 0.2 * x[i-1] - 0.26 * y[i-1]
            y[i] = 0.23 * x[i-1] + 0.22 * y[i-1] + 1.6
        else:
            x[i] = -0.15 * x[i-1] + 0.28 * y[i-1]
            y[i] = 0.26 * x[i-1] + 0.24 * y[i-1] + 0.44
    return x, y

# Generate fern leaf points
x, y = barnsley_fern(100000)

# Plot using only dots
ax.plot(x, y, 'g.', markersize=0.2)

# Remove axes and style
ax.axis('off')
plt.title("Fern Leaf — Created with Math & Dots 🌿", fontsize=14)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(1, 1e4, 1000)

# Calculate y values for both functions
y1 = 0.2 * x
y2 = x**0.99

# Plot the functions
plt.plot(x, y1, label='0.2x')
plt.plot(x, y2, label='x^0.99')

# Highlight the region where 0.2x > x^0.99
plt.fill_between(x, y1, y2, where=(y1 > y2), color='green', alpha=0.3)

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of 0.2x and x^0.99')
plt.legend()

# Show plot
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.yscale('log')  # Use logarithmic scale for y-axis
plt.grid(True, which="both", ls="--")  # Add grid lines
plt.show()

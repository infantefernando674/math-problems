import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Squared X Values')
plt.show()

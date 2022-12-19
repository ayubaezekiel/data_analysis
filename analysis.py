#plot a matpotlib graph with random data
import matplotlib.pyplot as plt
import numpy as np
import random

#generate random data
x = np.arange(0, 10, 0.2)
y = np.sin(x)
z = np.cos(x)

#plot the data
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos')
plt.legend()
plt.show()

# Path: analysis.py
#plot a matpotlib graph with random data

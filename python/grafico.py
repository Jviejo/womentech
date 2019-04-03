import numpy as np
import matplotlib.pyplot as plt
N = 10
x = range(1, N+1)
y = np.random.rand(N) * 10000 + 3000
plt.barh(x, y)
plt.show()


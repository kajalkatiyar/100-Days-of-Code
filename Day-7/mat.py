import matplotlib.pyplot as plt
import numpy as np

a=np.array([[10,70,60,40],[0,19,24,38],[10,50,16,75]])
plt.imshow(a)
plt.colorbar(orientation='vertical')
plt.show()
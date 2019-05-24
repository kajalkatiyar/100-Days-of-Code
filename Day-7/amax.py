#2-D array. Print max from axis 0 and min from axis 1.
#axis 0 = 1st column
#axis 1 = 1st row

import numpy as np
a=np.array([[34,43,73],[82,22,12],[53,94,66]])
print(a)

max=np.amax(a,0)
print("Max from axis 0:",max)

min=np.amin(a,1)
print("Min from axis 1:",min)

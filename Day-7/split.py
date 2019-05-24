#Create an 8X3 integer array from a range between 10 to 34 such 
#that the difference between each element is 1 and then 
#Split the array into four equal-sized sub-arrays.

import numpy as np

a=np.arange(10,34,1)
a=a.reshape(8,3)
print(a)

b=np.split(a,4)
print(b)
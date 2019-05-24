 # Create a 4X2 integer array and Prints its attributes
# Note: element must be a type of unsigned int16. And print the following Attributes: –

# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.

import numpy as np

a=np.empty([4,2],dtype=np.uint16)
print("Printing array:")
print(a)
print("Array shape:",a.shape)
print("Array dim.:",a.ndim)
print("Length of each elements:",a.itemsize)
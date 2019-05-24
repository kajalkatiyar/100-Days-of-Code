#Sort following NumPy array
#7.1- by the second row and
#7.2-by the second column

import numpy as np
a=np.array([[34,43,73],[82,22,12],[53,94,66]])
print(a)

ar=a[:,a[1,:].argsort()]
print("Sort by 2nd row:\n",ar)

ac=a[a[:,1].argsort()]
print("Sort by 2nd col.:\n",ac)
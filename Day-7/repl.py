import numpy as np
a = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
n = np.array([[10,10,10]])
print("Actual:\n",a)
print("New array:\n",n)

a = np.delete(a,1,axis=1)
print("After deleting:\n",a)

a=np.insert(a,1,n,axis=1)
print("After inserting col 2 on axis 1:\n",a)

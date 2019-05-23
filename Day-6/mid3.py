a=input("Enter string:")
if len(a)%2 != 0:
	mid=int(len(a)/2)
	m3=a[mid-1:mid+2]
	print(m3)
else:
	print("Be ODD in length ;-)")
	
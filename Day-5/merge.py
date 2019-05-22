def mergelist(l1,l2):
	l3=[]
	for num in l1:
		if(num%2 != 0):
			l3.append(num)
	for num in l2:
		if(num%2 == 0):
			l3.append(num)
	return l3
print("merged list:")
l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 3, 1]
print("List 1:",l1)
print("List 2:",l2)
print(mergelist(l1,l2))
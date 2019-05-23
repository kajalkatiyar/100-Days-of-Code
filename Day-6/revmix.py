# String s1 and s2 is balanced if all the chars in the string1 are there in s2.
# Characters position doesn’t matter.

a=input("Enter string to be checked:")
b=input("Enter ultimate string:")
y=0
n=0
l1=int(len(a))
for char in a:
	if char in b:
		y+=1
	else:
		n+=1
if n in range(1,int(len(a)+1)):
	print("Not a match!")
else:
	print("Yessss...all exist")
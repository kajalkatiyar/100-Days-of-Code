#Given an input string Count all lower case, upper case, digits, and special symbols

a=input("Enter string:")
low=[]
up=[]
num=[]
sym=[]
lc=0
uc=0
numb=0
sy=0
for char in a:
	if char.islower():
		low.append(char)
		lc+=1
	elif char.isupper():
		up.append(char)
		uc+=1
	elif char.isnumeric():
		num.append(char)
		numb+=1
	else:
		sym.append(char)
		sy += 1
print("Lower case:",low,"=",lc)
print("Upper case:",up,"=",uc)
print("Number:",num,"=",numb)
print("Symbol:",sym,"=",sy)
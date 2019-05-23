#Given an input string, count occurrences of all characters within a string
a=input("Enter string:")
c=dict()
for char in a:
	count=a.count(char)
	c[char]=count
print(c)
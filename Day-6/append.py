s1=input("Enter string 1:")
s2=input("Enter string 2:")
n=int(len(s1)/2)
m3=s1[:n:]+s2+s1[n-1:]
print(m3)
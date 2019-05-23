s1=input("Enter string:")
s2=input("Enter string:")

l1=int(len(s1))
l2=int(len(s2))

ms=s1[:1]+s2[:1]+s1[int(l1/2):int(l1/2)+1]+s2[int(l2/2):int(l2/2)+1]+s1[l1-1]+s2[l2-1]
print(ms)
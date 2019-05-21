w="bottle"
num=int(input("Enter no. of beer bottles you guys have:"))
for beer in range(num,0,-1):
	print(beer,w,"of beer on the wall")
	print(beer,w,"of beer.")
	print("Take only one \nPass it around.\n")
	if beer==1:
		print("No more bottle of beer on the wall.")
	else:
		new=beer-1
		if new==1:
			w="bottle"
		print(new,w,"of beer on the wall.")
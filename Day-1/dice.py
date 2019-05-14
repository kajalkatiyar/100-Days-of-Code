import secrets
import time

print("Rolling the dice...")
time.sleep(1)
foo=[1,2,3,4,5,6]
roll="yes"
while roll=="yes" or roll=="y":
	print(secrets.choice(foo))
	roll=input("Roll dice again?\n")
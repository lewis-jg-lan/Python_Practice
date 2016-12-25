#encoding=utf-8

import sys
print(sys.version)

#The first method
print("\n")
for i in range(1,10):
	for j in range(1,10):
		print("%d*%d=%2d " % (i,j,i*j),end="")
	print("")


#The second method
print("\n")
for i in range(1,10):
	for j in range(i,10):
		print("%d*%d=%2d" % (i,j,i*j),end=" ")
	print("")

#The third method	
print("\n")
for i in range(1,10):
	for k in range(1,i):
		print(end = "       ")
	for j in range(i,10):
		print("%d*%d=%2d" % (i,j,i*j),end=" ")
	space = (" ")
	print(space[0])


#The fourth method
print("\n")
for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%2d" % (i,j,i*j),end=" ")
	print(" ")

print("\n")
for i in range(1,10):
	for k in range(1,10-i):
		print(end="       ")
	for j in range(1,i+1):
		print("%d*%d=%2d" % (i,j,i*j),end=" ")
	print(" ")


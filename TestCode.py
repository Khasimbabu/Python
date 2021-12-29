x = int(input("Enter a Number : "))
 # all prime numbers are greater than 1
if x > 1:
	for i in range(2, x):
		if (x % i) == 0:
			print(str(x) + " is not a Prime number")
			break
	else:
		print(str(x) + " is a Prime number")
else:
	print(str(x) + ' is not a prime number')
'''
def numbercheck(a):
	if(a%2==0):
		print(a, "is a Even number")
	elif(a%2!=0):
		print(a, "is a Odd number")
	else:
		print("Invalid Input")
numbercheck(int(input("Enter a Value : ")))
'''
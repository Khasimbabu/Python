n = int(input("How many numbers? "))

# first two numbers
n1, n2 = 0, 1
count = 0

# check if the number is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nTotal = n1 + n2
       # update values
       n1 = n2
       n2 = nTotal
       count += 1
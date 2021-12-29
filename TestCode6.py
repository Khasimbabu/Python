n=int(input('Enter an Integer number : '))
reverse_number=0
while(n>0):
    remainder = n % 10
    reverse_number = (reverse_number * 10) + remainder
    n = n // 10
print("The reverse number is : {}".format(reverse_number))
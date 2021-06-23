'''n = input()
list=n.split(" ")
print(list)
for i in list:
    print(i)'''

#name = str(input())
#print(name[0],name[1],name[2],name[3])
#for i in name:
 #   print(i)
'''
n = str(input())
x = len(n)
y=0
print(x)
print(y)
while y < x:
    print(n[0:y])
    print('hello')
    y += 1
'''
'''
n = str(input())
x=''
for i in n:
    x=x + i + ' '
print(x.strip())
'''
'''
n = input()
x = n.split(' ')
for i in x:
    print(i)
'''
'''
n = input()
for i in n:
    print(i)
'''
'''
n = str(input())
x=''
for i in n:
    x=x + i + ','
print(x[:-1])
'''
'''
n = input()
x = n.split(" ")
P = eval(x[0])
T = eval(x[1])
R = eval(x[2])
print(x)
print(P, R, T)
SI = (P * T * R) / 100
print(round(SI,2))
'''
'''
radius = float(input())
x = float(22/7)
y = 2 * x * radius
print(round(y,2))
'''
'''
num = int(input())
fact=1
for i in range(2,num+1):
    fact = fact * i
print(fact)
'''
'''
n = int(input())
if n != 0:
    x = []
    for i in range(1,n+1):
        x = i * 9
        print(x)
else:
    print('NULL')
'''
'''
num = int(input())

for i in range(1, 6):
    print(num)
'''
'''
n = 25
x = 5
print(n % x)
print(n / x)
print(n // x)
'''
'''
year = int(input())
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
'''
'''
name = input()
name_new = name.strip()
name_new = name_new.replace(' ','')
print(len(name_new))
'''
'''
num = int(input())
A = num * 1
B = num * 2
C = num * 3
print(A,' ',B,' ',C)
'''
'''
num = int(input())
for i in range(1,num+1):
    if(i % 2 == 0):
        print(i)
'''
'''
num = int(input())
x = 0
for i in range(1,num+1):
    x = x + i
print(x)
'''
'''
from calendar import monthrange
num_days = monthrange(2019, 2)[1]
print(num_days)

import calendar
import datetime
now = datetime.datetime.now()
print (calendar.monthrange(now.year, now.month)[1])
'''
'''
import calendar
import datetime
now = datetime.datetime.now()
num = int(input())
if(num > 0 and num <= 12):
    print (calendar.monthrange(now.year, num)[1])
else:
    print('Invalid Input')
'''
'''
num = int(input())
x = 0
for i in str(num):
    x = x + int(i)
print(x)
'''
'''
num = int(input())
print(num ** 3)
'''
'''
n = str(input())
x=''
for i in n:
    x=x + i + ' '
print(x.strip())
'''
'''
import math
number1 = int(input("ENTER FIRST NUMBER : "))
number2 = int(input("ENTER SECOND NUMBER : "))
print("THE HCF OF ",number1," AND ",number2," IS : ",math.gcd(number1,number2))
'''
'''
n1 = int(input())
n2 = int(input())
if n1 > n2:
    small = n2
else:
    small = n1
for i in range(1,small + 1):
    if((n1 % i == 0) and (n2 % i == 0)):
        result = i
print(result)
'''
'''
num = str(input())
n1 = num.split()
# print(n1)
# print(n1[1])
x1 = int(n1[0])
x2 = int(n1[1])
if x1 > x2:
    small = x2
else:
    small = x1
for i in range(1,small + 1):
    if((x1 % i == 0) and (x2 % i == 0)):
        result = i
print(result)
'''
'''
num = str(input())
x = num[::-1]
print(x)
'''
'''
a = eval(input())
b = eval(input())
c = a + b
print(round(c,1))
'''
'''
num = int(input())
for i in range(1,num+1):
    print(i)
'''
'''
num = int(input())
while(num!=0):
    print(num)
    num = num - 1
'''
'''
num = str(input())
n = num.split()
x = int(n[0])
y = int(n[1])
for i in range(1,y+1):
    print(n[0])
'''
'''
import math
area = int(input())
x = 1/4 *  (math.sqrt(3) * area**2)
print(round(x,2))
'''
'''
num = str(input())
n = num.split()
n1 = int(n[0])
n2 = int(n[1])
if(n1 > n2):
    print(n2)
else:
    print(n1)
'''
'''
n = str(input())
x=''
y=''
for i in n:
    if(int(i)%2==0):
        x = x + i + ' '
    else:
        y=y + i + ' '
print(x.strip())
print(y.strip())
'''
'''
n = str(input())
x=''
y=''
for i in n:
    if(int(i)%2==0):
        x = x + i + ' '
    else:
        y=y + i + ' '
x = x.strip().split()
x.sort()
p=''
for j in range(0,len(x)):
    p = p + x[j] + ' '
print(p.strip())
y = y.strip().split()
y.sort()
q=''
for j in range(0,len(y)):
    q = q + y[j] + ' '
print(q.strip())
'''
'''
n = int(input())
if n != 0:
    x = ''
    for i in range(1,n+1):
        x = x + str(i * 9) + ' '
    print(x.strip())
else:
    print('NULL')
'''
'''
a = int(input())
b = int(input())
c = int(input())
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)
'''
'''
temp = int(input())
f = temp * (9/5) + 32
print(round(f,2))
'''
'''
num = int(input())
for i in range(0,num):
    if(i % 2 != 0):
        j=0
        while(j<11):
            print(i,'*',j,'=', i * j)
            j = j+1
    else:
        print('Even Number')
'''
'''
name = input()
name = name.lower()
a,e,i,o,u = 0

for i in name:
    if(i in ('a','e','i','o','u')):
        if(i=='a'):
            a = a + 1
            print('Count of a: ',x)
        elif (i == 'e'):
            e = e + 1
            print('Count of e: ', x)
        elif (i == 'i'):
            i = i + 1
            print('Count of i: ', x)
        elif (i == 'o'):
            o = o + 1
            print('Count of o: ', x)
        else:
            u = u + 1
            print('Count of u: ', x)
    else:
        print('Not a vowel')
'''
'''
list_1 = [23,44,56,88,100,120]

for i in list_1:
    if i > 1:
        for j in range(2, len(list_1)):
            if (i % j) == 0:
                print(str(i) + " is not a Prime number")
                break
        else:
            print(str(i) + " is a Prime number")
else:
	print(str(i) + ' is not a prime number')
'''
'''
list_1=[100,45,36,1,32]
temp = 0
for i in range(len(list_1)-1,0,-1):
    for j in range(i):
        if list_1[j] < list_1[j+1]:
            temp=list_1[j]
            list_1[j] = list_1[j+1]
            list[j+1] = temp
print(temp)
'''
'''
data = "my name is suman gangopadhyay and I live in Banglore. He hates to eat mangoes and loves chola bhatura."

# Cal the percentage of using vowels, consonants.
# How many times he used AND IS from his data?
mylist = []

mylist = data.split()
print(mylist)
count = 0
count1 = 0
for i in mylist:    
    if (i.upper() == 'AND'):
        count = count + 1
        print('AND is used ', count, ' times')
    elif (i.upper() == 'IS'):
        count1 = count1 + 1
        print('IS used ', count1, ' times')
'''
'''
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
'''
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
'''
'''
n=input("Enter the list of numbers using comma separated : ")
list=n.split(",")
print(list)
for i in list:
    j=i.capitalize()
    print(j)
    # c:\users\kshaik\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip
'''
'''
n=int(input('Enter an Integer number : '))
reverse_number=0
while(n>0):
    remainder = n % 10
    reverse_number = (reverse_number * 10) + remainder
    n = n // 10
print("The reverse number is : {}".format(reverse_number))
'''
'''
#pip install pynum2word
import num2word
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','r')
content=fl.read()
print(content)
fl.close()
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','a')
out = num2word.word(content)
print(out)
fl.write(out)
fl.close()
fl = open('C:/Users/kshaik/Documents/Khasim2020/pythonfile1.txt','r')
print(fl.read())
fl.close()
'''











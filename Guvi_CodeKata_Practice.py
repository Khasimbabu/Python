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
'''
# (c:\users\kshaik\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip)
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
'''
from math import *
n = input()
num=n.split(" ")
print(num)
a = int(num[0])
b = int(num[1])
c = int(num[2])
print(a, b, c)

p = (b * b) - (4 * a * c)
print(p)
X = (-b + sqrt(p)) / (2 * a)
Y = (-b - sqrt(p)) / (2 * a)
print(X)
#print((round(X, 2))
#print(round(Y, 2))
print(f"{X:.2f}")
print(f"{Y:.2f}")
'''
'''
num = input()
num1 = input()

l = num.split(" ")
m = num1.split(" ")

a = l[0]
b = l[1]

if(b in m):
    print("yes")
else:
    print("no")
'''
'''
num = input()
num1 = input()

l = num.split(" ")
m = num1.split(" ")

a = l[0]
b = l[1]
count = 0
for i in m:
    if(i == b):
        count = count + 1
    else:
        print('-1')
print(count)
'''
'''
num = int(input())
if(num>1):
    for i in range(2,num):
        if(num % i == 0):
            print(str(num),' is a Composite number')
            break
    else:
        print(str(num), ' is a Prime number')
else:
    print('Invalid Number')
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])

c = (a * b)/2
print(c)
'''
'''
num = int(input())

num1 = input()
l = num1.split(' ')

min = int(l[0])
max = int(l[1])

if(num > min and num < max):
    print('yes')
else:
    print('no')
'''
'''
num1 = int(input())
num2 = input()
l = num2.split(' ')

a = int(l[0])
b = int(l[1])

print(int(bin(a|b),2))
'''
'''
def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
DecimalToBinary(10)
'''
'''
num = int(input())
count = 0
for i in range(1,num+1):
    count = count + i
print(count)
'''
'''
from math import *
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
c = int(l[2])

if(c == sqrt(a*a + b*b)):
    print('yes')
else:
    print('no')
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
multiplier = 1
resp = 0
for i in range(0,2):
 #   Add each bits
    bit_sum = a%10 + b%10
    print(bit_sum)
 # Negelect carry
    bit_sum = bit_sum % 10
    print(bit_sum)
# Update result
    resp = (bit_sum * multiplier) + resp
    a = a//10
    b = b//10
# Update multiplier
    multiplier = multiplier * 10
print(resp)
'''
'''
from math import *
num = input()
l = num.split(' ')
count = len(l)
lcm = int(l[0])

for i in range(1,count):
    lcm = lcm * int(l[i])//gcd(lcm, int(l[i]))
print(lcm)
'''
'''
num = input()
l = num.split(' ')
min = int(l[0])

for i in l:
    if(int(min) >= int(i)):
        min = i
    else:
        min = min
print(min)
'''
'''
num1 = int(input())
num2 = input()
l = num2.split(' ')
a = int(l[0])
b = int(l[1])
print(int(bin(a&b),2))
'''
'''
from math import *
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
m = a * b
if ((isqrt(m)**2) == m):
    print('yes')
else:
    print('no')
'''
'''
num1 = input()
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
c = int(l[2])
d = int(l[3])
e = int(l[4])

print(b,a,d,c,e)
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
c = int(l[2])

if(a!=b and b!=c):
    print('yes')
else:
    print('no')
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])

if(a<b):
    if(a%a==0 and b%a==0):
        a = a//a
        b = b//a
        if(a<b):
            print(b)
elif(a>b):
    if(a%b==0 and b%b==0):
        a = a/b
        b = b/b
        if(a>b):
            print(a)
else:
    print('-1')
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
c = int(l[2])

if(a==b and b==c and a!=0 and b!=0):
    print('yes')
elif(a==b and b!=c and a!=0 and b!=0):
    print('yes')
elif (a != b and b != c and a != c and a != 0 and b != 0):
    print('yes')
else:
    print('no')
'''
'''
num = input()
l = num.split(' ')
a = int(l[0])
b = int(l[1])
print(a**b)
'''
'''
num = input()
l = num.split(' ')
a = l[0]
b = l[1]
print(b,a)
'''
'''
sample = [2, 4, 6, 8]
test = (x**2 for x in sample)
print(next(test), next(test))
'''
'''
sample='bat'
sample=sample.capitalize()
print(sample)
print(sample.ljust(5,'*'))
'''
'''
sample="world cup"
x=sample.title()
print(x)
print(x[6])
'''
'''
x = 5
while x < 10:
    print(x,end=" ")
    x += 1
    if x == 9:
        break
else:
    print(11)
'''
'''
iteration = 0
while iteration < 5:
  print(iteration)
  iteration += 1
'''
'''
import random
sample=[1,2,3,4,5,6,7,8,9]
random.shuffle(sample)
print(sample[0])
'''
'''
sample="pra"
test='net'
goal='pra'
x=goal.maketrans(sample,test)
print(x[97])
'''
# print('\x67uv\x69')
'''
def fun(x,y):
    if x==0:
        return y
    else:
        return fun(x-1,x+y)
a=fun(5,2)
b=fun(3,4)
print(a,b)
'''
'''
tuple1=('x','y')
tuple1=[tuple1]
print(tuple1)
'''
'''
num1 = input()
num = input()
l = num.split(' ')
x = 0
for i in range(0,num1)
    if(x>=l[i])
'''
'''
data = [10, 20, 30, 40]
print(data)
tmp = str(data).replace(' ', '')
print(tmp)
'''
'''
data = (10,20,30,40)
l = []
sum = 0
l.append(data[0])
for i in range(len(data)-1):
    print(i)
    sum = data[i] + data[i+1]
    l.append(sum)
print(l)
'''
#**************************** Dictionaries *******************#
'''
data = {'id':0, 'name':'suman', 'place':'hyderabad'}
print(type(data))
print(data['id'])
print(data)
data['name'] = 'suman rao'
print(data)
# Iterate a dictionary
for key,value in data.items():
    print(key)
    print(value)
    print(key," = ", value)

for key,value in data.items():
    if(key=='name'):
        key = 'first_name'
    print(key)

for i,j in data.items():
    if(i=='name'):
        i = 'se_name'
    print(i)
'''
'''
input = 'ATGCTTAG'
# output ='TACGAATC'
codeon = {'A':'T','T':'A','C':'G','G':'C'}
out=''
for i in input:
    out+=codeon[i]
print(out)
#    for key, value in codeon.items():
#        if(key==i):
 #           out = str(codeon[i]) + out
# print(out)
 #       print(codeon[i])
'''
'''
input = 'ATGCTTAG'
# output ='TACGAATC'
codeon = {'A':'T','T':'A','C':'G','G':'C'}
out=''
for i in input:
    for key, value in codeon.items():
        if(key==i):
            out = out + str(codeon[key])
        else:
            out=out
print(out)
'''
#**************************** Functions *******************#
'''
def suman():
    """ THIS IS A DOC STRING """
    print("Suman Rao")
suman()
'''
# For getting doc string data in return/output
'''
def suman():
    """ THIS IS A DOC STRING """
    print("Suman Rao")
print(suman.__doc__)
'''
'''
def Add(n1,n2):
    sum = n1 + n2
    return sum
print(Add(10,20))

data = Add(50,100)
print(data)

data = Add('Suman','Rao')
print(data)
'''
# Function with default arguments/parameters
'''
def AreaOfCircle(radius,pi=3.141):
    area = pi * radius * radius
    return area
print(AreaOfCircle(10))
print(AreaOfCircle(10,100))
'''
'''
# Create a function that will return multiple values
def Circle(radius,pi=3.141):
    area = pi * radius * radius
    perimeter = 2 * pi * radius
    return[area, perimeter]
print("Area of Circle : ", Circle(10)[0])
print("Area of Circle : ", Circle(10)[1])
'''
'''
def suman(number, repeat):
    number = int(number)
    repeat = int(repeat)
    for i in number:
        print(number)
    for i in repeat:
        print(repeat)
    for i in range(0,repeat):
        print(number)
suman(2,3)
'''
'''
def suman(number):
    if(type(number)==int):
        print("integer")
    elif(type(number)==float):
        print("float")
    else:
        print("string")
suman('Rao')
'''
#**************************** OOPS of Python *******************#
# class = TV = Is a combination of functions & member variables
# object = Remote = Instance of a class = By using object you can access functions & member variables.
# member variable
# methods = functions inside of a class
# inheritance
'''
class Suman: # define a class
    # member variables
    name = "SumanRao"
    place = "Hyderabad"
    foreign_visit = "20 times"
    # methods = functions inside of a class
    # All methods are functions but All functions are not methods.
    def Hello(self):
        return self.name
    def Add(self,num1,num2):
        sum = num1 + num2
        return sum
# Object for a class
s = Suman()

print(s.Hello())
print(s.name, s.place, s.foreign_visit)
print(s.Add(20,30))
'''
'''
class Suman:
    name = "Suman Rao"
    pi = 3.141
    class Ravi:
        def Hello(self):
            print("Hello function from class Ravi")
        def Alpha(self):
            print(Suman().name)
        def AreaOfCircle(self,radius):
            area = Suman().pi * radius * radius
            return area
s = Suman()
s.Ravi().Hello()
s.Ravi().Alpha()
print(s.Ravi().AreaOfCircle(20))
'''
'''
class Arithmetic:
    x = 20
    y = 30
    def additionOp(self):
        return self.x + self.y
    def addition(self, a, b):
        return a + b
result = Arithmetic()
print(result.addition(2, 3))
print(result.additionOp())
'''
#**************************** Constructor of a class *******************#
'''
class Suman:
    # This is a constructor
    # A constructor is a special methods whose name is the name of the class and it is executed when the object of the class is called.
    def __init__(self):
        print("I am a constructor from class Suman!")
s = Suman()
'''
'''
class Suman:
    def __init__(self,radius):
        self.radius = radius
    def AreaOfCirle(self):
        area = 3.141 * self.radius * self.radius
        return area
s = Suman(20)
print(s.AreaOfCirle())
print(Suman(10).AreaOfCirle())
'''
#***********Destructor********
'''
class Suman:
    def __init__(self):
        print("I am a Constructor")
    def __del__(self):
        print("I am a Destructor")
s = Suman()
del s   # delete everything and clean the memory
'''
#***********DATA Encapsulation********
# Anything that is public inside of the class, can be accessed outside of the class. It s security nightmare.
# To avoid this we need to define them as Private.
'''
class Suman:
    pi = 3.141
    def Hello(self):
        return self.pi
s = Suman()
print(s.pi)

s.pi = 'Suman Rao' # value of pi changes
print(s.pi)
'''
'''
class Suman:
    __pi = 3.141    # __ make the variable to Private
    name = 'Test'   # Public variable.
    def Hello(self):
        return self.__pi
s = Suman()
print(s.Hello())    # You can access the method
print(s.__pi)   # You can't acess the Private member variable from outside of a class. It gives an error.
'''
'''
# You can make a method as Private & variable as Private.
class Suman:
    __pi = 3.141    # Private variable
    name = 'TEST'   # Public variable
    def __Hello(self):  # Private method
        print('I am Private method')
    def Area(self): # Public method
        return self.__pi
    def Sum(self):
        return self.__Hello()
s = Suman()
print(s.Area())
print(s.Sum())
print(s.__Hello())
'''
'''
class Statistical_Class:
    def Average(self):
        pass
    def Mean(self):
        pass
    def Standard_Deviation(self):
        pass
# pass is used to Go On, don't stop.
'''
'''
num1 = input()
num2 = input()
l = num2.split(' ')
count = 0
for i in l:
    if (i == num1):
        count = count + 1
#print(count)
if (count > 1):
    print(count)
else:
    print('0')
'''
#********* HCF of numbers ***********#
# Through the use of Super() method we can call the parent class constructor inside a child class when their is a concept of Inheritence
# Abstract class is a blueprint for other classes (It has predefined methods and member variables)
# With abstract class we can define a common API for a set of sub-classes using Inheritance
# ABC = Abstract Base Classes
import mongo


#************* Modules **************#
# PyPI = Python Package Index
# PIP is standard package manager for Python
# python working directoy > pip install mongo
# python working directoy > pip --version
# python working directoy > pip help
# python working directoy > pip uninstall mongo
# python working directoy > pip list
# python working directoy > python.exe -m pip install --upgrade pip
# python working directoy > pip show flask  #flask is a module name

'''
>>> import sys
>>> for p in sys.path:
...     print(p)
...
'''
#C:\Users\kshaik\AppData\Local\Programs\Python\Python39\python39.zip
#C:\Users\kshaik\AppData\Local\Programs\Python\Python39\DLLs
#C:\Users\kshaik\AppData\Local\Programs\Python\Python39\lib
#C:\Users\kshaik\AppData\Local\Programs\Python\Python39
#C:\Users\kshaik\AppData\Roaming\Python\Python39\site-packages
#C:\Users\kshaik\AppData\Roaming\Python\Python39\site-packages\win32
#C:\Users\kshaik\AppData\Roaming\Python\Python39\site-packages\win32\lib
#C:\Users\kshaik\AppData\Roaming\Python\Python39\site-packages\Pythonwin
#C:\Users\kshaik\AppData\Local\Programs\Python\Python39\lib\site-packages
'''
>>>
'''

#************* Regular Expressions **************#
# RegEX
# 2 types of Regex 1.) POSIX 2.) PERL based


# The ? is to match for zero or one occurance of the pattern left to it
# re.findall() # Returns all the matches
# re.search() # It will return me a single match object
# pip install requests
'''
import re
from urllib.request import urlopen


class Web_Scrapping:
    email_regex = "(\w+@[a-zA-Z]+?\.[a-zA-Z]{2,6})"
# For phone numbers    email_regex = "[987]]"
    def __init__(self, url):
        self.url = url
        self.data = urlopen(self.url).read().decode("utf-8")

    def Email_Scrapping(self):
        email_result = ""
        final_list = []
        email_result = re.findall(self.email_regex, self.data)
        for email in email_result:
            if email not in final_list:
                final_list.append(email)
        return email_result
s = Web_Scrapping("https://indusdictum.com/contact/")
print(s.Email_Scrapping())

'''

# file = open("C:\Users\kshaik\Desktop\Tasks\example.txt", "w")

#file = open("C:\Users\kshaik\Desktop\Tasks\example.txt", "w")
'''
with file:
    for i in range(2,3):
        for j in range(1,11):
            file.write(i,'*',j,'=',i*j)
            file.write("{},'*',{},'=',{}*{}\n".format(i,j,i,j))
file.close()
#file.write()
 #   print('')

'''
'''
number = int(input("Enter your Number # "))
result = 1
if number % 2==0:
    with open("C:\kshaik\Desktop\Tasks\example.txt","w") as file:
        for i in range(1,11):
            result = number * i        
            file.write("{}*{}={}\n".format(number , i , result))
    file.close()
'''
'''
number = int(input("Enter your Number # "))
result = 1
if number % 2==0:
    try:    
        with open("table.txt","w", encoding="utf8") as file:
            for i in range(1,11):
                result = number * i        
                file.write("{}*{}={}\n".format(number , i , result))
        file.close()
    except:
        pass 
else:
        print("ERROR : Kindly use EVEN Numbers !")
'''
'''
number_1 = int(input("Number 1 # "))

number_2 = int(input("Number 2 # "))

try:
    # run the code with/without errors for
    result =  number_1 / number_2
    print("Result = ", result)
except:
    print("ERROR : Their is wrong Input in your program !")
'''
'''
# EXCEPTIONAL HANDLING 

number_1 = int(input("Number 1 # "))

number_2 = int(input("Number 2 # "))

try:
    # run the code with/without errors for
    result =  number_1 / number_2
    print("Result = ", result)
except:
    print("ERROR : Their is wrong Input in your program !")
finally:
    print("Your Code ran successfully !!!")
'''

# mysql -u root -p
# pip install pymysql
# https://www.microsoft.com/en-in/download/details.aspx?id=42642
'''
import pymysql # module driver for python and mysql 

# 1.) database connection 

ip = "localhost"
username = "root"
password = "suman"
database_name = "india"

db = pymysql.connect(host=ip, user=username, password=password) # database connection 

c = db.cursor() # cursor to fetch mysql commands 

print("database connection successful")

db.close()
'''
'''
import pymysql

try:
    ip = "localhost"
    username = "root"
    password = "suman"
    database_name = "india"
    db = pymysql.connect(host=ip, user=username, password=password, db=database_name)
    # FETCH DATA FROM TABLE    
    c = db.cursor()
    sql = """ SELECT * FROM food """
    c.execute(sql)
    result = c.fetchall()
    for data in result:
        id = data[0]
        food_name = data[1]
        country_of_origin = data[2]
        print("ID #",id)
        print("FOOD NAME # ", food_name)
        print("COUNTRY # ", country_of_origin)    
    
    db.close()
except:
    print("ERROR : MySQL Database Connection Error :-(")
    '''
'''
import pymysql

try:
    ip = "localhost"
    username = "root"
    password = "suman"
    database_name = "india"
    db = pymysql.connect(host=ip, user=username, password=password, db=database_name)
    # INSERT DATA INTO THE TABLE
    sql = """ INSERT INTO food(id, item, country) VALUES(1, 'Pizza', 'Italy') """
    c = db.cursor()
    c.execute(sql)
    db.commit()
    print("SUCCESS : DATA ADDED SUCCESSFULLY !")
    
    db.close()
except:
    print("ERROR : MySQL Database Connection Error :-(")
    '''
# https://github.com/sgangopadhyay/Flask-CRUD-App
# https://github.com/sgangopadhyay/CRUD-App-with-Flask-SQLAlchemy

#****************************************************************************
'''import pandas as pd
import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

#print(data)
df = pd.DataFrame(data)
print(df)'''
'''
import pandas as pd
import numpy as np
df3 = pd.DataFrame(np.random.random(size=(5, 3)))
# df3.mean(axis=1)
df3['Mean_value'] = df3.mean(axis=1)
print(df3)
print('-----------')
df4 = df3.sub(df3.mean(axis=1),axis=0)
print(df4)'''
'''
import pandas as pd
import numpy as np
df5 = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
#df5['sum_data']=df5.sum(axis=1)
print(df5)
print("-----------")
df5.loc['5'] = df5.sum(axis=0, skipna=True)
print(df5)
print("-----------")
print(df5[5:].min(axis=1))'''
'''
import pandas as pd
import numpy as np
data = {'col1': [2.5, np.nan, 0.5, np.nan, 5.5, np.nan, np.nan, 2,3.6],
        'col2': [2.6, np.nan, 0.6, np.nan, 5.6, np.nan, np.nan, 2,3.6],
        'col3': [2.9, np.nan, 0.2, np.nan, 5.2, np.nan, np.nan, 2,3.6],
        'col4': [2.8, np.nan, 0.3, np.nan, 5.3, np.nan, np.nan, 2,3.6],
        'col5': [2.7, np.nan, 0.4, np.nan, 5.4, np.nan, np.nan, 2,3.6],
        'col6': [np.nan, 3.3, np.nan, 2.1, np.nan, 2, 4.2,np.nan,np.nan],
        'col7': [np.nan, 3.2, np.nan, 2.2, np.nan, 3, 4.3, np.nan,np.nan],
        'col8': [np.nan, 3.1, np.nan, 2.3, np.nan, 4, 4.4, np.nan,np.nan],
        'col9': [np.nan, 4.4, np.nan, 2.4, np.nan, 5, 4.6, np.nan,np.nan],
        'col10': [np.nan, 5.5, np.nan, 2.5, np.nan, 6, 4.7, np.nan,np.nan]}
df7 = pd.DataFrame(data)
print(df7)
print("----------")
#df7[((df7.iloc[:]=='NaN').value_counts())==3]
#df7 = (df7.iloc[:,2:3]).isna().any(axis=1)
#nan_val = (df7.iloc[0].isna().any(axis=1))
#df7[(df7["col3"]=='True')]
#print(nan_val)
#print(((df7.isna().iloc[0])==True).value_counts()==3)
#print(df7.iloc[0])
'''
import pandas as pd
import numpy as np
'''
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
print(df)
print(df.sort_values(by=['grps','vals'],ascending=[True,False]))
df1 = (df.groupby("grps").sum())
print(df1)
'''
'''
df = pd.DataFrame({'A': [1,2,3,4,8,7,6,5,9,10,11,12,13,14,15,16,17,18,19,20],
                   'B': [1,2,3,4,15,6,7,8,9,10,11,22,13,14,25,16,17,38,19,20]})

print(df['A'])
df1 = df['A'].count()
print(df1)
count=10
x=0
for i in range(1,100,10):
        if(count<=i):
                x = x + df['B']
count=count + 1
print(x)
'''
#df1=df.iloc[:10]
#df1 = df[['A','B']].groupby("A").count().sort_values('A',ascending=False)
#print(df1)
'''
s = pd.Series([7, 2, 0, 3, 4, 2, 5, 0, 3, 4])

x = (s.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()
print(x)
'''
'''
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#In []:
x = (df['X'] != 0).cumsum()
y = x != x.shift()
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()
print(df['Y'])
'''
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
              'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
              'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})

#print(df)
#df["FlightNumber"] = df["FlightNumber"] + 10
'''df["FlightNumber"] = df["FlightNumber"].interpolate().astype(int)
print(df)

temp = df.From_To.str.split('_', expand=True)
temp.columns = ['From', 'To']
temp['From']=temp['From'].str.capitalize()
temp['To']=temp['To'].str.capitalize()
df = df.drop('From_To', axis=1)
df = df.join(temp)
df['Airline']=df['Airline'].str.extract('([a-zA-Z\s]+)', expand=False).str.strip()
print(temp)
print(df)
# delays = df.RecentDelays.str.split()
delays = df["RecentDelays"].apply(pd.Series)
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
df = df.drop('RecentDelays', axis=1).join(delays)
print(delays)
print(delays.columns)
print(df)
'''
'''
df = pd.DataFrame({'x': [0,0,0],
                   'y': [0,1,2]})
print(df)
df['safe']= 0
df['mine']= 1
df['adjacent']= 1
print(df)
'''
'''
import pandas as pd
import numpy as np
p = pd.tools.util.cartesian_product([np.arange(X), np.arange(Y)])
df = pd.DataFrame(np.asarray(p).T, columns=['x', 'y'])
print(df)
'''
a = '1234'
print (a[::2])
print(a[1:1:2])
a = '1234'
print (a[3:0:-1])